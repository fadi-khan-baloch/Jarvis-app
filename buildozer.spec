[app]
title = JARVIS
package.name = jarvisapp
package.domain = com.fadi.jarvis
source.dir =.
source.include_exts = py
version = 0.1
requirements = python3,kivy,plyer
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.permissions = CAMERA,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
