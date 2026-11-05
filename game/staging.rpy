init python:
    CAST_TAGS = ("susan", "bree", "gabrielle", "carrie", "miranda", "cartman", "kyle", "randy", "villager", "bella", "strange", "wong")
    def cast_pose(character, pose):
        image = character + " " + pose
        if not renpy.has_image(image, exact=True):
            raise ValueError("Missing supplied pose: " + image)
        for tag in CAST_TAGS:
            if tag != character:
                renpy.hide(tag)
        renpy.show(image, at_list=[right_actor])


    def restore_sprite_framing():
        # Older saves may hold xalign/ypos/zoom from the former short canvases.
        # Rebind display transforms only; never change plot, theme or audio.
        for tag in ("olya",) + CAST_TAGS:
            if not renpy.showing(tag):
                continue
            attributes = renpy.get_attributes(tag)
            if tag == "olya":
                position = center_actor if current_world == "office" and not renpy.showing("bg birthday_home") else left_actor
            else:
                position = right_actor
            renpy.show(" ".join((tag,) + attributes), at_list=[position])

label after_load:
    $ restore_sprite_framing()
    $ renpy.block_rollback()
    return
