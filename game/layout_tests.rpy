init python:
    def dialogue_theme(node):
        name = node.filename.replace("\\", "/").rsplit("/", 1)[-1]
        if name.startswith("03_"):
            return "southpark"
        if name.startswith("04_"):
            return "minecraft"
        if name.startswith("05_"):
            return "sims"
        if name.startswith("06_"):
            return "marvel"
        if name == "endings.rpy":
            with renpy.file("endings.rpy") as source:
                lines = source.read().decode("utf-8").splitlines()
            world = "storybook"
            for line in lines[:node.linenumber]:
                if 'current_ending == "stay_' in line:
                    value = line.split('current_ending == "stay_')[1].split('"')[0]
                    world = value if value in THEMES else "storybook"
                elif 'current_ending == "home"' in line or 'current_ending == "open_door"' in line:
                    world = "storybook"
            return world
        return "storybook"

    def check_dialogue_layout():
        failures = []
        heights = []
        count = 0
        for node in renpy.game.script.all_stmts:
            if isinstance(node, renpy.ast.Say) and ("/game/" in node.filename or node.filename.startswith("game/")) and not node.filename.endswith("_tests.rpy"):
                spec = THEMES[dialogue_theme(node)]
                what = node.what.replace("[[", "[")
                displayable = Text(what, font=spec["body"], size=spec["body_size"], line_spacing=6, substitute=False)
                text_w, text_h = dialogue_text_area(dialogue_theme(node))
                width, height = renpy.render(displayable, text_w, text_h, 0, 0).get_size()
                heights.append((height, node.filename, node.linenumber))
                count += 1
                if width > text_w or height > text_h:
                    failures.append((node.filename, node.linenumber, width, height))
        _test.layout_checked = count
        _test.layout_failures = failures
        print("Largest text:", sorted(heights, reverse=True)[:5])
        print("Dialogue layout:", count, "blocks; failures:", failures)
        if count < 300 or failures:
            raise AssertionError((count, failures))

    def check_name_layout():
        for theme, spec in THEMES.items():
            for name in ("Ольга Игоревна", "Доктор Стрэндж", "Перевод жеста"):
                width, height = renpy.render(Text(name, font=spec["label"], size=spec["label_size"]), 480, 52, 0, 0).get_size()
                if width > 480 or height > 52:
                    raise AssertionError((theme, name, width, height))

testsuite layout:
    testcase dialogue:
        run Start()
        advance until screen "say"
        run Function(check_dialogue_layout)
        assert eval _test.layout_checked >= 300
        assert eval _test.layout_failures == []
    testcase names:
        run Start()
        advance until screen "say"
        run Function(check_name_layout)
