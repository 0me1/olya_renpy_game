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
