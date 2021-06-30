import discord
from discord.ext import commands
import nest_asyncio
import time 
nest_asyncio.apply()
 
bot = commands.Bot(command_prefix='0_<')
TOKEN = ''

@bot.event
async def on_ready():
    print(bot.user.name, 'has woken up.')                       # To check bot run
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Greeting'))
    
@bot.event
async def message_react(message):
<<<<<<< HEAD
    if message.author == bot.user:                              # except bot's msg
        return
    
    if message.content.startswith('@hello'):                    # hello msg
=======
    if message.author == bot.user:
        return
    
    if message.content.startswith('@hello'):
>>>>>>> dc8fa7a1a65fa08adb8f53e1c058bee399e522d7
        cchannel = message.channel                              # cchannel = current channel
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
        except:
            await cchannel.send(":thinking:")
            
<<<<<<< HEAD
    if message.content.startswith('@createstage'):              # Create Stage Channel for temporary 
=======
    if message.content.startswith('@createstage'):
>>>>>>> dc8fa7a1a65fa08adb8f53e1c058bee399e522d7
        cchannel = message.channel
        msglist = message.content.split(" ")
        stage = msglist[1]
        await create_category(name = stage, *, overwrites=None, reason=None, position=None)
<<<<<<< HEAD
        await create_stage_channel(name = stage, *, topic=None, category=stage, overwrites=None, reason=None, position=None)
        await create_text_channel(name = "For_" + stage, *, overwrites=None, category=stage, reason=None, **options)
        if Voicechannel.members = None:
            await cchannel.send("No members detected. This category will be deleted in a day.")
            time.sleep(86400)
            await voice.delete()
            await voice.delete()
            await "For_" + stage.delete()
    
=======
        await create_stage_channel(name = stage , *, topic=None, category=stage, overwrites=None, reason=None, position=None)
        await create_text_channel(name = "For_" + stage, *, overwrites=None, category=stage, reason=None, **options)
    if Voicechannel.members = "":
        await cchannel.send("No members has been detected. This category will be deleted in a day.")

>>>>>>> dc8fa7a1a65fa08adb8f53e1c058bee399e522d7

    if message.content.startswith('@createvoice'):              # Create Voice Channel with its temporary msg channel
        cchannel = message.channel
        msglist = message.content.split(" ")
        voice = msglist[1]
        await create_category(name = voice, *, overwrites=None, reason=None, position=None)
        await create_stage_channel(name = voice, *, topic=None, category=voice, overwrites=None, reason=None, position=None)
        await create_text_channel(name = "For_" + voice, *, overwrites=None, category=voice, reason=None, **options)
        if Voicechannel.members = None:
            await cchannel.send("No members detected. This category will be deleted in a day.")
            time.sleep(86400)
            await voice.delete()
            await voice.delete()
            await "For_" + voice.delete()


<<<<<<< HEAD
bot.run('')
=======
<<<<<<< HEAD
bot.run('')
=======
bot.run('')
>>>>>>> 210480b9124afa2018019cdc27757105157c3fd8
>>>>>>> dc8fa7a1a65fa08adb8f53e1c058bee399e522d7
