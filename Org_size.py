import os
import shutil
import time


def Organize_size(path):

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
            file_size = os.stat(file_path).st_size / 1000
            if file_size <= 100:
                dir_path = os.path.join(path, "Organized Files")
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)
                dest_folder = os.path.join(dir_path, "Small Size")
                if not os.path.exists(dest_folder):
                    os.mkdir(dest_folder)
                shutil.move(file_path, dest_folder)
            elif file_size > 100 and file_size <= 1024:
                dir_path = os.path.join(path, "Organized Files")
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)
                dest_folder = os.path.join(dir_path, "Mid Size")
                if not os.path.exists(dest_folder):
                    os.mkdir(dest_folder)
                shutil.move(file_path, dest_folder)
            else:
                dir_path = os.path.join(path, "Organized Files")
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)
                dest_folder = os.path.join(dir_path, "Large Size")
                if not os.path.exists(dest_folder):
                    os.mkdir(dest_folder)
                shutil.move(file_path, dest_folder)

    print("Working on it..Please wait !!")
    time.sleep(1)
    print("-> -> -> -> -> -> -> -> -> ->")
    time.sleep(1)
    print("Your Files are organized")
