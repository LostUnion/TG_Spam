import random
import string
import time
import pyfiglet
from os import system
from venv import create

import pymysql
from telethon import functions, types
from telethon.sync import TelegramClient

from SettingsSession.session_settings import API_HASH, API_ID, SESSION_NAME




def New_Contact():
    system('cls')
    system('Color b')
    system("mode con cols=90 lines=40")
    result = pyfiglet.figlet_format("CONTACT", font = "banner3-D")
    print(result)

    my_name_session = (SESSION_NAME)
    my_user_api_id = (API_ID)
    my_api_hash = (API_HASH)
    id, phone = input('Enter your username and phone number separated by a space: ').split()


    with TelegramClient(my_name_session, my_user_api_id, my_api_hash) as client:
        result = client(functions.contacts.AddContactRequest(
        id=id,
        first_name=("user"),
        last_name=("user"),
        phone=phone,
        add_phone_privacy_exception=True
    ))

    print("Contact added successfully!")
    answer = input('Do you want to continue?(y/n) ')
    if (answer == 'y'):
        New_Contact()
    elif (answer == 'n'):
        system('exit')
        system('Color 7')
        system('cls')
    else:
        system('exit')
        system('Color 7')
        system('cls')
New_Contact()
    
#time.sleep(5)
#system('cls')
    