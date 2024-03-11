import os
import googletrans

from colorama import Fore
from colorama import Style


class Translator:

    def translate(self, files, input_path, output_path, input_type, output_type, input_lang, output_lang):
        self.files = files
        self.input_path = input_path
        self.output_path = output_path
        self.input_type = input_type
        self.output_type = output_type
        self.input_lang = input_lang
        self.output_lang = output_lang

        self.remove_line_breaks_all_files()
        self.translate_all_files()

    def remove_line_breaks(self, input_file, output_file):
        # Read the contents of the input file
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
    
        # Remove line breaks from the text
        text = text.replace('\n', ' ')
    
        # Write the modified text back to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
    
    def remove_line_breaks_all_files(self):
        # Convert each TXT file to text
        for i, txt_file in enumerate(self.files):
            print(f"{Fore.GREEN}Removing break lines file {i+1}/{len(self.files)}{Style.RESET_ALL}  {txt_file}")

            # Construct paths for input TXT and output text files
            txt_in_path = os.path.join(self.input_path, txt_file)
            txt_out_path = os.path.join(self.output_path, txt_file)

            # Convert the TXT to text
            self.remove_line_breaks(txt_in_path, txt_out_path)

    def translate_text_file(self, input_file, output_file, source_lang='en', target_lang='es'):
        # Read the input text from the file
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()

        # Create a translator object
        translator = googletrans.Translator(service_urls=['translate.googleapis.com'])
    
        if len(text.strip()) == 0:
            print(f"{Fore.YELLOW}Empty file!{Style.RESET_ALL}  {os.path.basename()}")
        else:
            # Translate the text
            translated_text = translator.translate(text, src=source_lang, dest=target_lang)
            # Write the translated text to the output file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(translated_text.text)

    def translate_all_files(self):
        for i, txt_file in enumerate(self.files):
            print(f"{Fore.GREEN}Translating file {i+1}/{len(self.files)}{Style.RESET_ALL}  {txt_file}")

            txt_in_path = os.path.join(self.input_path, txt_file)
            txt_out_path = os.path.join(self.output_path, txt_file)

            self.translate_text_file(txt_in_path, txt_out_path, source_lang=self.input_lang, target_lang=self.output_lang)
