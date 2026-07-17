[app]
title = Tetris
package.name = tetrisgame
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,pygame==2.5.2,sdl2
orientation = landscape
fullscreen = 1

[buildozer]
android.api = 31
android.minapi = 21
android.arch = arm64-v8a, armeabi-v7a
android.logcat_filters = *:S python:D