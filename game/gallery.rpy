screen return_worlds():
    modal True
    add Solid("#101b29ed")
    vbox:
        align (0.5, 0.5) spacing 18
        text "Куда ты хочешь вернуться?" size 48 color "#f3cfab"
        for world in WORLDS:
            if world in visited_worlds:
                textbutton WORLD_NAMES[world] action Return(world) xsize 900

screen gallery():
    tag menu
    use menu_shell("Коллекция концовок"):
        vbox:
            xpos 140 ypos 170 spacing 15
            text "[len(persistent.unlocked_endings)] из 8 историй открыто" color "#f3cfab"
            for ending_id, title in ENDINGS:
                textbutton (title if ending_id in persistent.unlocked_endings else "Пока не открыто"):
                    action Replay("gallery_ending", scope={"current_ending": ending_id}, locked=False)
                    sensitive ending_id in persistent.unlocked_endings
                    xsize 1000
        text "Повтор не меняет текущее прохождение.\nНовая игра сохраняет коллекцию." xpos 1240 ypos 250 xsize 530 size 28

label gallery_ending:
    $ gallery_mode = True
    call ending_scene
    $ renpy.end_replay()
    return
