import PyPDF2
import os

from colorama import Fore
from colorama import Style

class Converter:

    def convert(self, files, input_path, output_path, input_type, output_type):
    
        # Convert each file
        for i, file in enumerate(files):
            # Send converting info to terminal
            print(f"{Fore.GREEN}Converting file {i+1}/{len(files)}{Style.RESET_ALL}  {file}")
            
            # Construct paths for input and output files
            in_path = os.path.join(input_path, file)

            # Select converter type
            if input_type == '.pdf' and output_type == '.txt':

                out_path = os.path.join(output_path, os.path.splitext(file)[0] + output_type)
                self.pdf_to_txt(in_path, out_path)

            elif input_type == '.pdf' and output_path == '.docx':
                #TODO
                pass

            elif input_type == '.docx' and output_path == '.docx':
                #TODO
                pass

            elif input_type == '.docx' and output_path == '.txt':
                #TODO
                pass

            elif input_type == '.txt' and output_path == '.txt':
                #TODO
                pass

            elif input_type == '.txt' and out_path == '.docx':
                #TODO
                pass


    def pdf_to_txt(self, pdf_file_path, txt_file_path):
        # Open the PDF file
        with open(pdf_file_path, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Initialize an empty string to store extracted text
            text = ''

            # Iterate through each page of the PDF
            for page_num in range(len(pdf_reader.pages)):
                # Extract text from the page
                page_text = pdf_reader.pages[page_num].extract_text()

                # Append the extracted text to the overall text
                text += page_text

            # Write the extracted text to a text file
            with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)

    def pdf_to_docx(self):
        #TODO
        pass

    def docx_to_pdf(self):
        #TODO
        pass

    def docx_to_txt(self):
        #TODO
        pass

    def txt_to_pdf(self):
        #TODO
        pass

    def txt_to_docx(self):
        #TODO
        pass