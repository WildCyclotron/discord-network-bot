import discord
import os
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
from discord_webhook import DiscordWebhook
import aiohttp

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+')

@bot.event
async def on_ready():
  print('Bot started...')

"""Let's name the two servers as Server 1 and Server 2.

We will be connecting #channel_1 of server 1 with the #channel_2 of the server 2.

"""


@bot.event
async def on_message(message):
  
  if message.channel.id == '#channel_1 id':
    await bot.process_commands(message)
    async with aiohttp.ClientSession() as session:
      user = message.author

      usernam = str(user)
      username = usernam[:-5] #to remove the tag      

      webhook = Webhook.from_url('#channel_2 webhook url', adapter=AsyncWebhookAdapter(session))
      if message.webhook_id:
        return

      elif message.attachments:
        list = message.attachments
        s = list[0]
        s = str(s)
        index = s.index('https://')
        s = s[index:-2]
        if message.content:
          await webhook.send(message.content, username=username,avatar_url= user.avatar_url)
        await webhook.send(s, username=username,avatar_url= user.avatar_url)
      else:
        await webhook.send(message.content, username=username,avatar_url= user.avatar_url)
    
  elif message.channel.id == '#channel_2 id':
    await bot.process_commands(message)
    async with aiohttp.ClientSession() as session:
      user = message.author

      usernam = str(user)
      username = usernam[:-5]      

      webhook = Webhook.from_url('#channel_1 webhook url', adapter=AsyncWebhookAdapter(session))
      if message.webhook_id:
        return
      
      elif message.attachments:
        list = message.attachments
        s = list[0]
        s = str(s)
        index = s.index('https://')
        s = s[index:-2]
        if message.content:
          await webhook.send(message.content, username=username,avatar_url= user.avatar_url)
        await webhook.send(s, username=username,avatar_url= user.avatar_url)
      else:
        await webhook.send(message.content, username=username,avatar_url= user.avatar_url)
      


  else:
    await bot.process_commands(message) #to process commands 
    
    
    
    
    
    
    
 bot.run('token')


  
