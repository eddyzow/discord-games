import discord
from datetime import datetime
import math
from math import floor
import time
from firebase_admin import db
import asyncio
import os
import random
repAdder = 0
line = "unsp"
allowedUsers = []
user_search_value = "undef"
client = discord.Client()
count = 0
kicked = 0
words = "undef"
authorizedAuthors = ['eddyzow#0001','Kyle!#2949']
points = 123
repAdder2 = 0
ref = db.reference('/')
users_ref = ref.child('users')
@client.event
async def on_message(message):
    if message.content = '!free':
        #do stuff
    
    
	
            

        
@client.event
async def on_ready():
    print('Bot logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(str(os.environ.get('BOT_TOKEN')))
