[app]
title = Tetris
package.name = tetris
package.domain = org.tetris
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,pygame
orientation = portrait
fullscreen = 1
icon.filename = icon.png

[android]
android.api = 31
android.minapi = 21
android.arch = arm64-v8a,armeabi-v7a
android.build_tools_version = 31.0.0
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653
android.ndk = 25b
android.permissions = INTERNET

[buildozer]
log_level = 2