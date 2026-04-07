[app]
title = Pro Flashlight
package.name = proflash
package.domain = org.rasel

# পারমিশন যা অবশ্যই লাগবে
android.permissions = CAMERA, FLASHLIGHT

# প্রয়োজনীয় লাইব্রেরি
requirements = python3,kivy,pyjnius

# অ্যান্ড্রয়েড আর্কিটেকচার
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
