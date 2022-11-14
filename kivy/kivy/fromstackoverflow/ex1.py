from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, ListProperty
from kivy.lang import Builder



class MyScreen(Screen):
    container = ObjectProperty(None)
    data_list = ListProperty([])

    def save_data(self):
        for child in reversed(self.container.children):
            if isinstance(child, TextInput):
                self.data_list.append(child.text)
                self.first_name.text = ""

        return self.data_list

class Test(Screen):
    a = MyScreen.data_list
    print(a)

class TestApp(App):
    def build(self):
        return MyScreen()

Builder.load_file('ex1.kv')

if __name__ == "__main__":
    TestApp().run()
