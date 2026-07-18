[app]
title = Tetris
package.name = tetris
package.domain = org.example
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,pygame
orientation = portrait
icon.filename = icon.png
fullscreen = 0

# Android
android.api = 31
android.minapi = 21
android.ndk_path = /home/runner/android-sdk/ndk/28.0.13025108
android.build_tools_version = 31.0.0
android.arch = arm64-v8a
android.permissions = INTERNET

# Build
p4a.branch = master
log_level = 2