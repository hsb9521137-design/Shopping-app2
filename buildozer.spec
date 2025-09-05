[app]
# App ka title
title = Shopping App

# APK banne ke baad jo package name hoga
package.name = shoppingapp
package.domain = org.hsb

# APK ka version
version = 1.0.0

# APK ke andar chalne wali python file
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Main file jo run hogi
main.py = main.py

# App icon (optional, abhi hata diya hai)
# icon.filename = %(source.dir)s/data/icon.png

# Permissions
android.permissions = INTERNET

# Minimum Android version
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# Orientation
orientation = portrait

# Python aur Kivy requirement
requirements = python3,kivy

# APK ka output name
android.archs = armeabi-v7a, arm64-v8a
android.entrypoint = org.kivy.android.PythonActivity
android.release_artifact = apk

# Log level
log_level = 2

# Window settings
fullscreen = 0

[buildozer]
# Spec file ka version
log_level = 2
warn_on_root = 1
