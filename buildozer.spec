[app]

# (আপনার অ্যাপের নাম এবং প্যাকেজ)
title = Pro Flashlight
package.name = proflash
package.domain = org.rasel

# ১. এই লাইনটি যোগ করুন (এটি বলে দিচ্ছে যে কোড বর্তমান ফোল্ডারে আছে)
source.dir = .

# ২. এই লাইনটি যোগ করুন (এটি অ্যাপের ভার্সন)
version = 0.1

# কোন ফাইলগুলো বিল্ডে ঢুকবে
source.include_exts = py,png,jpg,kv,atlas

# প্রয়োজনীয় পারমিশন
android.permissions = CAMERA, FLASHLIGHT

# প্রয়োজনীয় লাইব্রেরি
requirements = python3,kivy,pyjnius

# অন্যান্য সেটিংস
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
