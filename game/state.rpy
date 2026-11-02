default current_world = "office"
default ui_world = "storybook"
default visited_worlds = []
default chapter_choices = {}
default discovered_clues = []
default current_ending = None
default gallery_mode = False
default persistent.unlocked_endings = []

init python:
    WORLDS = ("housewives", "manhattan", "southpark", "minecraft", "sims", "marvel")
    WORLD_NAMES = {"housewives": "Вистерия-Лейн", "manhattan": "Манхэттен", "southpark": "South Park", "minecraft": "Minecraft", "sims": "The Sims", "marvel": "Marvel", "office": "Домой"}
    ENDINGS = [("stay_" + w, WORLD_NAMES[w]) for w in WORLDS] + [("home", "С днем рождения!"), ("open_door", "Дверь остается")]
    def enter_world(world):
        store.current_world = world
        store.ui_world = world if world in ("southpark", "minecraft", "sims", "marvel") else "storybook"
        if world in WORLDS and world not in store.visited_worlds:
            store.visited_worlds.append(world)
    def choose(chapter, key, value):
        store.chapter_choices.setdefault(chapter, {})[key] = value
    def clue(text):
        if text not in store.discovered_clues:
            store.discovered_clues.append(text)
    def unlock_ending(ending):
        if ending not in persistent.unlocked_endings:
            persistent.unlocked_endings.append(ending)
            renpy.save_persistent()
    def ending_choice(world, key, fallback=None):
        return store.chapter_choices.get(world, {}).get(key, fallback)
    def bonus_available():
        return all(w in store.visited_worlds for w in WORLDS) and "home" in persistent.unlocked_endings
