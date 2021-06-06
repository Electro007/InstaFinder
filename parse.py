# -*- coding: utf-8 -*-
"""
Recursive Parser for Instagram

@author : electro007
"""
import io
import os
import json
import configuration as cfg
import sys
import random
from instagrapi import Client
from Proxy_List_Scrapper import Scrapper

DICT_USERNAME_FULLNAME = {}
initial_data = None

def changeProxy():
    
    proxi = random.choice(PROXY.proxies)
    cl.set_proxy("http://"+proxi.ip+":"+proxi.port)
    print("Switched to proxy "+proxi.ip+":"+proxi.port)


def getData(level, data):
    if (level >= cfg.MAX_SCRAPING_DEEP_LEVEL):
        for user in data:
            print(user.username)
            DICT_USERNAME_FULLNAME[user.username] = user.full_name
    else:
        for user in data:
            try:
                userFollowers = cl.user_followers_gql(user.pk, cfg.FOLLOWER_PER_ACCOUNT)
                print("Got follower data of " + user.username)
            except:
                print("Failed to got follower data of "+ user.username)
                changeProxy()
            DICT_USERNAME_FULLNAME[user.username] = user.full_name
            getData(level+1, userFollowers)

def startupCheck():
    try:
        os.makedirs("data",exist_ok=True)
    except OSError as e:
        sys.exit("Can't create {dir}: {err}".format(dir="data", err=e))
    
    if os.path.isfile('data/raw_data.json') and os.access('data/raw_data.json', os.R_OK):
        # checks if file exists
        print ("File exists and is readable")
    else:
        print ("Either file is missing or is not readable, creating file...")
        with io.open('data/raw_data.json', 'w') as file:
            file.write(json.dumps({}))
def savingData(file):
            data = json.load(file)
            data.update(DICT_USERNAME_FULLNAME)
            file.seek(0)
            json.dump(data, file, indent=4, ensure_ascii=False)
                
if __name__ == '__main__':
    #Create "data" folder if not exist
    startupCheck()
    

    #Start scraping proxy
    scrapper = Scrapper(category='ALL', print_err_trace=False)
    PROXY = scrapper.getProxies()

    #Start Instagram Bot
    cl = Client()
    cl.login(cfg.ACCOUNT_USERNAME, cfg.ACCOUNT_PASSWORD)
    user_id = cl.user_id_from_username(cfg.FIRST_ACCOUNT_USERNAME)
    

    try:
        initial_data = cl.user_followers_gql(user_id, cfg.FOLLOWER_PER_ACCOUNT)
        print("Got follower data of " + cfg.FIRST_ACCOUNT_USERNAME)
    except:
        print("Failed to got follower data of "+ cfg.FIRST_ACCOUNT_USERNAME)
        changeProxy()

    
    with io.open('data/raw_data.json','r+', encoding="utf-8") as file:
        try:
            getData(0, initial_data)
        except:
            savingData(file)
        savingData(file)