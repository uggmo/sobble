import discord
import asyncio
import random
import time
import logging
from discord import Client
from discord.ext import commands
bot = commands.Bot(command_prefix='sb')
bot.remove_command('help')
@bot.event
async def on_ready():
    print('bot is up')
    activity = discord.Activity(name='pokemon|sbhelp for help!', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)
@bot.command()
async def help(ctx):
        embed = discord.Embed(title="Help", description="Help has been delivered!", color=0x00ff00)
        embed.add_field(name="sbhelp", value="This menu is brought up", inline=False)
        embed.add_field(name="sbcalmingmusic", value="Gives you a video of calming waves.", inline=False)
        embed.add_field(name="sbhug", value="Sobble hugs you!", inline=False)
        embed.add_field(name="sbslap", value="Sobble slaps you!", inline=False)
        embed.add_field(name="sbdab", value="?????", inline=False)
        embed.add_field(name="sbwisdom", value="Random wisdom.", inline=False)
        embed.add_field(name="sbeightball", value="An 8ball function that sees the future.", inline=False)
        embed.add_field(name='sbdice [number]', value="A guessing game where you guess the dice number!", inline=False)
        embed.add_field(name='sborder [order info] [waffle]', value="Use this command to order waffles! Remember:Workers are real people too.", inline=False)
        embed.add_field(name='sbfacts', value="Tells you the facts in a debate!", inline=False)
        embed.add_field(name='sbcoinflip', value="It flips a coin.", inline=False)
        embed.add_field(name="sbjoke", value="Tells you a funny joke.", inline=False)
        embed.add_field(name="sbwater", value="I give you some water.", inline=False)
        embed.add_field(name="sbhighfive", value="High five!", inline=False)
        embed.add_field(name="sbvanish", value="Provides a vanishing GIF.", inline=False)
        embed.add_field(name="sbdance", value="Provides a dancing GIF", inline=False)
        embed.add_field(name="sbrandmeme", value="Gives you a meme out of an ever growing list", inline=False)
        embed.add_field(name="sbdrift", value="kansei dorifto!", inline=False)
        embed.add_field(name="sbeva", value="Sings the evanglion theme(or does it...)", inline=False
        await ctx.send(embed=embed)

@bot.command()
async def calmingmusic(ctx):
    await ctx.send("***https://www.youtube.com/watch?v=j5a0jTc9S10***")
@bot.command()
async def hug(ctx):
    await ctx.send("https://tenor.com/view/hug-anime-gif-11074788")
@bot.command()
async def slap(ctx):
    await ctx.send("https://tenor.com/view/slap-bears-gif-10422113")
@bot.command()
async def wisdom(ctx):
    wisdom = ["You can't get banned from a server if you follow the rules.","A sort of life is better than no life.","Some servers aren't worth going to.","Don't obsess over everything."]
    wisdomc = random.choice(wisdom)
    await ctx.send(wisdomc)
@bot.command()
async def eightball(ctx): 
        messag = ["Yes.", "It is certain", "Probably", "50/50", "There is a low probability.", "No."]
        message = random.choice(messag)
        await ctx.send(message)

@bot.command()
async def dice(ctx):
        botdice =["sbdice 1","sbdice 2","sbdice 3","sbdice 4","sbdice 5","sbdice 6"]
        botdi = random.choice(botdice)
        if message.content == botdi:
            await ctx.send("You were right! :partying_face: ")
        else:
            await ctx.send("you were wrong. :pensive:")
@bot.command()
async def joke(ctx):
        await ctx.send("Why did the chicken cross the road? It was getting to the idiot's house.")
        time.sleep(5)
        await ctx.send("Knock knock.")
        time.sleep(3)
        await ctx.send("It's the chicken.")
@bot.command()
async def facts(ctx):
    await ctx.send("https://imgur.com/a/H63R8hG")
@bot.command()
async def water(ctx):
    await ctx.send("https://tenor.com/view/sobble-water-pokemon-sword-and-shield-spit-pokemon-gif-13655946")
@bot.command()
async def highfive(ctx):
   await ctx.send("https://tenor.com/view/pokemon-sobble-high-five-hi-five-cute-gif-15450470")
@bot.command
async def coinflip():
        coin = ["Heads", "Tails"]
        coinf = random.choice(coin)
        await ctx.send(coinf)
@bot.command()
async def vanish(ctx):
    await ctx.send("https://tenor.com/view/sobble-whatever-bye-pokemon-pokemon-sword-and-shield-sword-and-shield-gif-13656059")
@bot.command()
async def dance(ctx):
    await ctx.send("https://tenor.com/view/thanos-dancing-fortnite-orange-gif-11793362")
@bot.command()
async def dab(ctx):
    await ctx.send("You asked.")
    time.sleep(1)
    await ctx.send("https://cdn.discordapp.com/attachments/385837258768515083/645685851698888704/165ouZ0gVczfHuvwCma1S96R7I0wAAAABJRU5ErkJggg.png")
@bot.command()
async def randmeme(ctx):
        meme = ["https://cdn.discordapp.com/attachments/645695800352964618/646018286504509440/ae6f07ce-085e-11ea-8da7-95ed4a38ab68.png","https://cdn.discordapp.com/attachments/645695800352964618/646018152743829514/EU-internet-meme_trans_NvBQzQNjv4BqpJliwavx4coWFCaEkEsb3pVDAZXwknrCGX2X3jMDFdw.png","https://cdn.discordapp.com/attachments/645695800352964618/646018080878624788/label-face-crowd-text-homedecor-person-human.png","https://cdn.discordapp.com/attachments/645695800352964618/646017964226904094/e0uhelxpmkm31.png", "https://i.redd.it/rwfpxonc0nz31.jpg", "https://preview.redd.it/vr89p4mf5nz31.jpg?width=640&crop=smart&auto=webp&s=98f4ec3d7e5a4c7b80c8178b5a714883cab795ad", "https://preview.redd.it/lbaosswd2oz31.jpg?width=640&crop=smart&auto=webp&s=7c5e4b6f2dcbadc7c48b0fe0078b327b40a95745", "https://preview.redd.it/bizn2l9qanz31.jpg?width=640&crop=smart&auto=webp&s=cc68cf8eb224ee6a58495e96be074b1ad844ea04", "https://preview.redd.it/bhf5et6y6oz31.jpg?width=640&crop=smart&auto=webp&s=8c03dd198478a09d1627afad3d47084153962eeb", "https://preview.redd.it/tmdhramd0nz31.jpg?width=640&crop=smart&auto=webp&s=52a4c5b04a115a478b9441d2b0a8b27cc33575c9", "https://preview.redd.it/66b0rfktlmz31.jpg?width=640&crop=smart&auto=webp&s=9893a79032204593c1177435117c8ea27ff70dcd", "https://preview.redd.it/jn7060kmwnz31.jpg?width=640&crop=smart&auto=webp&s=e66d4ccbd3b2985af35d94397ea8b1b7287e0369", "https://preview.redd.it/4j0bknoj4nz31.jpg?width=640&crop=smart&auto=webp&s=ce9de25e30f3bbdbfe2e73f2827e00ded833a055", "https://preview.redd.it/kax0nm6ycnz31.jpg?width=640&crop=smart&auto=webp&s=002c64f8d8d98dfdba74c58188abaa697fb9581d", "https://preview.redd.it/lckm8ryw9nz31.jpg?width=640&crop=smart&auto=webp&s=3a3e55fb01bd8e376a5023a1487dd105b29308b7", "https://preview.redd.it/s786dtyhsnz31.jpg?width=640&crop=smart&auto=webp&s=cf22f41f0aac182a98288abc5ce2a27fb87ece67", "https://preview.redd.it/frai7o57knz31.jpg?width=640&crop=smart&auto=webp&s=aa669a7ce9d75bf1f7799d88a3cc2fa8de19b35f", "https://preview.redd.it/qn5uczwbcnz31.jpg?width=640&crop=smart&auto=webp&s=fb0b9c3cee2280b37ac703bf54819cf05d064839", "https://i.redd.it/xbs7mcla8oz31.png", "https://external-preview.redd.it/56hO7MTgDT4zxmAxycINZ319yWXbfbpc6uBkmYQ12Aw.jpg?width=640&crop=smart&auto=webp&s=d07e4004c7f35b485ffaab67f93270adfa5dab11", "https://preview.redd.it/47xuwt4vcmz31.jpg?width=640&crop=smart&auto=webp&s=426d95aeb070dc6ece565301a0b22cb74696a5e8"]
        memes = random.choice(meme)
        await ctx.send(memes)
@bot.command()
async def drift(ctx):
        await ctx.send("...k..kansei dorifto!?!?")
        await ctx.send("https://gfycat.com/zigzagbasicblackpanther")
@bot.command()
async def evacover(ctx):
    await ctx.send("Zankoku na tenshi no you ni")
    await ctx.send("Shounen yo shinwa ni nare")
    time.sleep(2)
    await ctx.send("Yo!")
    await ctx.send("This is a story 'bout a boy named Shinji!")
    time.sleep(2)
    await ctx.send("Living in the flooded streets of New Orleans.")
    await ctx.send("Gendo, Shinji's father, is a scientist, okay")
    await ctx.send("So he built a giant robot for Shinji’s birthday!")
    time.sleep(2)
    await ctx.send("Shinji's friend Rei, knows how to bust a cap (how to bust a cap)")
    await ctx.send("When she's not fighting aliens, she's taking a nap")
    await ctx.send("Without Asuka from germany everybody would be lost, her country is responsible for the holo")
    time.sleep(3)
    await ctx.send("GRAFIC MAP!")
    await ctx.send("Shinji said, “Thanks, Daddy, can I take it for a whirl?")
    await ctx.send("And use it to help my friends save the world?")
    time.sleep(2)
    await ctx.send("Now c'mon, Shinji! Let's get this party on!")
    await ctx.send("And kick alien butt in your EVANGELION!")
    time.sleep(3)
    await ctx.send("Yo! Shinji! Get in the robot!")
    await ctx.send("Your dad loves you! Get in the robot!")
    await ctx.send("The cockpit's too small for a grownup!")
    await ctx.send("Kick some butt in your robot!")
    time.sleep(5)
    await ctx.send("Yo! Shinji! Get in the robot!")
    await ctx.send("Your friends love you! Get in the robot!")
    await ctx.send("Aliens get scared when you show up")
    await ctx.send("Kick their butt in your robot!")
    time.sleep(2)
    await ctx.send("Yo! Shinji! Get in the robot!")
    await ctx.send("It's not an EVA, it's a robot!")
    time.sleep(2)
    await ctx.send("Don't eat a rice ball, eat a donut!")
    await ctx.send("Get inside that ro-bot!")
#Moderation
@bot.command() 
async def kick(ctx, member : discord.Member, * , reason=None): 
 await member.kick(reason=reason)
 await ctx.send("GAME! That user's been kicked.")
@bot.command() 
async def mute(ctx, member : discord.Member, * , reason=None): 
 await member.mute(reason=reason)
 await ctx.send("zip! That user's been muted.")
@bot.command() 
async def unban(ctx, member : discord.Member, * , reason=None): 
 await member.unban(reason=reason)
 await ctx.send("*door opens* That user has been unbanned,")
@bot.command() 
async def ban(ctx, member : discord.Member, * , reason=None): 
 await member.mute(reason=reason)
 await ctx.send("That user's been hit with a ban hammer..")
@bot.command() 
async def unmute(ctx, member : discord.Member, * , reason=None): 
 await member.unmute(reason=reason)
 await ctx.send("unzip! That user's been unmuted")
 #Bot Business Proposals:1

bot.run('NjQ1MDA5Njc4MjI0NDU3NzQw.XdRAoQ.m2WxInCAssliDtGXt9akAp8766A')
