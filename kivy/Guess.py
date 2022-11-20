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


Window.size = (500, 400)
Name = []
full_score = []
score = 0

class Core(Screen):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.word = ""
		self.list1 = []
		self.cnt = 0
	def pt(self):
		if self.word.text not in self.list1:
			if len(self.word.text) > 2:
				self.list1.append(self.word.text)
				self.word.text=""
				self.cnt += 1
				self.ids.name_label.text = "Count : " + str(self.cnt)
			elif 1 <= len(self.word.text) <= 2:
				show_popup()
		else:
			self.word.text=""


	def pass_word(self):
		if self.list1 != []:
			Name.append(self.list1)
			full_score.append(int(self.cnt))
		else:
			show_popup1()


def spliter(Text):
	splited = []
	do = Text
	checker = Text.copy()
	for i in range(len(do)):
		quest = list(random.choice(do))
		q_copy = ''.join(quest.copy())
		times = random.randint(2,len(quest)-1)
		for i in range(times):
			index_quest = random.randint(2, len(quest)-1)
			if quest[index_quest] != ' ':
				quest[index_quest] = '_'
			elif quest[index_quest] == ' ':
				times += 1
		splited.append(''.join(quest))
		do.remove(q_copy)
	return splited, checker

class Guess(Screen):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.num = 0
	def on_enter(self):
		self.splited, self.check = spliter(Name[0])
		self.miss_word.text = "[%d]\n" %(self.num) + self.splited[0]
		self.i = len(self.splited) - 1

	def runner(self):
		if self.i > 0:
			self.miss_word.text = "[%d]\n" %(self.num) + self.splited[self.i]
			if self.answer.text in self.check:
				self.num += 1
				self.miss_word.text = "[%d]\n" %(self.num) + self.splited[self.i]
				self.i -= 1
			else:
				self.miss_word.text = "[%d]\n" %(self.num) + self.splited[self.i]
				self.i -= 1
			self.answer.text = ""
		else:
			if self.answer.text in self.check:
				self.num += 1
				score = self.num
				self.miss_word.text = "%d/" %score + "%d" %full_score[0]
				self.answer.text = ""
			else:
				score = self.num
				self.miss_word.text = "%d/" %score + "%d" %full_score[0]
				self.answer.text = ""


class No_word(Screen):
	def diss_miss(self):
		need_word.dismiss()

def show_popup2():
	show = No_word()
	global need_word
	need_word = Popup(title="", content=show, size_hint=(None,None), size=(300,300))
	need_word.open()

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

class Memorry_helperApp(App):
	def build(self):
		return kv

Memorry_helperApp().run()
