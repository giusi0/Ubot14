#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telethon import TelegramClient, events
import asyncio
client = TelegramClient('@opentelegramfiles',1443535,"866638a09d2b3728ed9ca1b935003029")
@client.on(events.NewMessage)
async def MEWTWOUBOT(event):
 if event.sender_id == 1355294968:
  if event.text == '.com14': 
     await event.edit(f"[Lista Comandi!](https://telegra.ph/Comandi-attuali-3-03-31)")
  if event.text == '.dev':
     await event.edit('Developer👨🏼‍💻=[Mewtwo](tg://user?id=1240217051)')
  if event.text == '.fbi':
     await event.edit('fbi open the door')
     await asyncio.sleep(2)
     await event.edit('hai 3 secondi per aprire la porta o la sfonderemo')
     await asyncio.sleep(3)
     await event.edit('porta sfondata con successo!')

     
client.start()
client.run_until_disconnected()