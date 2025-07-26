bl_info = {
    "name": "Sculpt Mode Scale Warning 1.2",
    "author": "Luga3D + ChatGPT",
    "version": (1, 2),
    "blender": (4, 5, 0),
    "description": "Changes the viewport background if you enter sculpt mode with scale not applied.",
    "category": "3D View"
}

import bpy
from bpy.app.handlers import persistent

DEFAULT_BG_COLOR = (0.01, 0.01, 0.01)  # Default viewport background color
WARNING_BG_COLOR = (1.0, 0.1, 0.1)     # Color for warning

def is_scale_applied(obj):
    return all(abs(s - 1.0) < 1e-4 for s in obj.scale)

def change_viewport_bg(color):
    for area in bpy.context.window.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.shading.background_color = color

@persistent
def sculpt_mode_checker(scene):
    obj = bpy.context.active_object
    mode = bpy.context.mode

    if obj and obj.type == 'MESH':
        if mode == 'SCULPT':
            if not is_scale_applied(obj):
                change_viewport_bg(WARNING_BG_COLOR)
            else:
                change_viewport_bg(DEFAULT_BG_COLOR)
        else:
            change_viewport_bg(DEFAULT_BG_COLOR)
            
	# Force background for ‘VIEWPORT’ (Custom)
    for area in bpy.context.window.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    if space.shading.background_type != 'VIEWPORT':
                        space.shading.background_type = 'VIEWPORT'

classes = []

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.app.handlers.depsgraph_update_post.append(sculpt_mode_checker)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    if sculpt_mode_checker in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(sculpt_mode_checker)

if __name__ == "__main__":
    register()

