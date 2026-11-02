# Target virtual canvas: 1920 x 1080. Copy into your project's game folder.
default ui_world = "storybook"

init python:
    WORLD_UI_COLORS = {
        "storybook": "#713047", "sims": "#10265F",
        "minecraft": "#FFFFFF", "southpark": "#101010", "marvel": "#FFF2D6",
    }
    def world_ui_asset(filename):
        theme = ui_world if ui_world in WORLD_UI_COLORS else "storybook"
        return "gui/worlds/{}/{}.png".format(theme, filename)
    def world_ui_color():
        return WORLD_UI_COLORS.get(ui_world, "#713047")

# These replace the generated Ren'Py say and choice screens.
# Keep only ONE screen with each name in the project.
screen say(who, what):
    window:
        id "window"
        xpos 80
        ypos 740
        xsize 1760
        ysize 280
        padding (100, 42, 140, 32)
        background world_ui_asset("dialogue")
        text what:
            id "what"
            color world_ui_color()
            size 34
            line_spacing 8
    if who is not None:
        frame:
            xpos 120
            ypos 682
            xsize 320
            ysize 76
            padding (48, 12, 25, 12)
            background world_ui_asset("name")
            text who:
                id "who"
                color ("#FFF2D6" if ui_world in ("storybook", "sims", "marvel") else world_ui_color())
                size 32
                yalign 0.5
    add world_ui_asset("next") xpos 1750 ypos 952
    use world_quick_menu

screen choice(items):
    vbox:
        xalign 0.5
        yalign 0.43
        spacing 18
        for item in items:
            textbutton item.caption:
                action item.action
                xsize 860
                ysize 96
                padding (50, 14)
                background world_ui_asset("choice_idle")
                hover_background world_ui_asset("choice_hover")
                insensitive_background world_ui_asset("choice_disabled")
                text_color world_ui_color()
                text_hover_color ("#FFFFFF" if ui_world == "storybook" else world_ui_color())
                text_size 30
                text_xalign 0.5
                text_yalign 0.5
                text_text_align 0.5

screen world_quick_menu():
    hbox:
        xalign 0.5
        ypos 1024
        spacing 14
        for caption, operation in [("История", ShowMenu("history")), ("Авто", Preference("auto-forward", "toggle")), ("Сохранить", ShowMenu("save")), ("Настройки", ShowMenu("preferences"))]:
            textbutton caption:
                action operation
                xsize 190
                ysize 48
                padding (12, 6)
                background world_ui_asset("quick_idle")
                hover_background world_ui_asset("quick_hover")
                text_color world_ui_color()
                text_size 21
                text_xalign 0.5
                text_yalign 0.5
