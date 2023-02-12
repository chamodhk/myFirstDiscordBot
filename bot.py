import discord
import pyjokes
from bs4 import BeautifulSoup
import requests
import nest_asyncio
nest_asyncio.apply()
import os 


token = os.getenv('token')
client = discord.Client(intents = discord.Intents.all())

url = "http://www.meteo.gov.lk/index.php?lang=en"
html = requests.get(url).text

soup = BeautifulSoup(html)
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
  if message.content.startswith("!") or "bot" in message.content:
    if "hello" in message.content:
      await message.channel.send("Hello "+message.author.name+"!")
    if "weather" in message.content:

      await message.channel.send("Getting weather info....")

      url ="http://www.meteo.gov.lk/index.php?lang=en"


      html = requests.get(url).text
      await message.channel.send("processing......")
      soup = BeautifulSoup(html)

      out ="\n"

      forecast = soup.find("div",class_="article_anywhere")
      forecasts = forecast.findChildren("p")

      for forecast in forecasts:
        out = out + forecast.text +"\n"
      await message.channel.send(out)

    if "news" in message.content:
      url = "https://sinhala.newsfirst.lk/latest"
      await message.channel.send(f"getting the latest from {url}")

      html = requests.get(url).text

      soup = BeautifulSoup(html)

      news = soup.find_all("h4")

      out =""

      for id, new in enumerate(news):
        out += f"{id+1}. {new.text} \n"



      await message.channel.send(out)

    if "joke" in message.content:
      joke = pyjokes.get_joke()
        
      await message.channel.send(joke)

client.run(token)
