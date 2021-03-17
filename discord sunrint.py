import discord
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse
import re

client = discord.Client()

res = req.urlopen('http://sunrint.hs.kr/index.do')
soup = BeautifulSoup(res, 'html.parser')
tag = soup.find('div', attrs={'class': 'ellipsis'}).get_text()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game =  discord.Game("선린인터넷고 홈페이지 읽기")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!선린"):
        await message.channel.send("게시물 제목 : " + tag, tts = True)

client.run("ODEzODI2MTExMjU0NDI5NzY3.YDU8oQ.vKVyy-NbSJNA8KdxbP-gRraoPGw")