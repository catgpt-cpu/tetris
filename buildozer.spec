[app]
title = Tetris
package.name = tetris
package.domain = org.test
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,pygame,sdl2
orientation = portrait
icon.filename = icon.png
android.api = 31
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a
android.permissions = INTERNET
p4a.branch = develop
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1