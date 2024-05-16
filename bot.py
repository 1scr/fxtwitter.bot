'''
--------------
FX-TWITTER BOT
--------------

> Made with 💖 in France by EletrixTime

(https://github.com/1scr/fxtwitter.bot)
'''
regex = r'https://(twitter\.com|x\.com)'

import os
from interactions import *
import json
import re

config = json.loads(open("config.json").read())
bot = Client(intents=Intents.DEFAULT)

for i in config["status"]:
    print(i)

@listen()  
async def on_ready():
    print("Bot prêt")

@listen()
async def on_message_create(event):
    msg = event.message.content
    if msg.startswith("https://twitter.com") or msg.startswith("https://x.com"):
        channel = await bot.fetch_channel(event.message.channel.id);await channel.delete_message(event.message.id)
        d = re.sub(regex, '', msg)
        print(d)
        await channel.send(f"{d} \n \n \n > Message Original de <@{event.message.author.id}>")