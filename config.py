import os
import subprocess
import sys
from time import sleep

def start_code():
    subprocess.run(["python3", "main.py"])

def check_and_install_package(venv_name='backend', package_name='MailTm'):
    if not os.path.isdir(venv_name):
        print(f"[!] Dont {venv_name} in directory! ")
        sleep(0.7)
        print(f"[!] Creating...")
        os.system("python -m venv backend")
        print("[+] Created!")
    else:
        print(f"[!] {venv_name} in directory! ")

    pip_path = os.path.join(venv_name, 'bin', 'pip')

    # Library
    try:
        installed_packages = subprocess.check_output([pip_path, 'list']).decode('utf-8')
        if package_name in installed_packages:
            print(f"[!] Library {package_name} as installed!")
        else:
            print(f"[!] Library {package_name} not installed. Installing...")
            subprocess.check_call([pip_path, 'install', package_name])
            print(f"[+] Library {package_name} successfully installed.")
    except subprocess.CalledProcessError as e:
        print(f"Except: {e}")
    except FileNotFoundError:
        print(f"Not directory {venv_name}.")

check_and_install_package()
#start_code()
