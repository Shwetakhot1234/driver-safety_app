[app]

title = Driver Safety App
package.name = driversafety
package.domain = org.shweta

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,tflite,task,onnx,json,txt
source.include_patterns = assets/*,images/*,*.py,*.kv,*.png,*.jpg,*.jpeg,*.task,*.tflite,*.onnx,*.json

version = 1.0

requirements = python3,kivy==2.2.1,numpy,pillow,plyer

orientation = portrait
fullscreen = 0

android.permissions = CAMERA,INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,RECORD_AUDIO,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 34
android.minapi = 24
android.ndk = 28c
android.archs = arm64-v8a

android.accept_sdk_license = True
android.enable_androidx = True
android.gradle_dependencies =

p4a.branch = master

[buildozer]

log_level = 2
warn_on_root = 1
