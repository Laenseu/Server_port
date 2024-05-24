The source code is already have exe file and the step below is to convert the python file to exe file
To conver a Python script to an executable file

install Pyinstaller 

Step 1: Install Pyinstaller
pip install pyinstaller

Step 2: Prepare Your Script
make sure the script is ready and tested

Step 3: Create the Executable
use Pyinstaller to create the executable from your python script

pyinstaller --onefile server.py
  "--onefile: This option tells PyInstaller to bundle everything into a single executable file."

Step 4: Locate the Executable
After running the command, PyInstaller will generate several files and directories. The executable file will be located in the dist directory inside your project folder.

