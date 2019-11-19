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
        embed = discord.Embed(title="Help", description="Help has been delivered!", color=0x00ff00)
        embed.add_field(name="sbhelp", value="This menu is brought up", inline=False)
        embed.add_field(name="sbcalmingmusic", value="Gives you a video of calming waves.", inline=False)
        embed.add_field(name="sbhug", value="Sobble hugs you!", inline=False)
        embed.add_field(name="sbslap", value="Sobble slaps you!", inline=False)
        embed.add_field(name="sbdab", value="?????", inline=False)
        embed.add_field(name="sbwisdom", value="Random wisdom.", inline=False)
        embed.add_field(name="sb8ball", value="An 8ball function that sees the future.", inline=False)
        embed.add_field(name='sbdice [number]', value="A guessing game where you guess the dice number!", inline=False)
        
        embed.add_field(name='sbfacts', value="Tells you the facts in a debate!", inline=False)
        embed.add_field(name='sbcoinflip', value="It flips a coin.", inline=False)
        embed.add_field(name="sbjoke", value="Tells you a funny joke.", inline=False)
        embed.add_field(name="sbwater", value="I give you some water.", inline=False)
        embed.add_field(name="sbhighfive", value="High five!", inline=False)
        embed.add_field(name="sbvanish", value="Provides a vanishing GIF.", inline=False)
        embed.add_field(name="sbdance", value="Provides a dancing GIF", inline=False)
        embed.add_field(name="sbmeme", value="Gives you a meme", inline=False)
        await message.channel.send(embed=embed)
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
@bot.command(name='sbyeet')
    await ctx.send('No,I am yeet!')
Client.run('NjQ1MDA5Njc4MjI0NDU3NzQw.XdLw1w.0zeMhBp6Wk7jQhO4F3B8AJgTZ7A')

