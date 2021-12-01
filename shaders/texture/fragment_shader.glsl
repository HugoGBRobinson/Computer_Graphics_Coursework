# version 130

in vec2 fragment_texCoord;

out vec4 final_color;

uniform sampler2D textureObject;

void main() {

    vec4 texval = vec4(1.0f);

    texval = texture2D(textureObject, fragment_texCoord);

    final_color = texval;
}


