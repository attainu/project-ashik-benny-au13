JUNK FILE ORGANIZER USING PYTHON LANGUAGE
------------------------------------------------------------------------------------------------------------------------------------------------

OVERVIEW
------------------------------------------------------------------------------------------------------------------------------------------------
With an organized machine (PC), user can easily find out the files instead of hunting through folders and sub-folders. Here is the code in Python with many functionalities in which user can choose whether to organize according with file extension, file size and last modified month, year of the file.

REQUIREMENTS
------------------------------------------------------------------------------------------------------------------------------------------------
	Python Language
	Importing following modules :
        - os Module
        - argparse Module
        - shutil Module
        - textwrap Module
        - datetime Module
        - time Module
	Building user defined modules
	Code beautification using auto pep8/flake8 extensions in VS code.

FUNCTIONALITIES
------------------------------------------------------------------------------------------------------------------------------------------------
	Organize by file Extension :
By using Organize_ext function in the code, files will be organized with reference to the file format (extension). While functioning, a new folder will be created named ‘Organized files’ and the files will be moved to inside of that folder within their respective file category folders.
    Code format:  python <filename.py>  --org  ext

	Organize by file Size :
By using Organize_size function in the code, files will be organized with reference to the size of the file. While functioning, a new folder will be created named ‘Organized files’. The files will be moved ‘Small size’, ‘Mid size’ and ‘Large size’ within the ‘Organized files’. 
    Code format:  python <filename.py>  --org  size

	Organize by Month, Year :
By using Organize_month function in the code, files will be organized with reference to the month & year the file is created. While functioning, a new folder will be created named ‘Organized files’ and the files will arranged based on their month & year.
    Code format:  python <filename.py>  --org  size

	The code can be also run by giving the user defined path of the location of files which the user needs to organize. For this , it is set to organize by extension by default. For that in CLI ;
Code format: python  <filename.py>  --path  “ <path of the files to be organized> “  

ADDITIONAL FEATURES
------------------------------------------------------------------------------------------------------------------------------------------------
Python code is converted into .exe format (application) for the users who is not having python language in the system.They just need to copy the exe file in the folder and run it.

FUTURE IMPROVEMENTS
------------------------------------------------------------------------------------------------------------------------------------------------
Can develop a GUI for this in which user can choose any of the above mentioned organizing methods in the UI panel itself


