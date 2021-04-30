import discord
from discord.ext import commands
import nest_asyncio
nest_asyncio.apply()
 
bot = commands.Bot(command_prefix='0_<')
TOKEN = 'ODI1Mzg0NTMwODE4MjM2NDI3.YF9JPw.zaevLZt9IL1u2eo8oK3-MybZvOs'

@bot.event
async def on_ready():
    print(bot.user.name, 'has woken up.')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Greeting'))
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('@hello'):
        cchannel = message.channel   #current channel
        await cchannel.send('Hello World!')
        
        def check(m):
            return m.content == 'hello' and m.channel == cchannel

        msg = await bot.wait_for('message', check=check)
        await cchannel.send('Hello {.author}!'.format(msg))


    if message.content.startswith('$emoji'):
        cchannel = message.channel
        await cchannel.send(':thinking:')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == ':thinking:'

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=10.0, check=check)



bot.run('ODI1Mzg0NTMwODE4MjM2NDI3.YF9JPw.zaevLZt9IL1u2eo8oK3-MybZvOs')