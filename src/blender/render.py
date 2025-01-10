# This file contains a class `Renderer` that handles rendering the generated 3D models using Blender's API.

import bpy

class Renderer:
    def __init__(self, output_path):
        self.output_path = output_path

    def render(self, model_path):
        # Load the 3D model
        bpy.ops.import_scene.obj(filepath=model_path)

        # Set up the rendering settings
        bpy.context.scene.render.filepath = self.output_path
        bpy.context.scene.render.image_settings.file_format = 'PNG'

        # Render the scene
        bpy.ops.render.render(write_still=True)