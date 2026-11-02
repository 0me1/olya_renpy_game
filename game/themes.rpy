# Saved ui_world chooses every in-game font. Menus keep the storybook styles.
init -1 python:
    THEMES = {
        "storybook": {"body": "fonts/AlegreyaSans-Regular.ttf", "label": "fonts/OlyaStorySerif-Semibold.ttf", "body_size": 40, "label_size": 36},
        "sims": {"body": "fonts/OlyaGameSans-Regular.ttf", "label": "fonts/OlyaRounded-Bold.ttf", "body_size": 38, "label_size": 34},
        "minecraft": {"body": "fonts/PressStart2P-Regular.ttf", "label": "fonts/PressStart2P-Regular.ttf", "body_size": 28, "label_size": 28},
        "southpark": {"body": "fonts/Neucha-Regular.ttf", "label": "fonts/Neucha-Regular.ttf", "body_size": 42, "label_size": 40},
        "marvel": {"body": "fonts/OlyaGameSans-Regular.ttf", "label": "fonts/RussoOne-Regular.ttf", "body_size": 38, "label_size": 34},
    }
    def theme_spec(world=None):
        return THEMES.get(world or store.ui_world, THEMES["storybook"])
    def theme_font(role):
        return theme_spec()[role]
    def theme_size(role):
        return theme_spec()[role + "_size"]
    def themed_frame(name, left, top):
        return Transform(Frame(ui_asset(name), left, top), nearest=(store.ui_world == "minecraft"))
