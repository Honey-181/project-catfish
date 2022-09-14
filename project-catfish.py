#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Project catfish

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

from shutil import which

print(G + '[+]' + C + 'Starting Project-catfish')
print(G + '[+]' + C + 'Project catfish')

row = []
info = ''
result = ''
version = '1.0'

print(G + '[>]' + C + 'version :' + W + version + '\n')

def ver_check():
    print(G + '[+]' + C + ' Checking for Updates.....', end='')
    ver_url = 'https://raw.githubusercontent.com/Optane002/catfish/main/version.txt'
    try:
        ver_rqst = request.get(ver_url)
        ver_sc = ver_rqst.status_code
        if ver_sc == 200:
            github_ver = ver_rqst.text
            github_ver = github_ver.strip()

            if version == github_ver:
                print(C + '[' + G + ' Up-To-Date ' + C +']' + '\n')
            else:
                print(C + '[' + G + ' Available : {} '.format(github_ver) + C +>
        else:
            print(C + '[' + R + ' Status : {} '.format(ver_sc) + C + ']' + '\n')
    except Exception as e:
        print('\n' + R + '[-]' + C + ' Exception :' + W + str(e))
