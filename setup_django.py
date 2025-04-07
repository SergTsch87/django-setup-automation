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
import pathlib
import subprocess
import platform
import inspect


def some_func_1(a: int, b: int):
    return a + b


def some_func_2():
    print('some text')


def is_path_venv_file(path_file):
    venv_file = f'{os.getcwd()}{path_file}'
    if os.path.isfile(venv_file):
        return True
    else:
        return False


def get_name_os():
    return platform.system()


def main():
    # path_venv_file = '/.venv/Scripts/python.exe'
    # if is_path_venv_file(path_venv_file):
    #     print(f'+ Файл {path_venv_file} існує')
    # else:
    #     print(f'- Файл {path_venv_file} не існує')

    # subprocess.run(['powershell', '-Command', f'ls "{os.getcwd()}"'])
    
    # !
    # subprocess.run(['powershell', '-Command', 'py -m venv .venv2'])

    # print(inspect.get(inspect.currentframe()))
    # print(inspect.args(subprocess.run(['powershell', '-Command', 'ls'])))
    # print(inspect.signature( subprocess.run(['powershell', '-Command', 'ls']) ).arguments)

    # print(get_name_os())

    shell = os.environ.get('SHELL') or os.environ.get('COMSPEC', '').lower()
    
    if get_name_os() == 'Windows':
        if 'powershell' in shell or 'pwsh' in shell:
            subprocess.run(['pwsh', '-Command', '.venv\\Scripts\\Activate.ps1'])
        if 'cmd' in shell:
            subprocess.run(['cmd.exe', '/k', '.venv\\Scripts\\activate.bat'])
    elif get_name_os() == 'Unix':
        subprocess.run(['pwsh', '-Command', '.venv\\bin\\Activate.ps1'])

    # # !!!
    # # if you want to run commands inside the activated environment, you should:
    # subprocess.run(['pwsh', '-Command', '& .venv\\Scripts\\Activate.ps1; python your_script.py'])
    
    
    # subprocess.run(['pwsh', '-Command', f'ls "{os.getcwd()}"'])
    
    # try:
    #     subprocess.run(['pwsh', '-Command', f'ls "{os.getcwd()}"'])
    # except FileNotFoundError as e:
    #     subprocess.run(['powershell', '-Command', f'ls "{os.getcwd()}"'])


if __name__ == '__main__':
    main()