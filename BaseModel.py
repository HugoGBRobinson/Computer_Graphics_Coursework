# imports all openGL functions
from OpenGL.GL import *

# and we import a bunch of helper functions
from matutils import *

from material import Material

from mesh import Mesh

from shaders import *
from texture import Texture

import sys


class BaseModel:
    '''
    Base class for all models, implementing the basic draw function for triangular meshes.
    Inherit from this to create new models.
    '''

    def __init__(self, scene, M=poseMatrix(), mesh=Mesh(), color=[1., 1., 1.], primitive=GL_TRIANGLES, visible=True):
        '''
        Initialises the model data
        '''

        print('+ Initializing {}'.format(self.__class__.__name__))

        self.visible = visible

        self.scene = scene

        self.primitive = primitive

        self.color = color

        self.shader = None

        self.mesh = mesh
        if self.mesh.textures == 1:
            self.mesh.textures.append(Texture('stone.bmp'))

        self.name = self.mesh.name

        self.vbos = {}

        self.attributes = {}

        self.M = M

        self.vao = glGenVertexArrays(1)

        self.index_buffer = None

    def initialise_vbo(self, name, data):
        print('Initialising VBO for attribute {}'.format(name))

        if data is None:
            print('(W) Warning in {}.bind_attribute(): Data array for attribute {} is None!'.format(
                self.__class__.__name__, name))
            return

        self.attributes[name] = len(self.vbos)

        self.vbos[name] = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbos[name])

        glEnableVertexAttribArray(self.attributes[name])

        glVertexAttribPointer(index=self.attributes[name], size=data.shape[1], type=GL_FLOAT, normalized=False,
                              stride=0, pointer=None)

        glBufferData(GL_ARRAY_BUFFER, data, GL_STATIC_DRAW)

    def bind_shader(self, shader):
        '''
        If a new shader is bound, we need to re-link it to ensure attributes are correctly linked.  
        '''
        if self.shader is None or self.shader.name is not shader:
            if isinstance(shader, str):
                self.shader = PhongShader(shader)
            else:
                self.shader = shader

            self.shader.compile(self.attributes)

    def bind(self):
        '''
        This method stores the vertex data in a Vertex Buffer Object (VBO) that can be uploaded
        to the GPU at render time.
        '''

        glBindVertexArray(self.vao)

        if self.mesh.vertices is None:
            print('(W) Warning in {}.bind(): No vertex array!'.format(self.__class__.__name__))

        self.initialise_vbo('position', self.mesh.vertices)
        self.initialise_vbo('normal', self.mesh.normals)
        self.initialise_vbo('color', self.mesh.colors)
        self.initialise_vbo('texCoord', self.mesh.textureCoords)
        self.initialise_vbo('tangent', self.mesh.tangents)
        self.initialise_vbo('binormal', self.mesh.binormals)

        if self.mesh.faces is not None:
            self.index_buffer = glGenBuffers(1)
            glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.index_buffer)
            glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.mesh.faces, GL_STATIC_DRAW)

        glBindVertexArray(0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def draw(self, Mp=poseMatrix()):
        '''
        Draws the model using OpenGL functions.
        :param Mp: The model matrix of the parent object, for composite objects.
        :param shaders: the shader program to use for drawing
        '''

        if self.visible:

            if self.mesh.vertices is None:
                print('(W) Warning in {}.draw(): No vertex array!'.format(self.__class__.__name__))

            glBindVertexArray(self.vao)

            self.shader.bind(
                model=self,
                M=np.matmul(Mp, self.M)
            )

            for unit, tex in enumerate(self.mesh.textures):
                glActiveTexture(GL_TEXTURE0 + unit)
                tex.bind()

            if self.mesh.faces is not None:
                glDrawElements(self.primitive, self.mesh.faces.flatten().shape[0], GL_UNSIGNED_INT, None )
            else:
                glDrawArrays(self.primitive, 0, self.mesh.vertices.shape[0])

            glBindVertexArray(0)

    def vbo__del__(self):
        '''
        Release all VBO objects when finished.
        '''
        for vbo in self.vbos.items():
            glDeleteBuffers(1, vbo)

        glDeleteVertexArrays(1,self.vao.tolist())


class DrawModelFromMesh(BaseModel):
    '''
    Base class for all models, inherit from this to create new models
    '''

    def __init__(self, scene, M, mesh, name=None, shader=None, visible=True):
        '''
        Initialises the model data
        '''

        BaseModel.__init__(self, scene=scene, M=M, mesh=mesh, visible=visible)

        if name is not None:
            self.name = name

        if self.mesh.faces.shape[1] == 3:
            self.primitive = GL_TRIANGLES

        elif self.mesh.faces.shape[1] == 4:
            self.primitive = GL_QUADS

        else:
            print('(E) Error in DrawModelFromObjFile.__init__(): index array must have 3 (triangles) '
                  'or 4 (quads) columns, found {}!'.format(self.indices.shape[1]))

        self.bind()

        if shader is not None:
            self.bind_shader(shader)
