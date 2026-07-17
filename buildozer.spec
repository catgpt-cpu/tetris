[app]
title = Tetris
package.name = tetrisgame
package.domain = tetris.game
source.dir =.
source.include_exts = py,png
source.main = tetris.py
version = 1.0
requirements = python3,pygame,sdl2
orientation = landscape
fullscreen = 1
icon.filename = images.png

android.api = 33
android.archs = arm64-v8a
android.logcat_filters = *:S python:D