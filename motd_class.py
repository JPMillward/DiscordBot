#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 14:30:51 2021

@author: johnm
"""

import requests
import re
import html2markdown as h2m

class Motd():
    
    
    def __init__(self, api_location, last_post):        
        self.search = api_location + '_fields='
        self.last_post = last_post
    
    def check_id(self):
        self.search_id = self.search + 'id'
        print('Searching')
        id_check = requests.get(self.search_id)
        self.id = id_check.json()[0]['id']
        print(f'Last post id = {self.last_post}')
        print(f'Current post id = {self.id}')
        if int(self.last_post) == int(self.id):
            print("No new posts since last query.")
            return None
        else:
            print(self.id)
            return self.id
        
    def pull_content(self):
        self.search_content = self.search + 'content.rendered'
        print('Requesting MoTD')
        r = requests.get(self.search_content) 
        motd = r.json()
        content = motd[0]['content']['rendered']
        fuck_nbsp = re.sub('&nbsp;', '', content)
        markdown = h2m.convert(fuck_nbsp)
        self.content = re.sub('\n    \n    \n    \n    \n    ','', markdown)
        
        #print(repr(self.content))
        return self.content
        

    def discord_compliant(self, content, limit = 2000):
        
        #Conditional to skip unnecessary steps
        char_limit = limit
        if len(content) < char_limit : 
            print("Content is already shorter than the max of {char_limit} characters.")
            return content
        print(f"Post is {len(content)} characters long.")
        
        #NVariables to define acceptable post bounds
        position = 0
        max_messages = int(len(content)/char_limit) + int(len(content) % char_limit > 0)
        buffer_characters = 0
        min_characters = round(len(content)/max_messages)
        print(f"starting at position ({position}), limiting messages to ({max_messages})")
        print(f"Requiring a mininmum initial length of ({min_characters})")
        self.compliant = []
        while len(content) - position > char_limit:
                break_des = '\n    \n    \n'
                next_break = content.find(break_des, position+int(min_characters), position+int(char_limit))
                buffer_characters = next_break - (position + min_characters)
                min_characters = len(content)/max_messages - buffer_characters
                print(f"Current position({position}), Next break ({next_break}), Buffer Size is ({buffer_characters})")
                #print(content[position:next_break])
                self.compliant.append(content[position:next_break])
                position += next_break
        self.compliant.append(content[position:])
        return self.compliant
    
    def get_motd(self):
        if Motd.check_id(self) == None : return None
        content = Motd.pull_content(self)
        message = Motd.discord_compliant(self, content)
        return message
