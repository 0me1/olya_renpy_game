"""Compare all Windows PE icon resource payloads to the supplied ICO (stdlib)."""
from pathlib import Path
import hashlib
import struct
import sys


def verify(executable, icon):
    data = Path(executable).read_bytes()
    ico = Path(icon).read_bytes()
    u16 = lambda offset: struct.unpack_from('<H', data, offset)[0]
    u32 = lambda offset: struct.unpack_from('<I', data, offset)[0]
    assert data[:2] == b'MZ'
    pe = u32(0x3c)
    assert data[pe:pe+4] == b'PE\0\0'
    count = u16(pe + 6)
    optional_size = u16(pe + 20)
    optional = pe + 24
    magic = u16(optional)
    assert magic in (0x10b, 0x20b)
    directory = optional + (112 if magic == 0x20b else 96)
    resource_rva = u32(directory + 16)
    sections = []
    for index in range(count):
        offset = optional + optional_size + index * 40
        virtual_size, virtual, raw_size, raw = struct.unpack_from('<IIII', data, offset + 8)
        sections.append((virtual, max(virtual_size, raw_size), raw))
    def physical(rva):
        for virtual, size, raw in sections:
            if virtual <= rva < virtual + size:
                return raw + rva - virtual
        raise AssertionError(('RVA outside sections', rva))
    base = physical(resource_rva)
    resources = {}
    def walk(relative=0, path=()):
        offset = base + relative
        named, ids = struct.unpack_from('<HH', data, offset + 12)
        assert len(path) <= 3
        for index in range(named + ids):
            key, value = struct.unpack_from('<II', data, offset + 16 + index * 8)
            current = path + (key,)
            if value & 0x80000000:
                walk(value & 0x7fffffff, current)
            else:
                rva, size = struct.unpack_from('<II', data, base + value)
                start = physical(rva)
                resources[current] = data[start:start+size]
    walk()
    reserved, kind, count = struct.unpack_from('<HHH', ico)
    assert reserved == 0 and kind == 1
    expected = {}
    for index in range(count):
        width, height, colors, reserved, planes, bits, size, offset = struct.unpack_from('<BBBBHHII', ico, 6+index*16)
        key = (width or 256, height or 256)
        expected[key] = hashlib.sha256(ico[offset:offset+size]).digest()
    groups = [payload for key, payload in resources.items() if key[0] == 14]
    assert groups
    found = False
    for group in groups:
        _, kind, entries = struct.unpack_from('<HHH', group)
        if kind != 1 or entries != count:
            continue
        actual = {}
        for index in range(entries):
            width, height, colors, reserved, planes, bits, size, image_id = struct.unpack_from('<BBBBHHIH', group, 6+index*14)
            payloads = [payload for key, payload in resources.items() if key[0] == 3 and key[1] == image_id]
            assert payloads and all(len(p) == size for p in payloads)
            actual[(width or 256, height or 256)] = hashlib.sha256(payloads[0]).digest()
        if actual == expected:
            found = True
    assert found, 'Embedded EXE icons differ from supplied ICO'
    print('Windows EXE resources verified: all ICO payloads match:', sorted(w for w, h in expected))

if __name__ == '__main__':
    verify(sys.argv[1], sys.argv[2])
