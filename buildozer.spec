[app]

title = Tetris
package.name = tetrisgame
package.domain = tetris.game

source.dir =.
source.include_exts = py,png
source.main = main.py

version = 1.0
requirements = python3,pygame,sdl2

orientation = landscape
fullscreen = 1
icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.logcat_filters = *:S python:D
android.allow_backup = False
android.accept_sdk_license = True