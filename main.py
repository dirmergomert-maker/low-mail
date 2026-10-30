# [!] dev @smoke_fear
# License MailTm [BackEnd, API]
# License manytools.org [Banner]  (https://manytools.org/hacker-tools/ascii-banner/)
# License api.ipify.org [Ip]

import os
from mailtm import Email
import requests
import socket
from datetime import datetime

r = "\033[31m"
g = "\033[32m"
d = "\033[0m"
y = "\033[33m"
b = "\033[34m"

def main( ):
    name_venv="backend"
    if os.path.isdir(name_venv):
        print(f"[+] Cheking venv...  True")
        handler()
    else:
        print(f"[-] Cheking venv...  False")
        print(f"{y}Start configure.py!")
        return False


ip = ""
banner = """
██╗      ██████╗ ██╗    ██╗                                                                 
██║     ██╔═══██╗██║    ██║                                                                 
██║     ██║   ██║██║ █╗ ██║                                                                 
██║     ██║   ██║██║███╗██║                                                                 
███████╗╚██████╔╝╚███╔███╔╝                                                                 
╚══════╝ ╚═════╝  ╚══╝╚══╝                                                                  
                                                                                            
███╗   ███╗ █████╗ ██╗██╗         ██╗  ██╗ █████╗ ███╗   ██╗██████╗ ██╗     ███████╗██████╗ 
████╗ ████║██╔══██╗██║██║         ██║  ██║██╔══██╗████╗  ██║██╔══██╗██║     ██╔════╝██╔══██╗
██╔████╔██║███████║██║██║         ███████║███████║██╔██╗ ██║██║  ██║██║     █████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║██║         ██╔══██║██╔══██║██║╚██╗██║██║  ██║██║     ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║███████╗    ██║  ██║██║  ██║██║ ╚████║██████╔╝███████╗███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
dev: @smoke_fear    
                                                                                        
"""

test = Email()

link_ip = 'https://api.ipify.org?format=json'
response = requests.get(link_ip).json()
local_ip = response['ip']
ip = local_ip
local_host = socket.gethostname()

def times():
    now = datetime.now()
    time = now.strftime("%H:%M %d/%m/%Y")
    print(time)

def clear_screen():
    if os.name == 'nt':  # Dos/Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

def listener(message):
    print("\nТема: " + message['subject'])
    print(f"Сообщение: " + message['text'] if message['text'] else message['html'])
    with open("logging.txt", 'a') as f:
        f.write(f"- - - - - - - - - - - - - - -\nEmail: {test.address}\nТема: {message['subject']}\nСообщение: {message['text'] if message['text'] else message['html']}\nTime: {datetime.now().strftime('%H:%M %d/%m/%Y')}\n")

data = {
    "Ip": f"{ip}",
    "Host": f"{local_host}",
    "Domain": f"{test.domain}",
}

def table():
    # для того кому интересна таблица есть небольшие памятки
    key_width = max(len(key) for key in data.keys()) + 2  # +2 для отступа
    value_width = max(len(value) for value in data.values()) + 2  # +2 для отступа
    print("╔" + "═" * (key_width + value_width + 5) + "╗")
    for key, value in data.items():
        print("║ {:<{}} : {:<{}} ║".format(key, key_width, value, value_width))
    print("╚" + "═" * (key_width + value_width + 5) + "╝")



def handler():
    test.register()

    clear_screen()
    print(banner)
    times()
    
    # Get Create Email
    table()
    print(f"\n{r}YOU MAIL{d}: {g}{test.address}{d}\n")

    # Start listening
    test.start(listener)
    print("\nОжидание писем...")

if __name__ == "__main__":
    main()
