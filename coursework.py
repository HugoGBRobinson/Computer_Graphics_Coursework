import pygame

# import the scene class
from cubeMap import FlattenCubeMap
from scene import Scene

from lightSource import LightSource

from blender import load_obj_file

from ShadowMapping import *

from skyBox import *

from environmentMapping import *

import math

from sphereModel import Sphere

class StreetScene(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.light = LightSource(self, position=[5, 5, 5])

        self.shaders = 'phong'

        self.shadows = ShadowMap(light=self.light)
        self.show_shadow_map = ShowTexture(self, self.shadows)

        self.skybox = SkyBox(scene=self)

        self.show_light = DrawModelFromMesh(scene=self, M=poseMatrix(position=self.light.position, scale=0.2),
                                            mesh=Sphere(material=Material(Ka=[10, 10, 10])), shader=PhongShader())

        self.environment = EnvironmentMappingTexture(width=400, height=400)

        self.envbox = EnvironmentBox(scene=self)

        meshes = (load_obj_file('models/bunny_world.obj'))
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([-1.9, 0, 3], [0.1, 0.1, 0.1], 0, 180 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows))for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([1.9, 0, 6.5], [0.1, 0.1, 0.1], 0, 0, 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows))for mesh in meshes])
        meshes = load_obj_file('models/Street_Light.obj')
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([-2, 0, -2], [0.1, 0.1, 0.1], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows))for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([-2, 0, -6], [0.1, 0.1, 0.1], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows))for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([2, 0, -2], [0.1, 0.1, 0.1], 0, 270 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows))for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([2, 0, -6], [0.1, 0.1, 0.1], 0, 270 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows))for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([-2, 0, 6], [0.1, 0.1, 0.1], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows))for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([-2, 0, 2], [0.1, 0.1, 0.1], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows))for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([2, 0, 2], [0.1, 0.1, 0.1], 0, 270 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows))for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([2, 0, 6], [0.1, 0.1, 0.1], 0, 270 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows))for mesh in meshes])
        meshes = load_obj_file('models/house.obj')
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([-4, 0, 2], [0.2, 0.2, 0.2], 0, 0 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows)) for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([-4, 0, -4], [0.2, 0.2, 0.2], 0, 0 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows)) for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([4, 0, 2], [0.2, 0.2, 0.2], 0, 180 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows)) for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([4, 0, -4], [0.2, 0.2, 0.2], 0, 180 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows)) for mesh in meshes])

        meshes = load_obj_file('models/tree.obj')
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([-3, 0, 4], [0.1, 0.1, 0.1], 0, 0 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows)) for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([3, 0, 4], [0.1, 0.1, 0.1], 0, 0 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows)) for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([-3, 0, 0], [0.1, 0.1, 0.1], 0, 0 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows)) for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([-3, 0, -4], [0.1, 0.1, 0.1], 0, 0 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows)) for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([3, 0, 0], [0.1, 0.1, 0.1], 0, 180 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows)) for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([3, 0, -4], [0.1, 0.1, 0.1], 0, 180 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows)) for mesh in meshes])

        meshes = load_obj_file('models/floor.obj')
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([0, -0.18, 0], [1, 1, 1], 0, 0, 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows)) for mesh in meshes])

        meshes = load_obj_file('models/road.obj')
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([0, -0.11, 0], [0.2, 0.2, 0.2], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows))for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([0, -0.11, -7], [0.2, 0.2, 0.2], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows))for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([0, -0.11, -14], [0.2, 0.2, 0.2], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows))for mesh in meshes])

        meshes = load_obj_file('models/road_lines.obj')
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([0, -0.1, 8], [0.1, 0.1, 0.1], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=PhongShader())for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([0, -0.1, 4], [0.1, 0.1, 0.1], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=PhongShader())for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([0, -0.1, 0], [0.1, 0.1, 0.1], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=PhongShader())for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([0,-0.1, -4], [0.1, 0.1, 0.1], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=PhongShader())for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([0, -0.1, -8], [0.1, 0.1, 0.1], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=PhongShader())for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([0, -0.1, -12], [0.1, 0.1, 0.1], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=PhongShader())for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([0, -0.1, -16], [0.1, 0.1, 0.1], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=PhongShader())for mesh in meshes])

        meshes = load_obj_file('models/pavement.obj')
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([-2, -0.1, 8], [1, 0.2, 0.3], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=PhongShader())for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([2, -0.1, 8], [1, 0.2, 0.3], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=PhongShader())for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([-2, -0.1, 0], [1, 0.2, 0.3], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=PhongShader())for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([2, -0.1, 0], [1, 0.2, 0.3], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=PhongShader())for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([-2, -0.1, -8], [1, 0.2, 0.3], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=PhongShader())for mesh in meshes])
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([2, -0.1, -8], [1, 0.2, 0.3], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=PhongShader())for mesh in meshes])

        meshes = load_obj_file('models/bin.obj')
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([-2, -0.1, -2.5], [0.1, 0.1, 0.1], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=EnvironmentShader(map=self.environment))for mesh in meshes])

        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=poseMatrix([2, -0.1, 5], [0.1, 0.1, 0.1], 0, 90 * (math.pi / 180), 0),
                               mesh=mesh, shader=EnvironmentShader(map=self.environment))for mesh in meshes])

        self.flattened_cube = FlattenCubeMap(scene=self, cube=self.environment)

        self.show_texture = ShowTexture(self, Texture('stone.bmp'))

    def draw_shadow_map(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for model in self.models:
            model.draw()

    def draw_reflections(self):
        self.skybox.draw()

        for model in self.models:
            model.draw()

    def draw(self, framebuffer=False):
        '''
        Draw all models in the scene
        :return: None
        '''

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if not framebuffer:
            self.camera.update()

        self.skybox.draw()

        self.shadows.render(self)

        if not framebuffer:

            self.environment.update(self)

            self.flattened_cube.draw()

            self.show_texture.draw()

            self.show_shadow_map.draw()

        for model in self.models:
            model.draw()

        self.show_light.draw()

        if not framebuffer:
            pygame.display.flip()


if __name__ == '__main__':
    scene = StreetScene()

    scene.run()
