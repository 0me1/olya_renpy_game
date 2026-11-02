init python:
    UI_COLORS = {"storybook": "#713047", "sims": "#10265f", "minecraft": "#ffffff", "southpark": "#101010", "marvel": "#fff2d6"}
    def ui_asset(name):
        return "gui/worlds/{}/{}.png".format(ui_world if ui_world in UI_COLORS else "storybook", name)
    def ui_ink():
        return UI_COLORS.get(ui_world, "#713047")

screen say(who, what):
    window:
        id "window"
        xpos 80 ypos 740 xsize 1760 ysize 280
        background ui_asset("dialogue")
        padding (100, 36, 130, 24)
        text what:
            id "what"
            color ui_ink()
            size 34
            line_spacing 6
    if who is not None:
        frame:
            xpos 120 ypos 682 xsize 450 ysize 76
            background Frame(ui_asset("name"), 40, 15)
            padding (40, 12)
            text who:
                id "who"
                color ("#fff2d6" if ui_world in ("storybook", "sims", "marvel") else ui_ink())
                size 31
                yalign 0.5
    add ui_asset("next") xpos 1750 ypos 954
    use quick_menu

screen choice(items):
    vbox:
        xalign 0.5 yalign 0.42 spacing 18
        for item in items:
            textbutton item.caption:
                action item.action
                xsize 1160
                yminimum 104
                padding (60, 20)
                background Frame(ui_asset("choice_idle"), 35, 25)
                hover_background Frame(ui_asset("choice_hover"), 35, 25)
                insensitive_background Frame(ui_asset("choice_disabled"), 35, 25)
                text_color ui_ink()
                text_hover_color ("#ffffff" if ui_world == "storybook" else ui_ink())
                text_size 30
                text_xalign 0.5
                text_text_align 0.5
    use quick_menu

screen quick_menu():
    zorder 100
    hbox:
        xalign 0.5 ypos 1024 spacing 10
        for caption, operation in [("История", ShowMenu("history")), ("Пропуск", Skip()), ("Авто", Preference("auto-forward", "toggle")), ("Сохранить", ShowMenu("save")), ("Загрузить", ShowMenu("load")), ("Настройки", ShowMenu("preferences"))]:
            textbutton caption:
                action operation
                xsize 220 ysize 48 padding (10, 6)
                background Frame(ui_asset("quick_idle"), 15, 10)
                hover_background Frame(ui_asset("quick_hover"), 15, 10)
                selected_background Frame(ui_asset("quick_selected"), 15, 10)
                insensitive_background Frame(ui_asset("quick_disabled"), 15, 10)
                text_color ui_ink()
                text_hover_color ui_ink()
                text_selected_color ui_ink()
                text_size 23
                text_xalign 0.5 text_yalign 0.5

screen menu_shell(title):
    tag menu
    add Solid("#101b29")
    add Transform("images/backgrounds/office_evening.png", xysize=(1920, 1080), fit="cover", alpha=0.17)
    text title xpos 100 ypos 65 size 56 color "#f3cfab"
    hbox:
        xpos 100 ypos 970 spacing 20
        if not main_menu:
            textbutton "Продолжить" action Return()
        textbutton "Главное меню" action MainMenu()
        textbutton "Управление" action ShowMenu("help")
    transclude

screen main_menu():
    tag menu
    add "bg office_evening"
    add Solid("#111a27c9")
    vbox:
        xpos 180 ypos 190 spacing 16
        text "В порядке\nперевода" size 90 color "#f7dfbd"
        text "Шесть миров. Одно личное желание." size 30
        null height 25
        textbutton "Новая игра" action Start() xsize 500
        textbutton "Загрузить" action ShowMenu("load") xsize 500
        textbutton "Коллекция концовок" action ShowMenu("gallery") xsize 500
        textbutton "Настройки" action ShowMenu("preferences") xsize 500
        textbutton "Управление" action ShowMenu("help") xsize 500
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
        vbox:
            xpos 140 ypos 200 spacing 28
            hbox:
                spacing 20
                textbutton "Окно" action Preference("display", "window")
                textbutton "Полный экран" action Preference("display", "fullscreen")
            text "Скорость текста"
            bar value Preference("text speed")
            text "Задержка авто"
            bar value Preference("auto-forward time")
            text "Громкость"
            bar value Preference("sound volume")
            textbutton "Пропускать только прочитанное" action Preference("skip", "seen")
            textbutton "Пропускать весь текст" action Preference("skip", "all")
            textbutton "Пропуск после выбора" action Preference("after choices", "toggle")

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
