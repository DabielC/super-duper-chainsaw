from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from te import MyApp

class LoginScreen(GridLayout):
	def __init__(self, **kwargs):#**kwargs ไว้ส่งค่าหลายๆค่า
		super(LoginScreen, self).__init__(**kwargs)
		self.cols=2
		self.rows=2
		self.add_widget(Label(text="Username"))
		self.username=TextInput(multiline=True)
		self.add_widget(self.username)#พิกัด x,y เริ่มที่ล่างซ้าย
		self.add_widget(Label(text="Password"))
		self.password=TextInput(password=True,multiline=False)
		self.add_widget(self.password)

class MyApp(App):
	def build(self):
		return LoginScreen()

MyApp().run()
