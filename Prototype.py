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
    if message.author == bot.user:                              # except bot's msg
        return
    
    if message.content.startswith('@hello'):                    # hello msg
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
            
    if message.content.startswith('@createstage'):              # Create Stage Channel for temporary 
        cchannel = message.channel
        msglist = message.content.split(" ")
        stage = msglist[1]
        await create_category(name = stage, *, overwrites=None, reason=None, position=None)
        await create_stage_channel(name = stage, *, topic=None, category=stage, overwrites=None, reason=None, position=None)
        await create_text_channel(name = "For_" + stage, *, overwrites=None, category=stage, reason=None, **options)
        print(f"stage channel created at {time.strftime('%X')}")
        if Voicechannel.members = None:
            await cchannel.send("No members was detected. This category will be deleted in a day.")
            time.sleep(86400)
            await voice.delete()
            await voice.delete()
            await "For_" + stage.delete()
    

    if message.content.startswith('@createvoice'):              # Create Voice Channel with its temporary msg channel
        cchannel = message.channel
        msglist = message.content.split(" ")
        voice = msglist[1]
        await create_category(name = voice, *, overwrites=None, reason=None, position=None)
        await create_stage_channel(name = voice, *, topic=None, category=voice, overwrites=None, reason=None, position=None)
        await create_text_channel(name = "For_" + voice, *, overwrites=None, category=voice, reason=None, **options)
        print(f"text channel created at {time.strftime('%X')}")
        if Voicechannel.members = None:
            await cchannel.send("No members was detected. This category will be deleted in a day.")
            time.sleep(86400)
            await voice.delete()
            await voice.delete()
            await "For_" + voice.delete()


bot.run('')