init python:
    import json
    with renpy.file("art_layout.json") as _art_file:
        ART_LAYOUT = json.load(_art_file)
    ART_POSES = list(ART_LAYOUT)
    CAST_WORLD = {"susan": "housewives", "bree": "housewives", "gabrielle": "housewives", "carrie": "manhattan", "miranda": "manhattan", "cartman": "southpark", "kyle": "southpark", "randy": "southpark", "villager": "minecraft", "bella": "sims", "strange": "marvel", "wong": "marvel"}
    PREVIEW_BG = {"office": "office_evening", "housewives": "wisteria_kitchen", "manhattan": "manhattan_bar", "southpark": "southpark_street", "minecraft": "minecraft_house", "sims": "sims_home", "marvel": "marvel_hall"}
    def prepare_pose_preview(relative):
        parts = relative.split("/")
        world = parts[1] if parts[0] == "olya" else CAST_WORLD[parts[1]]
        enter_world(world)
        renpy.scene()
        renpy.show("bg " + PREVIEW_BG[world])
        pose = parts[-1].removesuffix(".png")
        if parts[0] == "olya":
            renpy.show("olya " + world + " " + pose, at_list=[left_actor])
        else:
            default_pose = {"housewives": "pie", "minecraft": "confused"}.get(world, "neutral")
            renpy.show("olya " + world + " " + default_pose, at_list=[left_actor])
            cast_pose(parts[1], pose)
        _test.pose_world = world

label pose_preview:
    $ prepare_pose_preview(_test.pose)
    $ renpy.say("Доктор Стрэндж" if "strange/" in _test.pose else "Ольга Игоревна", "Все русские буквы: АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ. Пауза — это тоже решение… «Давай посмотрим», — сказала Оля.")
    return

testsuite integration:
    testcase poses:
        parameter pose = ['cast/bella/greeting.png', 'cast/bella/supportive.png', 'cast/bella/suspicious.png', 'cast/bree/base.png', 'cast/bree/approving.png', 'cast/bree/strict.png', 'cast/bree/surprised.png', 'cast/carrie/neutral.png', 'cast/carrie/explaining.png', 'cast/carrie/laugh.png', 'cast/carrie/surprised.png', 'cast/carrie/thinking.png', 'cast/carrie/greeting.png', 'cast/cartman/proud.png', 'cast/cartman/angry.png', 'cast/cartman/scared.png', 'cast/gabrielle/base.png', 'cast/gabrielle/smirk.png', 'cast/gabrielle/indignant.png', 'cast/gabrielle/laugh.png', 'cast/kyle/neutral.png', 'cast/kyle/indignant.png', 'cast/kyle/explaining.png', 'cast/miranda/neutral.png', 'cast/miranda/skeptical.png', 'cast/miranda/explaining.png', 'cast/miranda/surprised.png', 'cast/miranda/supportive.png', 'cast/randy/proud.png', 'cast/randy/confused.png', 'cast/randy/panicked.png', 'cast/strange/explaining.png', 'cast/strange/magic.png', 'cast/susan/base.png', 'cast/susan/worried.png', 'cast/susan/relieved.png', 'cast/susan/serious.png', 'cast/villager/neutral.png', 'cast/villager/trade.png', 'cast/wong/neutral.png', 'cast/wong/skeptical.png', 'cast/wong/approving.png', 'olya/housewives/angry.png', 'olya/housewives/confused.png', 'olya/housewives/gossip.png', 'olya/housewives/pie.png', 'olya/housewives/relief.png', 'olya/housewives/scared.png', 'olya/housewives/thinking.png', 'olya/manhattan/neutral.png', 'olya/manhattan/confused.png', 'olya/manhattan/happy.png', 'olya/manhattan/ironic.png', 'olya/marvel/neutral.png', 'olya/marvel/confused.png', 'olya/marvel/power.png', 'olya/marvel/scared.png', 'olya/minecraft/confused.png', 'olya/minecraft/pickaxe.png', 'olya/minecraft/scared.png', 'olya/office/neutral.png', 'olya/office/angry.png', 'olya/office/happy.png', 'olya/office/scared.png', 'olya/office/skeptical.png', 'olya/office/sleepy.png', 'olya/sims/neutral.png', 'olya/sims/confused.png', 'olya/sims/happy.png', 'olya/sims/panic.png', 'olya/southpark/neutral.png', 'olya/southpark/angry.png', 'olya/southpark/confused.png', 'olya/southpark/scared.png']
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        $ _test.pose = pose
        run Jump("pose_preview")
        assert screen "say" timeout 2.0
        assert eval current_world == _test.pose_world
        assert eval sum(renpy.showing(tag) for tag in CAST_TAGS) <= 1
        pause 0.1
        screenshot f"v2/poses/{pose}.png"

    testcase birthday:
        run Start()
        $ preferences.text_cps = 0
        $ preferences.transitions = 0
        $ current_ending = "home"
        run Jump("ending_scene")
        advance until "Дома праздничный свет встретил Олю уже по другую сторону рабочего дня. В телефоне одно за другим открывались теплые сообщения. Без выдуманного прошлого, без обязательных больших слов — просто от людей, которым она дорога."
        assert eval renpy.showing("bg birthday_home")
        assert eval renpy.showing("olya office happy")
        screenshot "v2/birthday.png"

    testcase music_save_restore:
        run Start()
        $ preferences.text_cps = 0
        advance until screen "choice"
        assert eval renpy.music.get_playing(channel="music") == "audio/music/office_airport_lounge.ogg" timeout 3.0
        run Preference("music volume", 0.35)
        run FileSave(2, confirm=False)
        click "Сначала разберусь с этим"
        advance until screen "choice"
        assert eval current_world == "housewives"
        pause 1.6
        assert eval renpy.music.get_playing(channel="music") is None
        run FileLoad(2, confirm=False)
        assert eval current_world == "office" timeout 2.0
        assert eval ui_world == "storybook"
        assert eval renpy.music.get_playing(channel="music") == "audio/music/office_airport_lounge.ogg" timeout 3.0
        assert eval abs(preferences.get_volume("music") - 0.35) < 0.01
        run Preference("music volume", 1.0)

    testcase credits:
        click "Авторы и музыка"
        assert screen "credits"
        assert eval "Kevin MacLeod" in MUSIC_CREDITS
        assert eval "https://creativecommons.org/licenses/by/4.0/" in MUSIC_CREDITS
        screenshot "v2/credits.png"
        click "Главное меню"
        assert screen "main_menu"
