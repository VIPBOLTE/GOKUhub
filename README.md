``` python

import asyncio, os, time, aiohttp
import aiohttp
from pyrogram import filters
from GOKUhub import GOKUhub as papagoku
from GOKUMUSIC import app

@app.on_message(filters.command("GOKUhub"))
async def GOKUhub(_, message):
    text = message.text[len("/GOKUhub") :]
    papagoku(f"{text}").save(f"GOKUhub_{message.from_user.id}.png")
    await message.reply_photo(f"GOKUhub_{message.from_user.id}.png")
    os.remove(f"GOKUhub_{message.from_user.id}.png")

```
``` python
 pip install GOKUhub

```




# GOKUHUB 


![Project Image](https://github.com/VIPBOLTE/GOKUhub/blob/main/out.png)

