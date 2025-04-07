# Task 2: Automate Dependency Handling
# Write a Python script that:
# Checks if a virtual environment exists.
# If not, creates and activates it


# To solve this task, use the built-in `os` and `pathlib` modules to check for the virtual environment folder.  
# Use the `subprocess` module to run shell commands from within Python.  
# To create a virtual environment, use the `venv` module.  
# Detect the OS using `platform` to choose the correct activation method (Windows vs. Unix).  
# You can store the activation command as a string and optionally run it via a subprocess or display it for manual activation.  
# Use `sys` for paths and environment-related checks if needed.

import os
import sys
import subprocess
import platform
from  pathlib import Path


def get_os():
    return platform.system()


def is_file(path: Path) -> bool:
    return path.is_file()


def create_venv(venv_path: Path):
    print(f'Creating virtual environment at: {venv_path}')
    subprocess.run([sys.executable, '-m', 'venv', str(venv_path)])


def is_path_file(path_file):
    if os.path.isfile(path_file):
        return True
    else:
        return False


def get_name_os():
    return platform.system()


def venv_activate():
    shell = os.environ.get('SHELL') or os.environ.get('COMSPEC', '').lower()
    
    if get_name_os() == 'Windows':
        if 'powershell' in shell or 'pwsh' in shell:
            subprocess.run(['pwsh', '-Command', '.venv\\Scripts\\Activate.ps1'])
        if 'cmd' in shell:
            subprocess.run(['cmd.exe', '/k', '.venv\\Scripts\\activate.bat'])
    elif get_name_os() == 'Unix':
        subprocess.run(['pwsh', '-Command', '.venv\\bin\\Activate.ps1'])


def main():
    path_venv_file = '/.venv/Scripts/python.exe'
    venv_file = f'{os.getcwd()}{path_venv_file}'
    
    if is_path_file(venv_file):
        print(f'+ Файл {venv_file} існує')
    else:
        print(f'- Файл {venv_file} не існує')
        subprocess.run(['pwsh', '-Command', 'py venv .venv'])
        venv_activate()

        path_requests_file = '/requests.txt'
        requests_file = f'{os.getcwd()}{path_requests_file}'
        
        if not is_path_file(requests_file):
            subprocess.run(['pwsh', '-Command', 'pip install -r requests.txt'])
            print('Install libs from requests.txt')
        else:
            subprocess.run(['pwsh', '-Command', 'type nul > requests.txt; pip install django; pip freeze > requests.txt'])
            print('To create file requests.txt and writing installing libs to requests.txt')

    
    # # !!!
    # # if you want to run commands inside the activated environment, you should:
    # subprocess.run(['pwsh', '-Command', '& .venv\\Scripts\\Activate.ps1; python your_script.py'])
    

if __name__ == '__main__':
    main()