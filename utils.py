import os

def get_list_of_files(folder_path, file_extesion):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Filter out only the PDF files
    selected_files = [file for file in files if file.endswith(file_extesion)]

    return selected_files