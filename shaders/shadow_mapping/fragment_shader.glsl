# version 130

in vec3 fragment_color;
in vec3 position_view_space;
in vec3 normal_view_space;
in vec2 fragment_texCoord;


out vec4 final_color;


uniform int mode;
uniform int has_texture;
uniform sampler2D textureObject;
uniform sampler2DShadow shadow_map;

uniform mat4 shadow_map_matrix;

uniform vec3 Ka;
uniform vec3 Kd;
uniform vec3 Ks;
uniform float Ns;


uniform vec3 light;
uniform vec3 Ia;
uniform vec3 Id;
uniform vec3 Is;

uniform float alpha = 1.0f;


vec4 phong(vec4 texval);

vec4 phong(vec4 texval) {
    vec3 camera_direction = -normalize(position_view_space);
    vec3 light_direction = normalize(light-position_view_space);

    vec4 ambient = vec4(Ia*Ka,alpha);
    vec4 diffuse = vec4(Id*Kd*max(0.0f,dot(light_direction, normal_view_space)), alpha);
    vec4 specular = vec4(Is*Ks*pow(max(0.0f, dot(reflect(light_direction, normal_view_space), -camera_direction)), Ns), alpha);

    float dist = length(light - position_view_space);
    float attenuation =  min(1.0/(dist*dist*0.005) + 1.0/(dist*0.05), 1.0);

    return texval*ambient + attenuation*(texval*diffuse + specular);
}

void main() {

    vec4 texval = vec4(1.0f);
    if(has_texture == 1)
        texval = texture2D(textureObject, fragment_texCoord);

    final_color = vec4(0.0f);

    final_color = phong(texval);

    vec4 p = shadow_map_matrix*vec4(position_view_space, 1);


	if (p.w > 0)
	{
		p.xyz /= p.w;


		p.z *= 0.999;


		float val = texture(shadow_map, p.xyz);
        final_color.xyz = (1.0-val)*Ka*Ia*texval.xyz + val*final_color.xyz;
	}

}


