[app]
title = Tetris Game
package.name = tetrisgame
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,pygame==2.5.2

[buildozer]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.arch = arm64-v8a