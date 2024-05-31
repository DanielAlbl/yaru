from colorz import colorz
from glob import iglob
from os import path

sccs_file = "common/accent-colors.scss.in"
options_file = "meson_options.txt"

colors = {
    path.splitext(path.basename(image))[0]: f'#{''.join('%02X' % p for p in colorz(image, n=1)[0][0])}'
    for image in iglob("/home/daniel/Pictures/Wallpapers/*.jpg")
}

with open(sccs_file, "r") as f:
    lines = f.readlines()
    scss_index = next(i for i, line in enumerate(lines) if "} @else {" in line)
with open(sccs_file, "w") as f:
    new_lines = [f"    }} @else if $accent_color == '{k}' {{\n        $color: {v};\n" for k, v in colors.items()]
    lines = lines[:scss_index] + new_lines + lines[scss_index:]
    f.write("".join(lines))

with open(options_file, "r") as f:
    lines = f.readlines()
    options_index = next(i for i, line in enumerate(lines) if "choices: [" in line) + 1
with open(options_file, "w") as f:
    new_lines = [f"        '{color}',\n" for color in colors.keys()]
    lines = lines[:options_index] + new_lines + lines[options_index:]
    f.write("".join(lines))


