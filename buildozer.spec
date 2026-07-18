[app]
title = Tetris
package.name = tetris
package.domain = org.tetris
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,pygame
orientation = portrait
icon.filename = icon.png
fullscreen = 1

# Android
android.api = 31
android.minapi = 21
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653
android.ndk = 25b
android.build_tools_version = 31.0.0
android.arch = arm64-v8a,armeabi-v7a
android.permissions = INTERNET

# Build
p4a.branch = master
log_level = 2