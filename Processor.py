from Converter import Converter
from Merger import Merger
from Translator import Translator
from utils import get_list_of_files

class Processor():

    def __init__(self):
        self.data = None
        self.converter = Converter()
        self.merger = Merger()
        self.translator = Translator()
    
    def validate(self, data: dict):
        self.data = data
        # print('Processing information....')
        # for key, value in self.data.items():
        #     print(f"key: {key}, value: {value}")
        # print('*'*20)

        # Check selected options from kivy widgets
        # Must exist a function selected
        if self.data["ft"] == '':
            return False, "Select a function."

        if self.data['if'] == '':
            return False, "Select input format type."
        elif self.data['of'] == '':
                return False, "Select output format type."
        elif self.data['ifp'] == '':
            return False, "Select input folder path."
        elif self.data['ofp'] == '':
            return False, "Select output folder path."

        if self.data["ft"] == "merge":
            return True, 'merge'
        elif self.data["ft"] == "convert":
            return True, "convert"
        elif self.data["ft"] == "translate":
            if self.data['il'] == '':
                return False, "Select input language."
            elif self.data['ol'] == '':
                return False, "Select output language."
            else:
                return True, "translate"
        else:
            raise Exception("In Processor.validate(self). Unknown selected argument.")

    def process(self):
        # Get list of file from input folder
        files = get_list_of_files(self.data['ifp'], self.data['if'])

        # Perform selected operation
        if self.data['ft'] == 'convert':
            print("Converting...")
            self.converter.convert(files, self.data['ifp'], self.data['ofp'], self.data['if'], self.data['of'])
            print("Done.")
        elif self.data['ft']  == 'merge':
            print("Merging...")
            self.merger.merge(files, self.data['ifp'], self.data['ofp'], self.data['if'], self.data['of'])
            print("Done.")
        elif self.data['ft']  == 'translate':
            print('Translating')
            self.translator.translate(files, self.data['ifp'], self.data['ofp'], self.data['if'], self.data['of'], self.data['il'], self.data['ol'])
            print('Done.')
        else:
            raise Exception("In Processor.process(self), unknown operation.")