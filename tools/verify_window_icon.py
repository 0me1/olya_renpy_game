"""Read the running SDL/X11 window icon, without changing desktop settings."""
from pathlib import Path
import re
import subprocess
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
tree = subprocess.check_output(['xwininfo', '-root', '-tree'], text=True)
windows = re.findall(r'^\s*(0x[0-9a-f]+) "В порядке перевода"', tree, re.M)
assert len(windows) == 1, ('Expected exactly one game window', windows)
# Xlib returns full 32-bit CARDINAL data; xprop may abbreviate large icons.
import ctypes as C
import ctypes.util
x11 = C.CDLL(C.util.find_library("X11"))
x11.XOpenDisplay.argtypes = [C.c_char_p]
x11.XOpenDisplay.restype = C.c_void_p
x11.XInternAtom.argtypes = [C.c_void_p, C.c_char_p, C.c_int]
x11.XInternAtom.restype = C.c_ulong
x11.XGetWindowProperty.argtypes = [C.c_void_p, C.c_ulong, C.c_ulong, C.c_long, C.c_long, C.c_int, C.c_ulong, C.POINTER(C.c_ulong), C.POINTER(C.c_int), C.POINTER(C.c_ulong), C.POINTER(C.c_ulong), C.POINTER(C.POINTER(C.c_ubyte))]
x11.XFree.argtypes = [C.c_void_p]
x11.XCloseDisplay.argtypes = [C.c_void_p]
display = x11.XOpenDisplay(None)
assert display
atom = x11.XInternAtom(display, b"_NET_WM_ICON", 0)
kind, fmt, count, after = C.c_ulong(), C.c_int(), C.c_ulong(), C.c_ulong()
buffer = C.POINTER(C.c_ubyte)()
status = x11.XGetWindowProperty(display, int(windows[0], 16), atom, 0, 1000000, 0, 0, C.byref(kind), C.byref(fmt), C.byref(count), C.byref(after), C.byref(buffer))
assert status == 0 and fmt.value == 32 and after.value == 0
array = C.cast(buffer, C.POINTER(C.c_ulong))
numbers = [array[i] & 0xffffffff for i in range(count.value)]
x11.XFree(buffer)
x11.XCloseDisplay(display)
image = Image.open(ROOT / 'game/gui/window_icon.png').convert('RGBA')
expected = [(a << 24) | (r << 16) | (g << 8) | b for r, g, b, a in image.get_flattened_data()]
position = 0
matched = False
while position + 2 <= len(numbers):
    width, height = numbers[position:position+2]
    pixels = numbers[position+2:position+2+width*height]
    assert len(pixels) == width * height
    if (width, height) == image.size and pixels == expected:
        matched = True
    position += 2 + width * height
assert matched, 'Window icon pixels do not match the configured PNG'
print(f'X11 window icon verified: {image.width}x{image.height}; every ARGB pixel matches configured PNG.')
