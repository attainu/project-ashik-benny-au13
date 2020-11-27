import os
import shutil
import time


def Organize_ext(path):

    DIRECTORIES = {
        "Images": [".jpeg", ".jpg", ".png", "..JPG"],
        "Videos": [".flv", ".mp4", ".mpg", ".mpeg", ".3gp"],
        "Audios": [".aac", ".mp3", ".vox", ".wav", ".wpl"],
        "Programming_softs": [".html", ".c", ".css", ".java", ".py"],
        "Designing_softs": [".psd", ".cdr"],
        "Applications": [".app", ".ipa", ".apk", ".exe"],
        "Documents": [".docx", ".doc", ".dox", ".xls", ".pdf", ".xlsx"],
        "Plain_texts": [".txt", ".in", ".out"],
        "Zips": [".a", ".tar", ".rar", ".xar", ".zip"],
    }

    FILE_FORMATS = {
        file_format: directory
        for directory, file_formats in DIRECTORIES.items()
        for file_format in file_formats
    }

    for file in os.scandir(path):
        if not file.is_dir():
            file_path = os.path.abspath(file)
            if os.path.basename(file_path) in (
                "main.py",
                "Org_ext.py",
                "Org_size.py",
                "Org_month.py",
            ):
                continue
            file_format = os.path.splitext(file_path)[1]
            if file_format in FILE_FORMATS:
                dir_path = os.path.join(path, "Organized Files")
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)
                dest_folder = os.path.join(dir_path, FILE_FORMATS[file_format])
                if not os.path.exists(dest_folder):
                    os.mkdir(dest_folder)
                shutil.move(file_path, dest_folder)
            else:
                dir_path = os.path.join(path, "Unknown_Files")
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)
                shutil.move(file_path, dir_path)

    print("Working on it..Please wait !!")
    time.sleep(1)
    print("-> -> -> -> -> -> -> -> -> ->")
    time.sleep(1)
    print("Your Files are organized")
