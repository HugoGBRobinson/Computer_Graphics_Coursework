#version 130

in vec2 fragment_texCoord;

out vec4 final_color;

uniform sampler2D sampler;

void main(void)
{

	final_color = texture(sampler, fragment_texCoord);
}
