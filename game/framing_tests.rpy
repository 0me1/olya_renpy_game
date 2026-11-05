init python:
    def switch_frame_pose(relative):
        parts = relative.split("/")
        pose = parts[-1].removesuffix(".png")
        if parts[0] == "olya":
            renpy.show("olya " + parts[1] + " " + pose, at_list=[left_actor])
        else:
            cast_pose(parts[1], pose)

    def simulate_legacy_placement():
        for tag in ("olya",) + CAST_TAGS:
            if renpy.showing(tag):
                attributes = renpy.get_attributes(tag)
                old = Transform(xalign=0.12 if tag == "olya" else 0.88, ypos=0.77, yanchor=1.0, zoom=0.49)
                renpy.show(" ".join((tag,) + attributes), at_list=[old])

    def frame_snapshot():
        result = {}
        for tag in ("olya",) + CAST_TAGS:
            if not renpy.showing(tag):
                continue
            attrs = renpy.get_attributes(tag)
            relative = ("olya/" + "/".join(attrs) if tag == "olya" else "cast/" + tag + "/" + attrs[0]) + ".png"
            data = ART_LAYOUT[relative]
            x, y, w, h = renpy.get_image_bounds(tag)
            sx, sy = w / data["canvas"][0], h / data["canvas"][1]
            left, top, right, bottom = data["derived_alpha_bbox"]
            assert y + bottom * sy >= 1120, (relative, "visible cut", y + bottom * sy)
            assert y + top * sy >= 24, (relative, "head crop")
            assert x + left * sx >= 20 and x + right * sx <= 1900, (relative, "side crop")
            result[tag] = (x, y, w, h)
        assert result
        return result

    def check_choice_text():
        checked = 0
        for node in renpy.game.script.all_stmts:
            if not isinstance(node, renpy.ast.Menu) or node.filename.endswith("framing_tests.rpy"):
                continue
            captions = [item[0] for item in node.items if item[0]]
            if not captions:
                continue
            spec = THEMES[dialogue_theme(node)]
            theme = dialogue_theme(node)
            size = choice_label_size(len(captions), theme)
            outer_w, outer_h = choice_dimensions(len(captions), theme)
            width = outer_w - 48
            maximum_height = outer_h - (16 if theme == "southpark" else 24)
            for caption in captions:
                w, h = renpy.render(Text(caption, font=spec["label"], size=size, text_align=0.5), width, maximum_height, 0, 0).get_size()
                assert w <= width and h <= maximum_height, (node.filename, caption, w, h, width)
                checked += 1
        _test.captions_checked = checked

screen framing_explore(with_panel=False):
    if with_panel:
        use lower_backdrop
    textbutton "Осмотреть предмет":
        xpos 1450 ypos 930
        action Return("examined")

label framing_probe:
    $ prepare_pose_preview(_test.pose)
    with dissolve
    o "Я осмотрюсь и решу, что делать дальше. Времени достаточно, можно не торопиться."
    menu:
        "Проверить заявление и спокойно продолжить путешествие":
            pass
        "Осмотреться, прежде чем выбирать следующий путь":
            pass
        "Остаться здесь и разобраться в происходящем":
            pass
    o "Хорошо. Теперь можно продолжать."
    window hide
    call screen framing_explore(False)
    $ _test.examined = _return
    o "Предмет осмотрен."
    return

label framing_passive_probe:
    $ prepare_pose_preview(_test.pose)
    call screen framing_explore(True)
    $ _test.passive_result = _return
    o "Подложка не помешала осмотреть предмет."
    return

testsuite framing:
    testcase poses:
        parameter pose = ['cast/bella/greeting.png', 'cast/bella/supportive.png', 'cast/bella/suspicious.png', 'cast/bree/base.png', 'cast/bree/approving.png', 'cast/bree/strict.png', 'cast/bree/surprised.png', 'cast/carrie/neutral.png', 'cast/carrie/explaining.png', 'cast/carrie/laugh.png', 'cast/carrie/surprised.png', 'cast/carrie/thinking.png', 'cast/carrie/greeting.png', 'cast/cartman/proud.png', 'cast/cartman/angry.png', 'cast/cartman/scared.png', 'cast/gabrielle/base.png', 'cast/gabrielle/smirk.png', 'cast/gabrielle/indignant.png', 'cast/gabrielle/laugh.png', 'cast/kyle/neutral.png', 'cast/kyle/indignant.png', 'cast/kyle/explaining.png', 'cast/miranda/neutral.png', 'cast/miranda/skeptical.png', 'cast/miranda/explaining.png', 'cast/miranda/surprised.png', 'cast/miranda/supportive.png', 'cast/randy/proud.png', 'cast/randy/confused.png', 'cast/randy/panicked.png', 'cast/strange/explaining.png', 'cast/strange/magic.png', 'cast/susan/base.png', 'cast/susan/worried.png', 'cast/susan/relieved.png', 'cast/susan/serious.png', 'cast/villager/neutral.png', 'cast/villager/trade.png', 'cast/wong/neutral.png', 'cast/wong/skeptical.png', 'cast/wong/approving.png', 'olya/housewives/angry.png', 'olya/housewives/confused.png', 'olya/housewives/gossip.png', 'olya/housewives/pie.png', 'olya/housewives/relief.png', 'olya/housewives/scared.png', 'olya/housewives/thinking.png', 'olya/manhattan/neutral.png', 'olya/manhattan/confused.png', 'olya/manhattan/happy.png', 'olya/manhattan/ironic.png', 'olya/marvel/neutral.png', 'olya/marvel/confused.png', 'olya/marvel/power.png', 'olya/marvel/scared.png', 'olya/minecraft/confused.png', 'olya/minecraft/pickaxe.png', 'olya/minecraft/scared.png', 'olya/office/neutral.png', 'olya/office/angry.png', 'olya/office/happy.png', 'olya/office/scared.png', 'olya/office/skeptical.png', 'olya/office/sleepy.png', 'olya/sims/neutral.png', 'olya/sims/confused.png', 'olya/sims/happy.png', 'olya/sims/panic.png', 'olya/southpark/neutral.png', 'olya/southpark/angry.png', 'olya/southpark/confused.png', 'olya/southpark/scared.png']
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        $ _test.pose = pose
        run Jump("framing_probe")
        assert screen "say" timeout 3.0
        $ _test.before = frame_snapshot()
        screenshot f"framing/{pose}-dialogue.png"
        advance until screen "choice"
        assert eval frame_snapshot() == _test.before
        assert id "choice_backdrop"
        screenshot f"framing/{pose}-choice.png"
        click "Проверить заявление и спокойно продолжить путешествие"
        assert screen "say" timeout 2.0
        assert eval frame_snapshot() == _test.before
        screenshot f"framing/{pose}-answer.png"
        advance until screen "framing_explore"
        assert eval frame_snapshot() == _test.before
        screenshot f"framing/{pose}-adventure.png"
        click "Осмотреть предмет"
        assert eval _test.examined == "examined" timeout 2.0

    testcase choice_text:
        run Start()
        advance until screen "say"
        run Function(check_choice_text)
        assert eval _test.captions_checked >= 40

    testcase passive_panel:
        run Start()
        $ _test.pose = "olya/office/neutral.png"
        run Jump("framing_passive_probe")
        assert screen "framing_explore" timeout 2.0
        click "Осмотреть предмет"
        assert eval _test.passive_result == "examined" timeout 2.0

    testcase hidden_interface:
        parameter pose = ['olya/office/neutral.png', 'olya/minecraft/pickaxe.png', 'cast/kyle/neutral.png', 'cast/carrie/greeting.png', 'cast/strange/magic.png']
        run Start()
        $ preferences.text_cps = 0
        $ _test.pose = pose
        run Jump("framing_probe")
        assert screen "say" timeout 3.0
        $ _test.before = frame_snapshot()
        keysym "hide_windows"
        pause 0.1
        assert eval frame_snapshot() == _test.before
        screenshot f"framing/hidden/{pose}.png"
        click pos (50, 50)
        assert screen "say" timeout 2.0
        click "Сохранить"
        click "Продолжить"
        assert eval frame_snapshot() == _test.before

    testcase display_and_load:
        parameter display = ["window", "fullscreen"]
        run Start()
        $ preferences.text_cps = 0
        $ _test.pose = "cast/kyle/explaining.png"
        run Preference("display", display)
        run Jump("framing_probe")
        advance until screen "choice"
        $ _test.saved_frame = frame_snapshot()
        run FileSave(3, confirm=False)
        click "Проверить заявление и спокойно продолжить путешествие"
        assert screen "say" timeout 2.0
        run FileLoad(3, confirm=False)
        assert screen "choice" timeout 3.0
        assert eval frame_snapshot() == _test.saved_frame
        screenshot f"framing/{display}-loaded.png"
        run Preference("display", "window")

    testcase emotion_and_fade:
        parameter (base, changed) = [('cast/bella/greeting.png', 'cast/bella/suspicious.png'), ('cast/bree/base.png', 'cast/bree/surprised.png'), ('cast/carrie/neutral.png', 'cast/carrie/greeting.png'), ('cast/cartman/proud.png', 'cast/cartman/scared.png'), ('cast/gabrielle/base.png', 'cast/gabrielle/laugh.png'), ('cast/kyle/neutral.png', 'cast/kyle/explaining.png'), ('cast/miranda/neutral.png', 'cast/miranda/supportive.png'), ('cast/randy/proud.png', 'cast/randy/panicked.png'), ('cast/strange/explaining.png', 'cast/strange/magic.png'), ('cast/susan/base.png', 'cast/susan/serious.png'), ('cast/villager/neutral.png', 'cast/villager/trade.png'), ('cast/wong/neutral.png', 'cast/wong/approving.png'), ('olya/housewives/angry.png', 'olya/housewives/thinking.png'), ('olya/manhattan/neutral.png', 'olya/manhattan/ironic.png'), ('olya/marvel/neutral.png', 'olya/marvel/scared.png'), ('olya/minecraft/confused.png', 'olya/minecraft/pickaxe.png'), ('olya/office/neutral.png', 'olya/office/sleepy.png'), ('olya/sims/neutral.png', 'olya/sims/panic.png'), ('olya/southpark/neutral.png', 'olya/southpark/scared.png')]
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 1
        $ _test.pose = base
        run Jump("framing_probe")
        assert screen "say" timeout 3.0
        $ _test.before = frame_snapshot()
        run Function(switch_frame_pose, changed)
        run With(dissolve)
        pause 0.1
        assert eval frame_snapshot() == _test.before
        screenshot f"framing/emotions/{changed}.png"
        $ _test.hidden_tag = "olya" if changed.startswith("olya/") else changed.split("/")[1]
        run Function(renpy.hide, _test.hidden_tag)
        run With(dissolve)
        pause 0.1
        assert eval not renpy.showing(_test.hidden_tag)
        run Function(switch_frame_pose, changed)
        run With(dissolve)
        pause 0.1
        assert eval frame_snapshot() == _test.before


    testcase legacy_placement:
        parameter pose = ["olya/minecraft/pickaxe.png", "cast/kyle/explaining.png", "olya/office/neutral.png"]
        run Start()
        $ preferences.text_cps = 0
        $ _test.pose = pose
        run Jump("framing_probe")
        advance until screen "choice"
        if eval current_world == "office":
            run Function(renpy.show, "olya office neutral", at_list=[center_actor])
        $ _test.correct_frame = frame_snapshot()
        run Function(simulate_legacy_placement)
        run FileSave(4, confirm=False)
        run FileLoad(4, confirm=False)
        assert screen "choice" timeout 3.0
        assert eval frame_snapshot() == _test.correct_frame
