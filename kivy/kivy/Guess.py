from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, ListProperty
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
import random


Window.size = (300, 400)
Name = []
score = []

class Core(Screen):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.word = ""
		self.list1 = []
		self.cnt = 0
	def pt(self):
		if len(self.word.text) > 2:
			self.list1.append(self.word.text)
			self.word.text=""
			self.cnt += 1
			self.ids.name_label.text = "Count : " + str(self.cnt)
		elif 1 <= len(self.word.text) <= 2:
			show_popup()

		return self.list1, self.cnt
	def pass_word(self):
		if self.list1 != []:
			Name.append(self.list1)
			score.append(int(self.cnt))
		else:
			show_popup1()

class Guess(Screen):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.num = 0
	def split_word(self):
		if Name[0] != []:
			self.btn.text = "Submit"
			quest = list(random.choice(Name[0]))
			q_copy = ''.join(quest.copy())
			global temp
			temp = ''.join(quest)
			print(temp)
			times = random.randint(2,len(quest)-1)

			for i in range(times):
				index_quest = random.randint(2, len(quest)-1)
				if quest[index_quest] != ' ':
					quest[index_quest] = '_'
				elif quest[index_quest] == ' ':
					times += 1
			self.miss_word.text = ''.join(quest)
			Name[0].remove(q_copy)

			if self.answer.text == temp:
				self.num += 1
			self.answer.text = ""
		else:
			if self.answer.text == temp:
				self.num += 1
			temp = 0
			self.ids.miss_word.text = "%d" %(self.num)
			self.answer.text = ""

class No_word(Screen):
	def diss_miss(self):
		need_word.dismiss()

def show_popup1():
	show = No_word()
	global need_word
	need_word = Popup(title="", content=show, size_hint=(None,None), size=(300,300))
	need_word.open()

class Syl_2(FloatLayout):
	def diss_miss(self):
		popupWindow.dismiss()

def show_popup():
	show = Syl_2()
	global popupWindow
	popupWindow = Popup(title="", content=show, size_hint=(None,None), size=(300,300))
	popupWindow.open()

class Manager(ScreenManager):
	pass

kv = Builder.load_file("guess.kv")

class guessApp(App):
	def build(self):
		return kv

guessApp().run()
