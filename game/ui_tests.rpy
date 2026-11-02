testsuite interface:
    testcase themes:
        parameter world = ["office", "housewives", "manhattan", "southpark", "minecraft", "sims", "marvel"]
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        if eval world != "office":
            run Jump("chapter_" + world)
        advance until screen "say"
        assert eval ui_world == (world if world in ("southpark", "minecraft", "sims", "marvel") else "storybook")
        pause 0.3
        screenshot f"themes/{world}_say.png"
        advance until screen "choice"
        pause 0.3
        screenshot f"themes/{world}_choice.png"
        click "Сохранить"
        assert screen "save"
        screenshot f"themes/{world}_save.png"
        click "Продолжить"
        assert screen "choice" timeout 2.0

    testcase menus:
        run Start()
        $ preferences.text_cps = 0
        advance until screen "choice"
        click "История"
        assert screen "history"
        assert eval len(_history_list) > 0
        screenshot "menus/history.png"
        click "Настройки"
        assert screen "preferences"
        screenshot "menus/preferences.png"
        run Preference("display", "fullscreen")
        pause 0.3
        run Preference("display", "window")
        click "Управление"
        assert screen "help"
        screenshot "menus/help.png"
        run MainMenu(confirm=False)
        assert screen "main_menu"
        screenshot "menus/main.png"
        click "Коллекция концовок"
        assert screen "gallery"
        screenshot "menus/gallery.png"

    testcase new_game:
        run Start()
        $ preferences.text_cps = 0
        $ visited_worlds.append("marvel")
        $ chapter_choices["marvel"] = {"solution": "test"}
        $ discovered_clues.append("test")
        $ _test.collection_before = list(persistent.unlocked_endings)
        run MainMenu(confirm=False)
        run Start()
        advance until screen "choice"
        assert eval current_world == "office"
        assert eval visited_worlds == []
        assert eval chapter_choices == {}
        assert eval discovered_clues == []
        assert eval persistent.unlocked_endings == _test.collection_before

    testcase gallery_replay:
        parameter ending = ["stay_housewives", "stay_manhattan", "stay_southpark", "stay_minecraft", "stay_sims", "stay_marvel", "home", "open_door"]
        run Start()
        $ preferences.text_cps = 0
        advance until screen "choice"
        $ preserved = (list(visited_worlds), dict(chapter_choices), current_world, ui_world)
        click "Сохранить"
        click "Коллекция"
        assert eval ending in persistent.unlocked_endings
        click expression (dict(ENDINGS)[ending])
        assert eval _in_replay is not None
        advance until screen "gallery"
        assert eval _in_replay is None
        assert eval (visited_worlds, chapter_choices, current_world, ui_world) == preserved
        click "Продолжить"
        assert screen "choice" timeout 2.0

    testcase save_transition:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        run Jump("chapter_minecraft")
        advance until screen "choice"
        click "Собрать дерево и построить свое укрытие"
        advance until screen "choice"
        click "Обменяться с жителем"
        advance until screen "choice"
        click "Обойти по освещенному гребню"
        advance until screen "choice"
        assert eval ui_world == "minecraft"
        run FileSave(1, confirm=False)
        click "Попрощаться с жителем и пройти к экрану «Создать жизнь»"
        advance until screen "choice"
        assert eval current_world == "sims"
        assert eval ui_world == "sims"
        run FileLoad(1, confirm=False)
        assert screen "choice"
        assert eval current_world == "minecraft"
        assert eval ui_world == "minecraft"
        assert eval chapter_choices["minecraft"]["resource"] == "base"

    testcase gallery_without_game:
        parameter ending = ["stay_housewives", "stay_manhattan", "stay_southpark", "stay_minecraft", "stay_sims", "stay_marvel", "home", "open_door"]
        assert screen "main_menu"
        $ preferences.text_cps = 0
        click "Коллекция концовок"
        assert screen "gallery"
        click expression (dict(ENDINGS)[ending])
        assert eval _in_replay is not None
        advance until screen "gallery"
        assert eval _in_replay is None
        assert eval main_menu
        click "Главное меню"
        assert screen "main_menu"

    testcase first_chapter_cast:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        run Jump("chapter_housewives")
        advance until screen "choice"
        keysym "K_DOWN"
        keysym "K_RETURN"
        advance until "О, прекрасно, ты уже здесь!"
        screenshot "cast/susan.png"
        assert eval renpy.showing("susan base")
        assert eval renpy.showing("olya housewives pie")
        advance until screen "choice"
        click "Спросить Бри напрямую"
        advance until "Я не против переноса. Я против того, чтобы узнать о нем, когда все уже стоят у двери."
        assert eval renpy.showing("bree strict")
        assert eval not renpy.showing("susan")
        screenshot "cast/bree.png"
