[app]
title = Tetris Game
package.name = tetrisgame
source.dir =.
source.include_exts = py,png,jpg
version = 1.0.0
requirements = python3,pygame==2.5.2,sdl2
orientation = landscape
fullscreen = 1
android.arch = arm64-v8a, armeabi-v7a
android.api = 31
android.minapi = 21
p4a.branch = develop
p4a.recipes = sdl2,pygame