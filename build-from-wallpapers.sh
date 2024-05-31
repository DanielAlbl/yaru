/home/daniel/.venv/rice/bin/python3 ./config-from-wallpapers.py
meson build --prefix=$HOME/.local
meson compile -C build
meson install -C build
git restore common/accent-colors.scss.in meson_options.txt
