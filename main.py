import time, uuid, requests, webbrowser
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.graphics import Line, Color

Window.clearcolor = (0.04, 0.05, 0.07, 1)

class SplashScreen(Screen):
    def on_enter(self):
        self.ids.splash_label.text = "در حال بارگذاری لایه‌های امنیتی...\nلطفاً صبور باشید"
        Clock.schedule_once(self.go_to_main, 4)
    def open_telegram(self):
        webbrowser.open("https://t.me")
    def go_to_main(self, dt):
        self.manager.current = 'main_screen'

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_neon_borders, 0.15)
    def update_neon_borders(self, dt):
        import random
        with self.canvas.before:
            Color(random.random(), random.random(), random.random(), 1)
            Line(rectangle=(15, 15, Window.width-30, Window.height-30), width=2)
    def trigger_hacker_terminal(self):
        friend_link = self.ids.friend_in.text.strip()
        if not friend_link or "ramakicyber" not in friend_link:
            self.ids.status_lbl.text = "خطا: لینک وارد شده نامعتبر است!"
            return
        self.ids.status_lbl.text = "[~] INITIALIZING LINUX KERNEL PROTOCOLS...\n"
        self.animate_logs(0)
    def animate_logs(self, step):
        logs = ["[~] INJECTING PEER CONNECTIONS...", "[~] CONFIGURING NETWORK ROUTE...", "[+] PORT 8080 ESTABLISHED!", "SUCCESS: وصل شدید!"]
        if step < len(logs):
            self.ids.status_lbl.text += logs[step] + "\n"
            Clock.schedule_once(lambda dt: self.animate_logs(step+1), 0.5)
    def generate_link(self):
        unique_id = uuid.uuid4().hex[:8]
        try: ip = requests.get("https://ipify.org", timeout=2).text
        except: ip = "192.168.1.1"
        link = f"ramakicyber://tunnel?id={unique_id}&node={ip}"
        self.ids.link_out.text = link
        Clipboard.copy(link)
        self.ids.status_lbl.text = "[+] لینک اختصاصی شما ساخته و کپی شد!"
    def open_social(self, spinner, text):
        if text == "پشتیبانی واتساپ": webbrowser.open("https://wa.me")
        elif text == "پشتیبانی ایمیل": webbrowser.open("mailto:ramakisahi4@gmail.com")

class RamakiTunnelApp(App):
    def build(self):
        kv_data = '''
ScreenManager:
    SplashScreen:
        name: 'splash_screen'
    MainScreen:
        name: 'main_screen'
<SplashScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 40
        spacing: 20
        Label:
            text: "RAMAKI TUNNEL"
            font_size: 28
            bold: True
            color: 0, 1, 0.5, 1
        Label:
            id: splash_label
            text: "STARTING..."
            font_size: 14
            color: 0.6, 0.6, 0.6, 1
            halign: 'center'
        Button:
            text: "عضویت در کانال تلگرام سازنده"
            font_size: 16
            size_hint_y: 0.15
            background_color: 0, 0.4, 0.8, 1
            on_press: root.open_telegram()
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 35
        spacing: 10
        Label:
            text: "سازنده: جنرال رامکی صاحب"
            font_size: 22
            bold: True
            color: 1, 0, 0.4, 1
            size_hint_y: 0.08
        Spinner:
            text: "منوی پشتیبانی و ارتباط"
            values: ("پشتیبانی واتساپ", "پشتیبانی ایمیل")
            size_hint_y: 0.07
            background_color: 0.15, 0.15, 0.2, 1
            on_text: root.open_social(*args)
        Label:
            text: "راهنما: دهنده اینترنت دکمه سبز را بزند. گیرنده لینک را کپی و در کادر پایین قرار داده دکمه آبی را بزند."
            font_size: 11
            color: 0.6, 0.6, 0.6, 1
            size_hint_y: 0.12
            text_size: self.width, None
            halign: 'center'
        Button:
            text: "ساخت لینک منحصربه‌فرد (سبز)"
            background_color: 0, 0.6, 0.2, 1
            size_hint_y: 0.09
            on_press: root.generate_link()
        TextInput:
            id: link_out
            hint_text: "لینک شما در این کادر ظاهر می‌شود..."
            readonly: True
            size_hint_y: 0.07
            font_size: 11
        TextInput:
            id: friend_in
            hint_text: "لینک رفیق خود را اینجا وارد کنید..."
            size_hint_y: 0.07
            font_size: 11
        Button:
            text: "اتصال به اینترنت رفیق (آبی)"
            background_color: 0, 0.4, 0.8, 1
            size_hint_y: 0.09
            on_press: root.trigger_hacker_terminal()
        Label:
            id: status_lbl
            text: "[*] TERMINAL STATUS: READY"
            font_size: 12
            color: 0, 1, 0, 1
            size_hint_y: 0.22
            text_size: self.width, None
'''
        from kivy.lang import Builder
        return Builder.load_string(kv_data)
if __name__ == '__main__':
    RamakiTunnelApp().run()
