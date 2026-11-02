init python:
    def check_dialogue_layout():
        failures = []
        count = 0
        for node in renpy.game.script.all_stmts:
            if isinstance(node, renpy.ast.Say) and ("/game/" in node.filename or node.filename.startswith("game/")):
                what = node.what.replace("[[", "[")
                displayable = Text(what, font="DejaVuSans.ttf", size=34, line_spacing=6, substitute=False)
                width, height = renpy.render(displayable, 1530, 220, 0, 0).get_size()
                count += 1
                if width > 1530 or height > 220:
                    failures.append((node.filename, node.linenumber, width, height))
        _test.layout_checked = count
        _test.layout_failures = failures
        renpy.log("Dialogue layout: {} blocks checked; failures: {}".format(count, failures))
        if count < 300:
            raise AssertionError("Not enough dialogue nodes inspected: {}".format(count))
        if failures:
            raise AssertionError(failures)

testsuite layout:
    testcase dialogue:
        run Start()
        advance until screen "say"
        run Function(check_dialogue_layout)
        assert eval _test.layout_checked >= 300
        assert eval _test.layout_failures == []
