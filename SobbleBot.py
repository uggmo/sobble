import discord
import asyncio
import random
import time
from discord import Client
from discord.ext import commands
Client: Client = discord.Client()
bot = commands.Bot(command_prefix='sb')
@Client.event
async def on_ready():
    print('bot is up')
    await Client.change_presence(activity=discord.Game(name='sbhelp|Being a sobble'))

@Client.event
async def on_message(message):
    if message.author == Client.user:
        return
    if message.content.startswith("sbhello"):
        await message.channel.send("Hi :wave:")
    if message.content.startswith("sbhelp"):
        embed = discord.Embed(title="Help", description="Page 1 of 2, use sbhelp2 for the rest of the commands!", color=0x00ff00)
        embed.add_field(name="sbhelp", value="This menu is brought up", inline=False)
        embed.add_field(name="sbcalmingmusic", value="Gives you a video of calming waves.", inline=False)
        embed.add_field(name="sbhug", value="Sobble hugs you!", inline=False)
        embed.add_field(name="sbslap", value="Sobble slaps you!", inline=False)
        embed.add_field(name="sbdab", value="?????", inline=False)
        embed.add_field(name="sbwisdom", value="Random wisdom.", inline=False)
        embed.add_field(name="sb8ball", value="An 8ball function that sees the future.", inline=False)
        embed.add_field(name='sbdice [number]', value="A guessing game where you guess the dice number!", inline=False)
        embed.add_field(name='sborder [order info] [waffle]', value="Use this command to order waffles! Remember:Workers are real people too.", inline=False)
        embed.add_field(name='sbfacts', value="Tells you the facts in a debate!", inline=False)
        embed.add_field(name='sbcoinflip', value="It flips a coin.", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("sbhelp2"):
        embed = discord.Embed(title="Help 2", description="Even more help!",colour=0x00ff00)
        embed.add_field(name="sbjoke", value="Tells you a funny joke.", inline=False)
        embed.add_field(name="sbwater", value="I give you some water.", inline=False)
        embed.add_field(name="sbhighfive", value="High five!", inline=False)
        embed.add_field(name="sbvanish", value="Provides a vanishing GIF.", inline=False)
        embed.add_field(name="sbdance", value="Provides a dancing GIF", inline=False)
        embed.add_field(name="sbmeme", value="Gives you a meme", inline=False)
    if message.content.startswith("sbcalmingmusic"):
        await message.channel.send("***https://www.youtube.com/watch?v=j5a0jTc9S10***")
    if message.content.startswith("sbhug"):
        await message.channel.send("https://tenor.com/view/hug-anime-gif-11074788")
    if message.content.startswith("sbslap"):
        await message.channel.send("No, I don't think I will.")
    if message.content.startswith("sbwisdom"):
        wisdom = ["You can't get banned from a server if you follow the rules.","A sort of life is better than no life.","Some servers aren't worth going to.","Don't obsess over everything."]
        wisdomc = random.choice(wisdom)
        await message.channel.send(wisdomc)
    if message.content.startswith("sb8ball"):
        messag = ["Yes.", "It is certain", "Probably", "50/50", "There is a low probability.", "No."]
        message = random.choice(messag)
        await message.channel.send(message)
    if message.content.startswith("sbdice"):
        botdice =["sbdice 1","sbdice 2","sbdice 3","sbdice 4","sbdice 5","sbdice 6"]
        botdi = random.choice(botdice)
        if botdi == message.content:
            await message.channel.send("Your guess was right! +5 internet points! :sunglasses:")
        else:
            await message.channel.send("Your guess was...wrong. :pensive:")
    if message.content.startswith("sbjoke"):
        await message.channel.send("Why did the chicken cross the road? It was getting to the idiot's house.")
        time.sleep(5)
        await message.channel.send("Knock knock.")
        time.sleep(3)
        await message.channel.send("It's the chicken.")
    if message.content.startswith('sborder'):
        if "waffle" in message.content.lower():
          query = message.content
          stopwords = ['sborder']
          querywords = query.split()
          resultwords = [word for word in querywords if word.lower() not in stopwords]
          info= ' '.join(resultwords)      
          InviteLink = await message.channel.create_invite(max_age=0, max_uses=0, reason=None, unique=True, temporary=True)
          embed = discord.Embed(title="New Order!", description=info, colour=0x00ff00)
          embed.add_field(name="Orderer", value=message.author, inline=False)
          embed.add_field(name="Invite", value=InviteLink, inline=False)
          channel = Client.get_channel(645259977304571935)
          await channel.send(embed=embed)
          embed2 = discord.Embed(title="Order Sent!", description="Your order has been sent to the kitchen.", inline=False, colour=0x206694)
          embed2.add_field(name="Order Information", value=info, inline=False)
          embed2.add_field(name="Orderer", value=message.author, inline=False)
          await message.channel.send(embed=embed2)
        else:
          await message.channel.send("Sorry, we don't cook anything. It has to be a waffle.")
    if message.content.startswith("sbfacts"):
          await message.channel.send("https://imgur.com/a/H63R8hG")
    if message.content.startswith("sbwater"):
        await message.channel.send("https://tenor.com/view/sobble-water-pokemon-sword-and-shield-spit-pokemon-gif-13655946")
    if message.content.startswith("sbhighfive"):
        await message.channel.send("https://tenor.com/view/pokemon-sobble-high-five-hi-five-cute-gif-15450470")
    if message.content.startswith("sbcoinflip"):
        coin = ["Heads", "Tails"]
        coinf = random.choice(coin)
        await message.channel.send(coinf)
    if message.content.startswith("sbvanish"):
        await message.channel.send("https://tenor.com/view/sobble-whatever-bye-pokemon-pokemon-sword-and-shield-sword-and-shield-gif-13656059")
    if message.content.startswith("sbdance"):
        await message.channel.send("https://tenor.com/view/thanos-dancing-fortnite-orange-gif-11793362")
    if message.content.startswith("sbdab"):
        await message.channel.send("You asked for this. https://cdn.discordapp.com/attachments/385837258768515083/645685851698888704/165ouZ0gVczfHuvwCma1S96R7I0wAAAABJRU5ErkJggg.png")
    if message.content.startswith("sbmeme"):
        meme = ["https://cdn.discordapp.com/attachments/645695800352964618/646018286504509440/ae6f07ce-085e-11ea-8da7-95ed4a38ab68.png","https://cdn.discordapp.com/attachments/645695800352964618/646018152743829514/EU-internet-meme_trans_NvBQzQNjv4BqpJliwavx4coWFCaEkEsb3pVDAZXwknrCGX2X3jMDFdw.png","https://cdn.discordapp.com/attachments/645695800352964618/646018080878624788/label-face-crowd-text-homedecor-person-human.png","https://cdn.discordapp.com/attachments/645695800352964618/646017964226904094/e0uhelxpmkm31.png"]
        memes = random.choice(meme)
        await message.channel.send(memes)

@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
 await member.kick(reason=reason)
@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
 await member.ban(reason=reason)
@bot.command()
async def mute(ctx, member : discord.Member, *, reason="Because you don't stop talking!"):
 await member.mute(reason=reason)
@bot.command()
async def unban(ctx, member : discord.Member, *, reason="You're really a good guy!"):
 await member.unban(reason=reason)
@bot.command()
async def unmute(ctx, member : discord.Member, *, reason="because you're good again"):
 await member.unmute(reason=reason)
Client.run('NjQ1MDA5Njc4MjI0NDU3NzQw.XdA44A.8SJbnevk1aTsiKfJB0IIF8qvJWY')

