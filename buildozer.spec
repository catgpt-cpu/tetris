[app]
title = Tetris
package.name = tetrisgame
package.domain = tetris.game
source.dir =.
source.include_exts = py,png
source.main = main.py
version = 1.0
requirements = python3,pygame, sdl2, sdl2_image, sdl2_mixer, sdl2_ttf, kivy
orientation = landscape
fullscreen = 1
icon.filename = icon.png

[buildozer]
log_level = 2

[android]
android.api = 33
android.minapi = 21
android.archs = arm64-v8a