import os
import shutil
import datetime
import time


def Organize_month(path):

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
            file_time = os.stat(file_path).st_mtime
            file_time_accurance = \
                datetime.datetime.fromtimestamp(file_time).strftime('%Y-%B')
            dir_path = os.path.join(path, 'Organized Files')
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
            dest_folder = os.path.join(dir_path, file_time_accurance)
            if not os.path.exists(dest_folder):
                os.mkdir(dest_folder)
            shutil.move(file_path, dest_folder)

    print("Working on it..Please wait !!")
    time.sleep(1)
    print("-> -> -> -> -> -> -> -> -> ->")
    time.sleep(1)
    print("Your Files are organized")
