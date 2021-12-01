#version 130

in vec3 normal_view_space;
in vec3 position_view_space;
in vec3 fragment_texCoord;
out vec4 final_color;

uniform samplerCube sampler_cube;
uniform mat4 PVM;
uniform mat4 VM;
uniform mat3 VMiT;
uniform mat3 VT;

void main(void)
{
	vec3 normal_view_space_normalized = normalize(normal_view_space);
	vec3 reflected = reflect(normalize(-position_view_space), normal_view_space_normalized);

	final_color = texture(sampler_cube, normalize(VT*reflected));


}
