import os
from kivy.app import App
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from Processor import Processor


class FileDialog(FloatLayout):
    default_path = StringProperty(os.getcwd())
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class ErrorDialog(FloatLayout):
    cancel = ObjectProperty(None)
    message = StringProperty(None)

class MainWidget(BoxLayout):
    
    input_format = StringProperty("")
    output_format = StringProperty("")
    is_merge_active = BooleanProperty(False)
    is_translate_active = BooleanProperty(False)
    input_folder_path = StringProperty("Select folder")
    output_folder_path = StringProperty("Select folder")
    input_language = StringProperty("")
    output_language = StringProperty("")
    vars_dict = dict()

    btn_idx = None

    processor = Processor()

    def on_button_click(self):
        # Add gui variables to a dictionary
        self.vars_dict.update({'if': self.input_format})
        self.vars_dict.update({'of': self.output_format})
        self.vars_dict.update({'ima': self.is_merge_active})
        self.vars_dict.update({'ita': self.is_translate_active})
        self.vars_dict.update({'ifp': self.input_folder_path})
        self.vars_dict.update({'ofp': self.output_folder_path})
        self.vars_dict.update({'il': self.input_language})
        self.vars_dict.update({'ol': self.output_language})

        # Validate entered data by user
        is_correct = self.processor.validate(self.vars_dict)
        if is_correct is True:
            print("Do tasks")
            self.processor.process()
        else:
            # print("Cannot realize operation.")
            self.load_error_dialog("Cannot realize operation.")

    def load_error_dialog(self, message):
        content = ErrorDialog(cancel=self.dismiss_popup, message=message)
        self.popup = Popup(title="Error", content=content, size_hint=(0.6, 0.4))
        self.popup.open()

    def load_file_dialog(self, btn_idx):
        self.btn_idx = btn_idx
        content = FileDialog(load=self.load, cancel=self.dismiss_popup)
        self.popup = Popup(title="Select folder", content=content, size_hint=(0.9, 0.9))
        self.popup.open()

    def dismiss_popup(self):
        self.popup.dismiss()

    def load(self, path, filename):
        if self.btn_idx == 0:
            self.input_folder_path = path
        elif self.btn_idx == 1:
            self.output_folder_path = path
        else:
            raise Exception
        self.popup.dismiss()

    def on_input_format_spinner(self, text):
        self.input_format = text
        # print(text)

    def on_output_format_spinner(self, text):
        self.output_format = text
        # print(text)

    def on_merge_checkbox_click(self, is_active):
        self.is_merge_active = is_active
        # print(is_active)

    def on_translate_checkbox_click(self, is_active):
        self.is_translate_active = is_active
        # print(is_active)

    def on_from_lang_spinner(self, text):
        self.input_language = text
        # print(text)
    
    def on_to_lang_spinner(self, text):
        self.output_language = text
        # print(text)

class TheLabApp(App):
    pass

TheLabApp().run()