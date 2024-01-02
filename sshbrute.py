#!/usr/bin/env python3


import argparse


def get_args():
    parser = argparse.ArgumentParser(description="SSH Bruteforcer")

    parser.add_argument('target', dest='target', required=True, type=str, help="host to attack on e.g. 93.184.216.34")
    parser.add_argument('-p', '--port', dest='port', default=22, required=False, type=int, help="port to attack on, default:22")
    parser.add_argument('-w', '--wordlist', dest='wordlist', required=True, type=str, help="list of passwords to use")
    parser.add_argument('-u', '--username', dest='username', required=True, type=str, help="username to use")

    args = parser.parse_args()

    return args