import requests
from colorama import Fore, init

init(autoreset=True)

def fragmentcheck(username):
    url = f'https://fragment.com/username/{username}'
    response = requests.get(url, allow_redirects=True)

    if response.url.startswith("https://fragment.com/?query="):
        return False  
    if '<span class="tm-section-header-status tm-status-avail">Available</span>' in response.text:
        return True  
    if '<span class="tm-section-header-status tm-status-taken">Taken</span>' in response.text:
        return True  
    return None  

with open('input.txt', 'r', encoding='utf-8') as f:
    usernames = [line.strip() for line in f if line.strip()]

with open('output.txt', 'w', encoding='utf-8') as output:
    for username in usernames:
        r = requests.get(f'https://t.me/{username}')
        if '<i class="tgme_icon_user"></i>' in r.text:
            
            fragment = fragmentcheck(username)

            if fragment is False:
                status = "AVAILABLE"
                color = Fore.GREEN
                print(color + f"[{status}] {username}")
                output.write(f"{username}\n")  
            elif fragment is None:
                status = "UNKNOWN"
                color = Fore.YELLOW
                print(color + f"[{status}] {username}")
            else:
                status = "TAKEN"
                color = Fore.RED
                print(color + f"[{status}] {username}")
        else:
            status = "TAKEN"
            color = Fore.RED
            print(color + f"[{status}] {username}")
