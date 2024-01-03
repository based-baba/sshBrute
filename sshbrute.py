#!/usr/bin/env python3


import argparse
import asyncio
from os import path
from sys import exit
from datetime import datetime
from termcolor import colored


def get_args():
    parser = argparse.ArgumentParser(description="SSH Bruteforcer")

    parser.add_argument('target', type=str, help="host to attack on e.g. 93.184.216.34")
    parser.add_argument('-p', '--port', dest='port', default=22, required=False, type=int, help="port to attack on, default:22")
    parser.add_argument('-w', '--wordlist', dest='wordlist', required=True, type=str, help="list of passwords to use")
    parser.add_argument('-u', '--username', dest='username', required=True, type=str, help="username to use")

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    args = get_args()

    if not path.exists(args.wordlist):
        print(colored(f"[-] {args.wordlist} : No such file or directory", "red"))
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
