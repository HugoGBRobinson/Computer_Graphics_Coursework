#version 130


in vec3 position;
in vec3 normal;
in vec3 tangent;
in vec3 binormal;
in vec3 color;
in vec2 texCoord;


out vec2 fragment_texCoord;
out vec3 view_normal;
out vec3 view_tangent;
out vec3 view_binormal;


uniform mat4 PVM;
uniform mat3 VMiT;

void main(){
    gl_Position = PVM * vec4(position, 1.0f);

    fragment_texCoord = texCoord;
}
