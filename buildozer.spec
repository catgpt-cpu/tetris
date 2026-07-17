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
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653
android.build_tools_version = 31.0.0
android.ndk = 25b
android.arch = arm64-v8a
android.permissions = INTERNET
android.wakelock = False

# Build
p4a.branch = master
log_level = 2