import requests
from colorama import Fore, init

init(autoreset=True)

with open('input.txt', 'r', encoding='utf-8') as f:
    usernames = [line.strip() for line in f if line.strip()]

with open('output.txt', 'w', encoding='utf-8') as output:
    for username in usernames:
        r = requests.get(f'https://t.me/{username}')
        if '<i class="tgme_icon_user"></i>' in r.text:
            print(Fore.GREEN + f"[AVAILABLE] {username}")
            output.write(username + '\n')
        else:
            print(Fore.RED + f"[TAKEN] {username}")
