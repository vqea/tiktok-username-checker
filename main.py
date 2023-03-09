import requests, os, colorama
from colorama import Fore , Back , Style
colorama.init (autoreset = True)

os.system('pip install requests')
os.system('pip install colorama')

print(f"""{Fore.TEAL}
 _   _ _    _        _    
| |_(_) | _| |_ ___ | | __
| __| | |/ / __/ _ \| |/ /
| |_| |   <| || (_) |   < 
 \__|_|_|\_\\__\___/|_|\_\                             
---------------------------- 
"""


available = 0
unavailable = 0
with open('usernames.txt','r') as handle:
        list = handle.readlines()
        for user in list:
          username = user.rstrip()
          if username.isdigit():
            unavailable += 1
            print(f"{Fore.RED} {username} is unavailable")
            continue
          with requests.Session() as session:
            headers = {
              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
              "accept-encoding": "gzip, deflate, br",
              "accept-language": "en-US",
              "content-type": "application/json"
            }
            r = session.head("https://www.tiktok.com/@{}".format(username), headers = headers)
            if r.status_code == 404:
                available += 1
                print(f"{Fore.GREEN} {username} is available or banned")
            elif r.status_code == 200:
                unavailable += 1
                print(f"{Fore.RED} {username} is unavailable")
        print(f"went through list.. {valid} valid, {invalid} invalid, total {len(list)}")
