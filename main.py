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
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
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
    function_type = StringProperty("")
    input_folder_path = StringProperty("")
    output_folder_path = StringProperty("")
    input_language = StringProperty("")
    output_language = StringProperty("")
    vars_dict = dict()

    btn_idx = None

    processor = Processor()

    def on_button_click(self):
        # Add gui variables to a dictionary
        self.vars_dict.update({'if': self.input_format})
        self.vars_dict.update({'of': self.output_format})
        self.vars_dict.update({'ft': self.function_type})
        self.vars_dict.update({'ifp': self.input_folder_path})
        self.vars_dict.update({'ofp': self.output_folder_path})
        self.vars_dict.update({'il': self.input_language})
        self.vars_dict.update({'ol': self.output_language})

        # Validate entered data by user
        is_correct, message = self.processor.validate(self.vars_dict)
        if is_correct is True:
            self.processor.process()
        else:
            # print("Cannot realize operation.")
            self.load_error_dialog(f"Cannot realize operation. {message}")

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

    def on_radiobutton(self, radiobutton_idx):
        if radiobutton_idx == 1:
            self.function_type = 'convert'
        elif radiobutton_idx == 2:
            self.function_type = 'merge'
        elif radiobutton_idx == 3:
            self.function_type = 'translate'
        else:
            self.function_type = ''
        # print(radiobutton_idx, type(radiobutton_idx))

    def on_from_lang_spinner(self, text):
        self.input_language = text
        # print(text)
    
    def on_to_lang_spinner(self, text):
        self.output_language = text
        # print(text)

class DocumentTranslatorApp(App):
    pass

DocumentTranslatorApp().run()