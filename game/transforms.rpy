# A fixed eye anchor is shared by dialogue, choices and panel-free scenes.
# The transparent canvas extends below the viewport; actual silhouette cuts do too.
transform left_actor:
    xpos 0.30
    xanchor 0.5
    ypos 0
    yanchor 0.0
    zoom 1.0
transform right_actor:
    xpos (0.76 if ui_world == "southpark" else 0.72)
    xanchor 0.5
    ypos 0
    yanchor 0.0
    zoom 1.0
transform center_actor:
    xpos 0.5
    xanchor 0.5
    ypos 0
    yanchor 0.0
    zoom 1.0
