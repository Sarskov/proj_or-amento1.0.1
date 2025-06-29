[app]

title = Orcamento
package.name = orcamentov
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.0.1
requirements = python3,kivy==2.2.1,kivymd,pyjnius,cython==0.29.36
orientation = portrait
fullscreen = 1
android.permissions =
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.private_storage = true
android.use_androidx = True
android.enable_androidx_workaround = True
android.gradle_dependencies = com.android.support:appcompat-v7:28.0.0
android.gradle_properties = android.useAndroidX=true,android.enableJetifier=false
android.gradle_version = 7.0.4
android.entrypoint = org.kivy.android.PythonActivity
android.bootstrap = sdl2
android.support = false
android.logcat_filters = *:S python:D

[buildozer]

log_level = 2
warn_on_root = 1
