#version 130

in vec3 position;

out vec3 fragment_texCoord;

uniform mat4 PVM;

void main(void)
{
	gl_Position = PVM*vec4(position, 1);
	gl_Position.z = gl_Position.w*0.9999;
	fragment_texCoord = -position;
}
