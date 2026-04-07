from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from jnius import autoclass

# Android API ক্লাসের রেফারেন্স
PythonActivity = autoclass('org.kivy.android.PythonActivity')
Context = autoclass('android.content.Context')

class FlashlightApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#121212')  # Dark Theme
        self.is_on = False
        
        # লেআউট ডিজাইন
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # টাইটেল
        self.label = Label(
            text="Flashlight: OFF",
            font_size='30sp',
            color=get_color_from_hex('#FFFFFF'),
            bold=True
        )
        
        # কন্ট্রোল বাটন
        self.btn = Button(
            text="TURN ON",
            size_hint=(None, None),
            size=('200dp', '200dp'),
            pos_hint={'center_x': 0.5},
            background_normal='',
            background_color=get_color_from_hex('#FF5252')
        )
        # বাটন গোল করার জন্য (সিম্পল ট্রিক)
        self.btn.bind(on_press=self.toggle_flashlight)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.btn)
        
        return self.layout

    def toggle_flashlight(self, instance):
        try:
            activity = PythonActivity.mActivity
            camera_manager = activity.getSystemService(Context.CAMERA_SERVICE)
            camera_id = camera_manager.getCameraIdList()[0]

            if not self.is_on:
                camera_manager.setTorchMode(camera_id, True)
                self.is_on = True
                self.btn.text = "TURN OFF"
                self.btn.background_color = get_color_from_hex('#4CAF50') # Green
                self.label.text = "Flashlight: ON"
            else:
                camera_manager.setTorchMode(camera_id, False)
                self.is_on = False
                self.btn.text = "TURN ON"
                self.btn.background_color = get_color_from_hex('#FF5252') # Red
                self.label.text = "Flashlight: OFF"
        except Exception as e:
            self.label.text = "Error: Android Only"

if __name__ == '__main__':
    FlashlightApp().run()
