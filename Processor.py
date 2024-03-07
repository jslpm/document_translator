from Converter import Converter

class Processor():

    def __init__(self):
        self.data = None
        self.converter = Converter()
    
    def validate(self, data: dict):
        self.data = data
        print('Processing information....')
        for key, value in self.data.items():
            print(f"key: {key}, value: {value}")
        print('*'*20)

        if data['if'] == "" or data['of'] == "" or data['ifp'] == "Select folder" or \
            data['ofp'] == "Select folder" or data['il'] == "" or data['ol'] == "":
            return False
        else:
            return True
    
    def process(self):
        pass
