[app]

title = Tetris
package.name = tetrisgame
package.domain = org.tetris

source.dir =.
source.include_exts = py,png,jpg,jpeg,kv,atlas
source.include_patterns = 
source.exclude_exts = spec
source.exclude_dirs =.buildozer,.git
source.include_files =
source.main = main.py

version = 1.0.0
requirements = python3, kivy, pygame==2.5.2, sdl2, sdl2_image, sdl2_mixer, sdl2_ttf

orientation = landscape
fullscreen = 1
icon.filename = icon.png
presplash.filename = %(source.dir)s/data/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 23
android.sdk_path =
android.ndk_path =
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = False
android.accept_sdk_license = True
android.logcat_filters = *:S python:D
android.permissions =
android.manifest.intent_filters =
android.extra_manifest_application_arguments =
android.extra_manifest_activity_arguments =
android.gradle_dependencies =