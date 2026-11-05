init python:
    UI_COLORS = {"storybook": "#713047", "sims": "#10265f", "minecraft": "#ffffff", "southpark": "#101010", "marvel": "#fff2d6"}
    def ui_asset(name):
        return "gui/worlds/{}/{}.png".format(ui_world if ui_world in UI_COLORS else "storybook", name)
    def ui_ink():
        return UI_COLORS.get(ui_world, "#713047")

screen say(who, what):
    window:
        id "window"
        xpos dialogue_box()[0] ypos dialogue_box()[1] xsize dialogue_box()[2] ysize dialogue_box()[3]
        background themed_frame("dialogue", 50, 24)
        padding ((60 if ui_world == "southpark" else 100), 12, (40 if ui_world == "southpark" else 130), 12)
        text what:
            id "what"
            color ui_ink()
            font theme_font("body")
            size theme_size("body")
            line_spacing 6
    if who is not None:
        frame:
            xpos 120 ypos (dialogue_box()[1] - 58) xsize 560 ysize 76
            background themed_frame("name", 40, 15)
            padding (40, 12)
            text who:
                id "who"
                color ("#fff2d6" if ui_world in ("storybook", "sims", "marvel") else ui_ink())
                font theme_font("label")
                size theme_size("label")
                yalign 0.5
    add ui_asset("next") xpos (dialogue_box()[0] + dialogue_box()[2] - 90) ypos 966
    use quick_menu

screen lower_backdrop():
    add ui_asset("dialogue") id "choice_backdrop" xpos dialogue_box()[0] ypos dialogue_box()[1] xsize dialogue_box()[2] ysize dialogue_box()[3] nearest (ui_world == "minecraft")

screen choice_card(item, count):
    textbutton item.caption:
        action item.action
        xsize choice_dimensions(count)[0]
        ysize choice_dimensions(count)[1]
        padding (24, (8 if ui_world == "southpark" else 12))
        background themed_frame("choice_idle", 35, 25)
        hover_background themed_frame("choice_hover", 35, 25)
        activate_background themed_frame("choice_pressed", 35, 25)
        selected_background themed_frame("choice_selected", 35, 25)
        insensitive_background themed_frame("choice_disabled", 35, 25)
        text_color ui_ink()
        text_hover_color ("#ffffff" if ui_world == "storybook" else ui_ink())
        text_font theme_font("label")
        text_size choice_label_size(count)
        text_xalign 0.5
        text_yalign 0.5
        text_text_align 0.5

screen choice(items):
    use lower_backdrop
    if ui_world == "southpark":
        vbox:
            xpos 96 ypos 710 spacing 6
            for item in items:
                use choice_card(item, len(items))
    else:
        hbox:
            xalign 0.5 ypos 830 spacing 24
            for item in items:
                use choice_card(item, len(items))
    use quick_menu

screen quick_menu():
    zorder 100
    hbox:
        xalign 0.5 ypos 1024 spacing 10
        for caption, operation in [("История", ShowMenu("history")), ("Пропуск", Skip()), ("Авто", Preference("auto-forward", "toggle")), ("Сохранить", ShowMenu("save")), ("Загрузить", ShowMenu("load")), ("Настройки", ShowMenu("preferences"))]:
            textbutton caption:
                action operation
                xsize 220 ysize 48 padding (10, 6)
                background themed_frame("quick_idle", 15, 10)
                hover_background themed_frame("quick_hover", 15, 10)
                activate_background themed_frame("quick_pressed", 15, 10)
                selected_background themed_frame("quick_selected", 15, 10)
                insensitive_background themed_frame("quick_disabled", 15, 10)
                text_color ui_ink()
                text_hover_color ui_ink()
                text_selected_color ui_ink()
                text_font theme_font("label")
                text_size (20 if ui_world == "minecraft" else 25)
                text_xalign 0.5 text_yalign 0.5

screen menu_shell(title):
    tag menu
    add Solid("#101b29")
    add Transform("images/backgrounds/office_evening.png", xysize=(1920, 1080), fit="cover", alpha=0.17)
    text title xpos 100 ypos 65 size 56 color "#f3cfab"
    hbox:
        xalign 0.95 ypos 80 spacing 12
        for caption, destination in [("Сохранить", "save"), ("Загрузить", "load"), ("Настройки", "preferences"), ("Коллекция", "gallery")]:
            textbutton caption:
                action ShowMenu(destination)
                sensitive not (main_menu and destination == "save")
                text_size 24
                padding (18, 12)
    hbox:
        xpos 100 ypos 970 spacing 20
        if not main_menu:
            textbutton "Продолжить" action Return()
        textbutton "Главное меню" action (ShowMenu("main_menu") if main_menu else MainMenu())
        textbutton "Управление" action ShowMenu("help")
    transclude

screen main_menu():
    tag menu
    add "bg office_evening"
    add Solid("#111a27c9")
    vbox:
        xpos 180 ypos 130 spacing 10
        text "В порядке\nперевода" font "fonts/OlyaStorySerif-Semibold.ttf" size 80 color "#f7dfbd"
        text "Шесть миров. Одно личное желание." size 30
        null height 25
        textbutton "Новая игра" action Start() xsize 500
        textbutton "Загрузить" action ShowMenu("load") xsize 500
        textbutton "Коллекция концовок" action ShowMenu("gallery") xsize 500
        textbutton "Настройки" action ShowMenu("preferences") xsize 500
        textbutton "Управление" action ShowMenu("help") xsize 500
        textbutton "Авторы и музыка" action ShowMenu("credits") xsize 500
        textbutton "Выход" action Quit() xsize 500
    text "Личная фанатская история • Подарок Оле" xpos 180 ypos 990 size 24 color "#d5c5b9"

screen save():
    tag menu
    use file_slots("Сохранить")
screen load():
    tag menu
    use file_slots("Загрузить")
screen file_slots(title):
    use menu_shell(title):
        vbox:
            xpos 100 ypos 170 spacing 25
            hbox:
                spacing 15
                textbutton "Авто" action FilePage("auto")
                textbutton "Быстрые" action FilePage("quick")
                for page in range(1, 7):
                    textbutton str(page) action FilePage(page)
            grid 3 2:
                spacing 25
                for slot in range(1, 7):
                    button:
                        xsize 550 ysize 290
                        action FileAction(slot)
                        vbox:
                            spacing 12
                            add FileScreenshot(slot) xysize (480, 190)
                            text FileTime(slot, format="%d.%m.%Y %H:%M", empty="Пустая ячейка") size 25
                        key "save_delete" action FileDelete(slot)

screen preferences():
    tag menu
    use menu_shell("Настройки"):
        hbox:
            xpos 140 ypos 200 spacing 200
            vbox:
                xsize 650 spacing 22
                hbox:
                    spacing 20
                    textbutton "Окно" action Preference("display", "window")
                    textbutton "Полный экран" action Preference("display", "fullscreen")
                text "Скорость текста"
                bar value Preference("text speed")
                text "Задержка авто"
                bar value Preference("auto-forward time")
                textbutton "Пропускать только прочитанное" action Preference("skip", "seen")
                textbutton "Пропускать весь текст" action Preference("skip", "all")
                textbutton "Пропуск после выбора" action Preference("after choices", "toggle")
            vbox:
                spacing 26
                text "Музыка"
                bar value Preference("music volume")
                textbutton "Выключить музыку" action Preference("music mute", "toggle")
                text "Звуковые эффекты"
                bar value Preference("sound volume")
                textbutton "Выключить эффекты" action Preference("sound mute", "toggle")

screen history():
    tag menu
    use menu_shell("История"):
        viewport:
            xpos 120 ypos 170 xsize 1680 ysize 740
            mousewheel True draggable True scrollbars "vertical" yinitial 1.0
            vbox:
                spacing 26
                for entry in _history_list:
                    vbox:
                        if entry.who:
                            text entry.who color "#f3cfab" size 28
                        text entry.what size 30 substitute False
                if not _history_list:
                    text "История появится после начала разговора."

screen help():
    tag menu
    use menu_shell("Управление"):
        vbox:
            xpos 140 ypos 200 spacing 22
            text "Enter / Пробел / Щелчок — следующая реплика"
            text "Стрелки / Tab — выбор кнопки; Enter — подтвердить"
            text "Esc / Правая кнопка мыши — меню"
            text "Колесо вверх / Page Up — вернуться к предыдущей реплике"
            text "Ctrl — пропуск; H — скрыть интерфейс; F — полный экран"
            text "S — снимок экрана; кнопка «Авто» — автоматическое чтение"
            text "Перед решением остаться можно сохранить игру."
            text "Все финалы равноценны. Новая игра сохраняет коллекцию концовок." color "#f3cfab"

screen confirm(message, yes_action, no_action):
    modal True zorder 200
    add Solid("#000b")
    frame:
        align (0.5, 0.5) xsize 1100 padding (50, 45) background Solid("#172738")
        vbox:
            spacing 30
            text message text_align 0.5 xalign 0.5
            hbox:
                xalign 0.5 spacing 40
                textbutton "Да" action yes_action
                textbutton "Нет" action no_action
    key "game_menu" action no_action

screen notify(message):
    zorder 150
    frame:
        xpos 40 ypos 30 padding (25, 16) background Solid("#172738ee")
        text message size 26
    timer 3.0 action Hide("notify")
screen skip_indicator():
    zorder 150
    text "Пропуск…" xpos 40 ypos 30 size 25

screen ending_result(ending):
    modal True
    add Solid("#101b29e9")
    vbox:
        align (0.5, 0.5) spacing 25
        text "[dict(ENDINGS).get(ending, 'Финал')]" size 60 color "#f3cfab" xalign 0.5
        text "Эта история остается с тобой." xalign 0.5
        textbutton "Главное меню" action MainMenu(confirm=False) xsize 650
        textbutton "Загрузить сохранение" action ShowMenu("load") xsize 650
        textbutton "Коллекция концовок" action ShowMenu("gallery") xsize 650


screen credits():
    tag menu
    use menu_shell("Авторы и музыка"):
        viewport:
            xpos 140 ypos 180 xsize 1640 ysize 700
            mousewheel True draggable True scrollbars "vertical"
            vbox:
                spacing 28
                text "В порядке перевода — персональная фанатская история для Оли." size 40 color "#f3cfab"
                text "Музыка обычного мира" size 36
                text MUSIC_CREDITS size 30 substitute False
                text "Шрифты: Alegreya Sans, Lora, Rubik, Comfortaa, Press Start 2P, Neucha, Russo One. Лицензии OFL включены в комплект." size 30
                text "Исходные миры и персонажи принадлежат их правообладателям. В игре используются стилизованные изображения, включая сгенерированную стилизацию The Sims." size 30
