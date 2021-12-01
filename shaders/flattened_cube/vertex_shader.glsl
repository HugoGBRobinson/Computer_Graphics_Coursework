#version 130

in vec3 position;
in vec3 texCoord;


out vec3 fragment_texCoord;

void main(void)
{
	gl_Position = vec4(position,1);
	fragment_texCoord = texCoord;
}
