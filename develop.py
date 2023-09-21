import os

def list_files_to_download():
    folder_path = "files"  # Substitua com o caminho completo da pasta se necessário

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        for index, file in enumerate(files):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                print(str(index) + ' - ' + file)

list_files_to_download()