[app]

title = Tetris
package.name = tetrisgame
package.domain = org.tetris
source.dir =.
source.include_exts = py,png,jpg,jpeg
source.main = main.py

version = 1.0.0
requirements = python3, kivy, pygame==2.5.2, sdl2, sdl2_image, sdl2_mixer, sdl2_ttf
android.archs = arm64-v8a, armeabi-v7a
android.api = 33
android.minapi = 23
android.sdk_path = 
android.ndk_path = 
android.ant_path = 

orientation = landscape
fullscreen = 1
icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.allow_backup = False
android.accept_sdk_license = True
android.add_jars = 
android.add_src = 
android.add_java = 
android.add_aars = 
android.add_gradle_dependencies = 
android.meta_data = 
android.permissions = 
android.api = 33
android.minapi = 23
android.sdk_path = 
android.ndk_path = 
android.ant_path = 
android.archs = arm64-v8a, armeabi-v7a