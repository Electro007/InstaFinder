# -*- coding: utf-8 -*-
"""
@author: electro007
"""

from re import search
import io
import json


FILTERED_DICT = {}

keywords = io.open('keyword.txt')
lines = keywords.readlines()


with io.open('data/raw_data.json','r+',encoding="utf-8") as file:
    data = json.load(file)
    for key, value in data.items():
        for keyword in lines:
            if search(keyword,key) or search(keyword, value):
                FILTERED_DICT[key] = value
    keywords.close()
     
with io.open('data/filtered_data.json','w+', encoding="utf-8") as file:
    json.dump(FILTERED_DICT, file, indent=4, ensure_ascii=False)
    
    
    
