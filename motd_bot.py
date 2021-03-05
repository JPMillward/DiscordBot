#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 22:08:45 2021

@author: johnm
"""

import discord
from motd_class import Motd
from dotenv import load_dotenv, find_dotenv
import os
from os.path import join, dirname


#Environment Variables for Discord Bot
#DISCORD_TOKEN=ODE0MjMxOTcyODA0ODIxMDAy.YDa2ng.wmRMKLmo7xw7rzAgkf5nn4dEZAQ
#REQUEST_LINK=https://www.endofthelinegaming.com/wp-json/wp/v2/posts?per_page=1&
#https://www.endofthelinegaming.com/wp-json/wp/v2/posts?per_page=1&\
dotenv_path = join(dirname("~/Documents/GitHub/DiscordBot/"), '.env')
load_dotenv(dotenv_path)
TOKEN = os.getenv("DISCORD_TOKEN")
EOTL_API = os.getenv("REQUEST_LINK")
print(TOKEN)
print(str(TOKEN))
print(repr(TOKEN))
print(repr(EOTL_API))