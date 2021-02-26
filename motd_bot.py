#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 14:30:51 2021

@author: johnm
"""

import discord
import asyncio
import requests
import re
from html import unescape

class Motd():

    def pull_motd():  
        motd_posts = 'https://www.endofthelinegaming.com/wp-json/wp/v2/posts?'
        search_function = '_embed_fields=title,id,date,content.rendered'
        r = requests.get(motd_posts + search_function)
        
        motd = r.json()
        motd_id = motd[0]['id']
        date = motd[0]['date']
        title = motd[0]['title']['rendered']
        content = motd[0]['content']['rendered']
        
        
    
    def to_markdown(input_text, formatting = 1):
        #Translate html -> markdown
        
        underline = '</*u>'
        bold = '</*strong>'
        italics = '</*i>'
        strikethrough = '</*s>'
        other_break = '</li>'
        line_break = '</p>'
        anyhtml = '<.*>'
        
        underlined = re.sub(underline, '__', input_text)
        stricken = re.sub(strikethrough, '~~', underlined)
        bolded = re.sub(bold, '**', stricken)
        italicized = re.sub(italics, '*', bolded)
        line_breaks = re.sub(line_break, '\n', italicized)
        other_breaks = re.sub(other_break, '', line_breaks)
        nohtml = re.sub(anyhtml, '', other_breaks)
        marked_down = html.unescape(nohtml)
        #Formatting Guidelines:
        #1 = Remove doubled line breaks. 0 = nothing
        if formatting == 1:
            double_break = '\s\n\s*\n*'
            line_format = re.sub(double_break, '\n\n', marked_down)
            
            #print(marked_down)
            #print('Removed Excess Whitespace')
            return line_format
        else:
            #print(marked_down)
            #print('Maintained Whitespace')
            return marked_down
    def discord_compliant(text_input):
        x = 0
        char_compliant = []
        #print(len(text_input))
        while len(text_input) - x > 2000:
            x += text_input.find('\n\n', x+1500, x+1999)
            char_compliant.append(text_input[:x])
            #print(text_input[:x])
            #print('TEXT BREAK')
            #print('THIS IS THE BREAK')
        char_compliant.append(text_input[x:])
        return char_compliant