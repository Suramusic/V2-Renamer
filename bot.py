import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5713245787:AAF-x7x7vbxcWO98HFbrkPI8FDIH24iw4Ww")

API_ID = int(os.environ.get("API_ID", "24531402"))

API_HASH = os.environ.get("API_HASH", "0f75926e95a476ccff47dacb52079053")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
