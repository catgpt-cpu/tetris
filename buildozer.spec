[app]
title = Tetris Game
package.name = tetrisgame
package.domain = org.test
source.dir =.
source.include_exts = py,png,jpg
version = 1.0.0
requirements = python3,pygame==2.5.2,sdl2
orientation = landscape
fullscreen = 1
icon.filename = icon.png
android.arch = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2

android.api = 31
android.minapi = 21
android.sdk_path =.buildozer/android/platform/android-sdk
android.ndk_path =.buildozer/android/platform/android-ndk-r25b

p4a.branch = develop
p4a.recipes = sdl2,pygame