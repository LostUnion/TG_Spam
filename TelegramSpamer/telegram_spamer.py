from ctypes import sizeof
from tabnanny import check
from unittest import result
import pyfiglet
import time
from time import sleep
from os import system
from email import message
from social_spam import Telegram
from TelegramSpamer.telegram_users_id import USERS_ID
from SettingsSession.session_settings import API_ID, API_HASH, NUMBER_PHONE
from TelegramSpamer.message import Message

system('cls')
system('Color 2')
system("mode con cols=90 lines=40")
result = pyfiglet.figlet_format("PROJECT", font = "banner3-D")
print(result)

def TelegramSpamer():
    print("Program launch")
    print("")
    print("Connecting to personal server")
    time.sleep(0.3)
    print("Connecting to personal server.")
    time.sleep(0.3)
    print("Connecting to personal server..")
    time.sleep(0.3)
    print("Connecting to personal server...")
    time.sleep(0.3)
    print("")

tg = Telegram()
tg.connect_user(API_ID, API_HASH, NUMBER_PHONE)

def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent} % {suffix}', end='\r')
    if iteration == total:
        print()

items = list(range(0, 40))
l = len(items)

loadbar(0, l, prefix="Authorization validity check", length=l)
for i, item in enumerate(items):
    sleep(0.02)
    loadbar(i + 1, l, prefix="Authorization validity check", length=l)

print("")
print("Connection secured")
time.sleep(0.3)
print("")

#print("Checking the validity of USERS_ID")

def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent} % {suffix}', end='\r')
    if iteration == total:
        print()

items = list(range(0, 35))
l = len(items)

loadbar(0, l, prefix="Checking the validity of USERS_ID", length=l)
for i, item in enumerate(items):
    sleep(0.02)
    loadbar(i + 1, l, prefix="Checking the validity of USERS_ID", length=l)

check = input("Do you want to continue(y/n)? ")

if check == "y":
    print("Starting spam attack.")
    time.sleep(0.2)
    print("Starting spam attack..")
    time.sleep(0.2)
    print("Starting spam attack...")
    time.sleep(0.2)
    print("")
    user_list = USERS_ID
    tg.start_selective_spam ( user_list, message = Message)
    print("")
    print("Sent message successful!")
    time.sleep(0.3)
    print("Exit..")
    time.sleep(0.3)
    system("cls")
elif check == "n":
    print("Exit..")
    time.sleep(3)
    system('cls')
    system('exit')
else:
    time.sleep(1)
    print("Incorrect answer")
    time.sleep(3)
    print("Exit..")
    time.sleep(3)
    system('exit')

TelegramSpamer()


#tg.send_message(user_id=2093558288, message='Hello')
#tg.start_selective_spam([2093558288], 'TEST')