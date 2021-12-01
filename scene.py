# pygame is just used to create a window with the operating system on which to draw.
import pygame

# imports all openGL functions
from OpenGL.GL import *

# import the shader class
from shaders import *

# import the camera class
from camera import Camera

# and we import a bunch of helper functions
from matutils import *

from lightSource import LightSource

class Scene:
    '''
    This is the main class for adrawing an OpenGL scene using the PyGame library
    '''
    def __init__(self, width=800, height=600, shaders=None):
        '''
        Initialises the scene
        '''

        self.window_size = (width, height)

        self.wireframe = False

        pygame.init()
        screen = pygame.display.set_mode(self.window_size, pygame.OPENGL | pygame.DOUBLEBUF, 24)

        glViewport(0, 0, self.window_size[0], self.window_size[1])

        glClearColor(0.7, 0.7, 1.0, 1.0)

        glEnable(GL_CULL_FACE)

        glEnableClientState(GL_VERTEX_ARRAY)

        glEnable(GL_DEPTH_TEST)

        self.shaders = 'flat'

        near = 1.0
        far = 20.0
        left = -1.0
        right = 1.0
        top = -1.0
        bottom = 1.0

        self.show_model = -1

        self.P = frustumMatrix(left, right, top, bottom, near, far)

        self.camera = Camera()

        self.light = LightSource(self, position=[5., 5., 5.])

        self.mode = 1

        self.models = []

    def add_model(self, model):
        '''
        This method just adds a model to the scene.
        :param model: The model object to add to the scene
        :return: None
        '''

        self.models.append(model)

    def add_models_list(self, models_list):
        '''
        This method just adds a model to the scene.
        :param model: The model object to add to the scene
        :return: None
        '''
        for model in models_list:
            self.add_model(model)

    def draw(self, framebuffer=False):
        '''
        Draw all models in the scene
        :return: None
        '''

        if not framebuffer:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            self.camera.update()

        for model in self.models:
            model.draw()

        if not framebuffer:
            pygame.display.flip()

    def keyboard(self, event):
        '''
        Method to process keyboard events. Check Pygame documentation for a list of key events
        :param event: the event object that was raised
        '''
        if event.key == pygame.K_q:
            self.running = False

        elif event.key == pygame.K_0:
            if self.wireframe:
                print('--> Rendering using colour fill')
                glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
                self.wireframe = False
            else:
                print('--> Rendering using colour wireframe')
                glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
                self.wireframe = True

    def pygameEvents(self):
        '''
        Method to handle PyGame events for user interaction.
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                self.keyboard(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mods = pygame.key.get_mods()
                if event.button == 4:
                    if mods & pygame.KMOD_CTRL:
                        self.light.position *= 1.1
                        self.light.update()
                    else:
                        self.camera.distance = max(1, self.camera.distance - 1)

                elif event.button == 5:
                    if mods & pygame.KMOD_CTRL:
                        self.light.position *= 0.9
                        self.light.update()
                    else:
                        self.camera.distance += 1

            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    if self.mouse_mvt is not None:
                        self.mouse_mvt = pygame.mouse.get_rel()
                        self.camera.center[0] -= (float(self.mouse_mvt[0]) / self.window_size[0])
                        self.camera.center[1] -= (float(self.mouse_mvt[1]) / self.window_size[1])
                    else:
                        self.mouse_mvt = pygame.mouse.get_rel()

                elif pygame.mouse.get_pressed()[2]:
                    if self.mouse_mvt is not None:
                        self.mouse_mvt = pygame.mouse.get_rel()
                        self.camera.phi -= (float(self.mouse_mvt[0]) / self.window_size[0])
                        self.camera.psi -= (float(self.mouse_mvt[1]) / self.window_size[1])
                    else:
                        self.mouse_mvt = pygame.mouse.get_rel()
                else:
                    self.mouse_mvt = None

    def run(self):
        '''
        Draws the scene in a loop until exit.
        '''

        self.running = True
        while self.running:

            self.pygameEvents()

            self.draw()