#!/usr/bin/python
# encoding: utf-8\


import aiohttp
import asyncio
import requests
import discord
from discord.ext import commands
from discord.ui import View, Button
import random
from discord_components import Button, Select, SelectOption, ComponentsBot
import time
import os
import json

#Token
TOKEN = "ODgxMzA5NjE1MzY1NjkzNDUy.Gm7YqU.R8DyTW6-hycjSa9YYO7Wz0C6JHqqv-UPlZKkOA"


#Prefix
bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())
bot.remove_command("help")


#Event functions
def randomize_letters(string: str) -> str:
    letters = [c for c in string if c.isalpha()]
    random.shuffle(letters)

    randomized = [letters.pop() if c.isalpha() else c for c in string]
    return "".join(randomized)

API_KEY_DALLE = 'd1ea449b-702e-40a9-9c48-16323de1b833'
url_dalle = 'https://api.deepai.org/api/text2img'
channelForAnswers = 000000000

#commands


@bot.event
async def on_message(message):
    msg = message.content
    if "евре".upper() in msg.upper():
        await message.add_reaction("🔥")
    elif "хулиганч".upper() in msg.upper():
        await message.add_reaction("🔥")
    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f"** {ctx.author.name}, the command doesn't exist**", color = discord.Colour.from_rgb(235, 64, 52)))
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, you do not have permissions**', color = discord.Colour.from_rgb(235, 64, 52)))
    
@bot.event
async def on_member_join(member):
    guild = bot.get_guild(881312815820980274)
    channel = bot.get_channel(881312815820980277)
    embedHey = discord.Embed(title = f"Welcome! Glad to see you here {member} <:anakinLove:999682658579787858>", color = discord.Colour.from_rgb(102, 3, 252))
    await channel.send(embed=embedHey)
    role = guild.get_role(881556162296836187)
    await member.add_roles(role)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(881312815820980277)
    await channel.send(f"{member} left.")



serverLink = "https://discord.gg/fK7wDDHX"

@bot.command()
async def deletech(ctx):
    await ctx.send(f"**Attacking TARGET:** `457952082121457685`\n__The URL:__ {serverLink}\n__Type of attack:__ **Deleting channels...**")

@bot.command()
async def deleterl(ctx):
    await ctx.send(f"**Attacking TARGET:** `457952082121457685`\n__The URL:__ {serverLink}\n__Type of attack:__ **Deleting roles...**")

@bot.command()
async def change(ctx, *, server_nickname):
    await ctx.send(f"**Attacking TARGET:** `457952082121457685`\n__The URL:__ {serverLink}\n__Type of attack:__ **Changing nickname + server avatar for {server_nickname}**")

@bot.command()
async def createrl(ctx):
    await ctx.send(f"**Attacking TARGET:** `457952082121457685`\n__The URL:__ {serverLink}\n__Type of attack:__ **Creating roles...**")

@bot.command()
async def createch(ctx):
    await ctx.send(f"**Attacking TARGET:** `457952082121457685`\n__The URL:__ {serverLink}\n__Type of attack:__ **Creating channels...**")



@bot.command()
async def color(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.post('https://api.deepai.org/api/colorizer', data={'image': ctx.message.attachments[0].url,}, headers={'api-key': 'd1ea449b-702e-40a9-9c48-16323de1b833'}) as response:
            html = await response.json()
    endEmbed = discord.Embed(title="**Colored image**", color = discord.Colour.from_rgb(102, 3, 252))
    endEmbed.set_image(url=html['output_url'])
    endEmbed.set_footer(text=f"by {ctx.author.name}")
    await ctx.send(embed=endEmbed)



@bot.command()
async def help(ctx, arg=None):
    if arg == None:
        embed=discord.Embed(title="**Unable commands:**", description="You can get more detailed help about each command by entering its name. \n For example: `help neural networks`", color=0x6603fc)
        embed.add_field(name="Neural Networks 🧠", value="`dalle` `deepdream` `imagemix` `color`", inline=False)
        embed.add_field(name="Moderation ⚔️", value=" `clear` `giverole` `removerole` `kick` `ban` `unban` `multiban` `multikick` `slowmode` ", inline=False)
        embed.add_field(name="Utilities 🥢", value="`avatar` `dm` `publicate` `send` `vanga` `se`", inline=False)
        embed.add_field(name="Economy 🎰", value="`balance` `slut` `dep` `with` `cash` `rob`", inline=False)
        embed.set_footer(text="EvreiBot © 2022 All rights reserved ")
        await ctx.send(embed=embed)




@bot.command()
async def imagemix(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.post('https://api.deepai.org/api/fast-style-transfer', data={'content': ctx.message.attachments[0].url, 'style': ctx.message.attachments[1].url,}, headers={'api-key': 'd1ea449b-702e-40a9-9c48-16323de1b833'}) as response:
            html = await response.json()
    endEmbed = discord.Embed(title="**Image mix**", color = discord.Colour.from_rgb(102, 3, 252))
    endEmbed.set_image(url=html['output_url'])
    endEmbed.set_footer(text=f"by {ctx.author.name}")
    await ctx.send(embed=endEmbed)




@bot.command()
async def rules(ctx):
    embed=discord.Embed(title="**<:verify:999621337075171368> Основные правила сервера**", color=0x6703fc)
    embed.add_field(name="⠀", value="`1.` Запрещены оскорбления участников, наций и Т.Д.", inline=False)
    embed.add_field(name="⠀", value="`2.` Запрещена **агрессивная** политика.", inline=False)
    embed.add_field(name="⠀", value="`3.` ~~Запрещен расизм~~ Я переезжал Джорджа Флойда катком нахуй.", inline=False)
    embed.add_field(name="⠀", value="`4.` Мат не запрещается, но рекомендуется использовать его в небольших количествах.", inline=False)
    embed.add_field(name="⠀", value="`5.` Запрещен пиар без разрешения администрации. ", inline=False)
    embed.add_field(name="⠀", value="`6.` Запрещено злоупотреблять пингами.", inline=False)
    embed.add_field(name="⠀", value="`7.` Адекватность приветствуется.", inline=False)
    embed.add_field(name="⠀", value="`8.` Если у вас есть идея для сервера/бота, `!idea текст идеи` для рассмотрения в <#969908226873249842>", inline=False)
    embed.add_field(name="⠀", value="`9.` Все члены сообщества равны в исполнении правил.", inline=False)
    embed.add_field(name="⠀", value="`10.` За конфликт в чате будут наказаны все участники.", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def dalle(ctx, *, promt):
    channel = bot.get_channel(999749828689023016)
    await ctx.send(f"Start creating image for promt **{promt}**")
    async with aiohttp.ClientSession() as session:
        async with session.post('https://api.deepai.org/api/text2img', data={'text': promt,}, headers={'api-key': 'd1ea449b-702e-40a9-9c48-16323de1b833'}) as response:
            html = await response.json()
            endEmbed = discord.Embed(title=f"Created image from promt: ", description=f"**{promt}**", color = discord.Colour.from_rgb(102, 3, 252))
            endEmbed.set_image(url=html['output_url'])
            endEmbed.set_footer(text=f"by {ctx.author.name}")
            await ctx.send(embed=endEmbed)
    await channel.send(f"{ctx.author.mention}: **{promt}**")



@bot.command()
async def deepdream(ctx, *, image):
    async with aiohttp.ClientSession() as session:
        async with session.post('https://api.deepai.org/api/deepdream', data={'image': image,}, headers={'api-key': 'd1ea449b-702e-40a9-9c48-16323de1b833'}) as response:
            html = await response.json()
    await ctx.send(html['output_url'])



@bot.command()
@commands.has_permissions(manage_roles = True)
async def giverole(ctx, user : discord.Member, role : discord.Role):
    av = ctx.author.avatar
    if role in user.roles:
        givrole = discord.Embed(description = f"**Role already added**", color = discord.Colour.from_rgb(235, 64, 52))
        givrole.set_author(name=f"Staff: {ctx.author.name}", icon_url=av)
        await ctx.send(embed=givrole)
    else:
        givrole = discord.Embed(description = f"**{role.mention} added for {user.mention}**", color = discord.Colour.from_rgb(51, 245, 84))
        givrole.set_author(name=f"Staff: {ctx.author.name}", icon_url=av)
        await user.add_roles(role)
        await ctx.send(embed=givrole)

@bot.command()
@commands.has_permissions(manage_roles = True)
async def removerole(ctx, user : discord.Member, role : discord.Role):
    av = ctx.author.avatar
    if role in user.roles:
        await user.remove_roles(role)
        remrole = discord.Embed(description = f"**{role.mention} removed from {user.mention}**", color = discord.Colour.from_rgb(51, 245, 84))
        remrole.set_author(name=f"Staff: {ctx.author.name}", icon_url=av)
        await ctx.send(embed=remrole)
    else:
        remrole = discord.Embed(description = f"**Role already removed**", color = discord.Colour.from_rgb(235, 64, 52))
        remrole.set_author(name=f"Staff: {ctx.author.name}", icon_url=av)
        await ctx.send(embed=remrole)



@bot.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def clear (ctx, amount = 0):
    av = ctx.author.avatar
    time.sleep(0.1)
    if amount <= 0:
        nonpurg = discord.Embed(title = "Please enter a valid number", color = discord.Colour.from_rgb(235, 64, 52))
        nonpurg.set_author(name=f"Staff: {ctx.author.name}", icon_url=av)
        await ctx.send(embed=nonpurg)
    elif amount > 0:
        await ctx.message.delete()
        purg = discord.Embed(title=f"{amount} messages deleted", color = discord.Colour.from_rgb(51, 245, 84))
        purg.set_author(name=f"Staff: {ctx.author.name}", icon_url=av)
        await ctx.channel.purge(limit = amount)
        await ctx.send(embed=purg)


@bot.command()
async def se(ctx, emoji : discord.Emoji):
    await ctx.send(f"**Take your emoji** {emoji.url}")


@bot.command()
async def goose(ctx):
    eb = discord.Embed(title=f":swan: Test embed", description=f"fuck the system, fuck the geese")
    await ctx.send(embed=eb)







@commands.has_permissions(ban_members=True)
@bot.command()
async def ban(ctx, member : discord.Member, *, reason="No reason provided"):
    try:
        await member.ban(reason=reason)
        av = ctx.author.avatar
        ban = discord.Embed(title=f"{member} banned. Reason: {reason}", color = discord.Colour.from_rgb(51, 245, 84))
        ban.set_author(name=f"Staff: {ctx.author.name}", icon_url=av)
        await ctx.channel.send(embed=ban)
    except:
        nonban = discord.Embed(title = "User is not found", color = discord.Colour.from_rgb(235, 64, 52))
        nonban.set_author(name=f"Staff: {ctx.author.name}", icon_url=av)
        await ctx.channel.send(embed=nonban)



@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, member : discord.Member, *, reason="No reason provided"):
    av = ctx.author.avatar
    try:
        await member.kick(reason=reason)
        kick = discord.Embed(title=f"{member} kicked. Reason: {reason}", color = discord.Colour.from_rgb(51, 245, 84))
        kick.set_author(name=f"Staff: {ctx.author.name}", icon_url=av)
        await ctx.channel.send(embed=kick)
    except:
        nonkick = discord.Embed(title = "User is not found", color = discord.Colour.from_rgb(235, 64, 52))
        nonkick.set_author(name=f"Staff: {ctx.author.name}", icon_url=av)
        await ctx.channel.send(embed=nonkick)


@bot.command()
async def vanga(ctx):
    rnd = random.randint(1, 14)
    if rnd == 1:
        phrase = "Подъём, ебаный самурай!"
    elif rnd == 2:
        phrase = "Раз тебе нужна особая жратва, шли нахуй официантку и иди сразу к повару"
    elif rnd == 3:
        phrase = "Чего тебя сегодня так накрыло, а?"
    elif rnd == 4:
        phrase = "Не могу ответить на этот вопрос. Обратитесь к моему юристу"
    elif rnd == 5:
        phrase = "Ебать мой лысый хуй, это и в правду интересно"
    elif rnd == 6:
        phrase = "Не хочу показаться грубым, но я всё это в рот ебал"
    elif rnd == 7:
        phrase = "Посмотри на меня, видишь? Видишь это выражение неудивления на моем лице?"
    elif rnd == 8:
        phrase = "Аллилуйя! Началось хоть что-то интересное. Сейчас ещё бы попкорна, и было бы вообще заебись"
    elif rnd == 9:
        phrase = "Я как подумаю, на сколько здесь темно... У меня сразу на лбу, которого нет, выступает пот, блять, которого я не выделяю"
    elif rnd == 10:
        phrase = "Всё, что мы можем получить здесь, так это пизды, причём в плохом смысле"
    elif rnd == 11:
        phrase = "Знаешь, Ви, походу над тобой попросту издеваются. Спорим, все эти точки на карте складываются в один огромный философический хуй?"
    elif rnd == 12:
        phrase = "Если бы я был предсказателем, я бы не оказался ёбаным чипом в голове живого трупа"
    elif rnd == 13:
        phrase = "От лица мотеля Свободная Калифорния... Желаю вам, блядь, приятных сноведений"
    await ctx.message.delete()
    await ctx.channel.send(phrase)



'''
@bot.command()
async def prediction(ctx, *, message:str):
    predictionEmb = discord.Embed(title = "Если бы я был предсказателем, я бы не оказался ёбаным чипом в голове живого трупа", description = f"{message}", color = discord.Colour.from_rgb(91, 45, 227))
    await ctx.send(embed=predictionEmb)
    #Доделать Embed
'''


@bot.command()
async def dm(ctx, user: discord.Member, *, message:str):
    av = ctx.author.avatar
    await ctx.message.delete()
    msgforuser = discord.Embed(title = f":shield: Security message from {ctx.author}", description = message, color = discord.Colour.from_rgb(51, 103, 245))
    msgforuser.set_author(name=f"Sender: {ctx.author.name}", icon_url=av)
    await user.send(embed=msgforuser)




@bot.command()
async def guilds(ctx):
    if ctx.author.id == 591203412385988609:
        await ctx.send(bot.guilds)






@commands.has_permissions(ban_members=True)
@bot.command()
async def unban(ctx, id):
    user = await bot.fetch_user(id)
    try:
        await ctx.guild.unban(user)
        await ctx.send(embed=discord.Embed(title=f":candle: Unbanned {user.name} by {ctx.author}", color = discord.Colour.from_rgb(51, 245, 84)))
    except:
        await ctx.send(embed=discord.Embed(title=f"User not banned", color = discord.Colour.from_rgb(235, 64, 52)))


@commands.has_permissions(manage_messages=True)
@bot.command()
async def publicate(ctx, ttl, message):
    av = ctx.author.avatar
    await ctx.message.delete()
    pblcemb = discord.Embed(title=ttl, description=message, color=discord.Colour.from_rgb(244, 247, 49))
    pblcemb.set_author(name=f"Broadcaster: {ctx.author.name}", icon_url=av)
    await ctx.send(embed=pblcemb)



@bot.command()
async def sh(ctx, *, content):
    await ctx.message.delete()
    channel = bot.get_channel(977492885891072050)
    if ctx.channel.id == 977268215522660362:
        await channel.send(f"Author: {ctx.author.mention} | {ctx.author.id}\nContent: {content}")
        await ctx.send(embed=discord.Embed(title=f'Спасибо, {ctx.author.name}! <:Love:977467786194452492>', description=f'Заявка с ответами на мероприятие "Поиск слов" рассматривается организаторами ивента прямо сейчас <:Bluush:977565989627645974>', color = discord.Colour.from_rgb(210, 105, 30)))
    else:
        await ctx.send(f"Используй только #┋🎉┋розыгрыши для ответов")

@bot.command()
@commands.has_any_role("Events MC")
async def eventpart(ctx, member : discord.Member):
    await ctx.message.delete()
    role = ctx.guild.get_role(977552543884402728)
    await member.add_roles(role)
    await ctx.send(f"{member.mention} становится участником")


@bot.command()
@commands.has_any_role("Events MC")
async def eventrempart(ctx, member : discord.Member):
    await ctx.message.delete()
    role = ctx.guild.get_role(977552543884402728)
    await member.remove_roles(role)
    await ctx.send(f"{member.mention} больше не участник")


@bot.command()
async def avatar(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author
    userAvatar = member.display_avatar
    avatarEmbed = discord.Embed(title = f"{member.name}'s avatar", color = discord.Colour.gold())
    avatarEmbed.set_image(url=userAvatar)
    avatarEmbed.set_author(name=f"Requester: {ctx.author.name}", icon_url=ctx.author.display_avatar)
    await ctx.send(embed=avatarEmbed)





@bot.command()
async def iqtest(ctx):
    await ctx.send("Enter your IQ: ")
    iq = await bot.wait_for("message", timeout=100000)
    await ctx.send("Pay $1")
    ch = await bot.wait_for("message", timeout=100000)
    await ctx.send(f"Congratulations, your IQ equals {iq.content}")



@commands.has_permissions(manage_channels=True)
@bot.command()
async def slowmode(ctx, seconds : int):
    if seconds < 0:
        await ctx.send(embed=discord.Embed(title=f"**Enter correct value**", color = discord.Colour.from_rgb(235, 64, 52)))
    elif seconds > 21600:
        await ctx.send(embed=discord.Embed(title=f"**Enter a value less than __21600__**", color = discord.Colour.from_rgb(235, 64, 52)))
    else:
        await ctx.channel.edit(slowmode_delay=seconds)
        if (seconds >= 3600):
            await ctx.send(f"⌚ Slowmode set to {seconds} seconds. ({seconds/3600} hours)")
        else:
            await ctx.send(f"⌚ Slowmode set to {seconds} seconds. ({seconds/60} minutes)")



@bot.command()
async def send(ctx, *, message):
    channel = bot.get_channel(998732205184536646)
    if "@everyone" in message:
        await ctx.send(f"Get the fuck out of here {ctx.author.mention}")
        await channel.send(f"{ctx.author.mention} попытался сказать: **{message}**")
    elif "@member" in message:
        await ctx.send(f"Get the fuck out of here {ctx.author.mention}")
        await channel.send(f"{ctx.author.mention} попытался сказать: **{message}**")
    elif "@here" in message:
        await ctx.send(f"Get the fuck out of here {ctx.author.mention}")
        await channel.send(f"{ctx.author.mention} попытался сказать: **{message}**")
    else:
        await ctx.message.delete()
        await ctx.send(message)
        await channel.send(f"{ctx.author.mention} сказал: **{message}**")




@bot.command()
@commands.has_any_role("Events MC")
async def scrabble(ctx, phrase, scrnum, channel : discord.TextChannel, language):
    await ctx.message.delete()
    final_phrase = phrase
    def check(m):
        return m.content.lower() == final_phrase.lower()
    phrase = randomize_letters(phrase).split()
    ballsforquest = 0
    wordscount = len(phrase)
    if (wordscount == 2):
        bl_circle = random.randint(1, len(phrase[0])) 
        rd_circle = random.randint(1, len(phrase[1]))
        bl_circle = bl_circle-1
        rd_circle = rd_circle-1
        phrase[0] = phrase[0][:bl_circle] + "🔵" + phrase[0][bl_circle+1:]
        phrase[1] = phrase[1][:rd_circle] + "🔴" + phrase[1][rd_circle+1:]
        ballsforquest = 1
        wrdballsforquest = "балл"
        if language == "rus":
            lastPhrase = "🔵 - 🔴 пропуски букв, для соответствующих слов"
        elif language == "eng":
            lastPhrase = "**🔵 & 🔴 are blanks for the respective words**"
    elif (wordscount == 3):
        bl_circle = random.randint(1, len(phrase[0])) 
        rd_circle = random.randint(1, len(phrase[1]))
        grn_circle = random.randint(1, len(phrase[2]))
        bl_circle = bl_circle-1
        rd_circle = rd_circle-1
        grn_circle = grn_circle-1
        phrase[0] = phrase[0][:bl_circle] + "🔵" + phrase[0][bl_circle+1:]
        phrase[1] = phrase[1][:rd_circle] + "🔴" + phrase[1][rd_circle+1:]
        phrase[2] = phrase[2][:rd_circle] + "🟢" + phrase[2][rd_circle+1:]
        ballsforquest = 2
        wrdballsforquest = "балла"
        if language == "rus":
            lastPhrase = "🔵 - 🔴 - 🟢 пропуски букв, для соответствующих слов"
        elif language == "eng":
            lastPhrase = "**🔵 & 🔴 & 🟢 are blanks for the respective words**"
    phrase = " / ".join(phrase)
    phrase = phrase.upper()

    if language == "rus":
        await channel.send(f"__Скрэббл номер {scrnum}__\n{phrase}\n**{wordscount} слова**\n**{ballsforquest} {wrdballsforquest}**\n{lastPhrase}")
    elif language == "eng":
        await channel.send(f"**Scrabble - Round {scrnum}**\n**{phrase}**\n**Words: {wordscount}\nPoints: {ballsforquest}**\n{lastPhrase}")


    guess = await bot.wait_for("message", check=check, timeout=100000)
    gcu = guess.content
    if final_phrase.lower() == gcu.lower():
        athor = guess.author
        if wordscount == 2:
            if language == "rus":
                await channel.send(f"Правильный ответ: **{final_phrase.upper()}**\n{athor.mention}, +1 балл")
            elif language == "eng":
                await channel.send(f"__Correct answer:__ **{final_phrase.upper()}**\n**+1 point for {athor.mention}**")
        elif wordscount == 3:
            if language == "rus":
                await channel.send(f"Правильный ответ: **{final_phrase.upper()}**\n{athor.mention}, +2 балла")
            elif language == "eng":
                await channel.send(f"__Correct answer:__ **{final_phrase.upper()}**\n**+2 points for {athor.mention}**")




@bot.command()
@commands.has_any_role("Events MC")
async def question(ctx, question, answer, channel : discord.TextChannel, language):
    def check(m):
        return m.content.lower() == answer.lower()
    await ctx.message.delete()
    wordscount = len(answer.split())
    if len(answer.split()) == 3:
        endword = ""
        for i in range(0, len(answer.split()[0])):
            endword = endword + "🟡"
        endword = endword + " / "
        for i in range(0, len(answer.split()[1])):
            endword = endword + "🟡"
        endword = endword + " / "
        for i in range(0, len(answer.split()[2])):
            endword = endword + "🟡"
        ballsforquest = 2
        wrdballsforquest = "балла"
    elif len(answer.split()) == 2:
        endword = ""
        for i in range(0, len(answer.split()[0])):
            endword = endword + "🟡"
        endword = endword + " / "
        for i in range(0, len(answer.split()[1])):
            endword = endword + "🟡"
        ballsforquest = 1
        wrdballsforquest = "балл"
    if language == "rus":
        await channel.send(f"__Скрэббл вопрос__\n**Вопрос: **{question}\n{endword}\n**{wordscount} слова**\n**{ballsforquest} {wrdballsforquest}**\n🟡 - замена каждой буквы в словах")
    elif language == "eng":
        await channel.send(f"**__Plus question__** {question}\n**Scrabble:** {endword}\n**Pts. for trivia : {ballsforquest}**\n**To unlock the letters, someone must answer correctly to the trivia question!**")
    guess = await bot.wait_for("message", check=check, timeout=100000)
    gcu = guess.content
    if answer.lower() == gcu.lower():
        athor = guess.author
        if len(answer.split()) == 2:
            if language == "rus":
                await channel.send(f"Правильный ответ: **{answer.upper()}**\n{athor.mention}, +1 балл")
            elif language == "eng":
                await channel.send(f"__Correct answer:__ **{answer.upper()}\n+1 score for {athor.mention}**")
        elif len(answer.split()) == 3:
            if language == "rus":
                await channel.send(f"Правильный ответ: **{answer.upper()}**\n{athor.mention}, +2 балла")
            elif language == "eng":
                await channel.send(f"__Correct answer:__ **{answer.upper()}\n+2 scores for {athor.mention}**")

#multi commands
@commands.has_permissions(kick_members=True)
@bot.command()
async def multikick(ctx, member1 : discord.Member = "None", member2 : discord.Member = "None",
                    member3 : discord.Member = "None", member4 : discord.Member = "None", member5 : discord.Member = "None"):
    members = []
    kicked_members = ""
    av = ctx.author.avatar
    if member1 != "None":
        members.append(member1)
    if member2 != "None":
        members.append(member2)
    if member3 != "None":
        members.append(member3)
    if member4 != "None":
        members.append(member4)
    if member5 != "None":
        members.append(member5)

    for member in members:
        await member.kick(reason="reason")
        kicked_members = kicked_members + member.name + "\n"
    
    multikick_embed = discord.Embed(title="Kicked members: ", description=kicked_members, color = discord.Colour.from_rgb(255, 184, 69))
    multikick_embed.set_author(name=f"Staff: {ctx.author.name}", icon_url=av)
    await ctx.send(embed=multikick_embed)



@commands.has_permissions(ban_members=True)
@bot.command()
async def multiban(ctx, member1 : discord.Member = "None", member2 : discord.Member = "None",
                    member3 : discord.Member = "None", member4 : discord.Member = "None", member5 : discord.Member = "None"):
    members = []
    banned_members = ""
    av = ctx.author.avatar
    if member1 != "None":
        members.append(member1)
    if member2 != "None":
        members.append(member2)
    if member3 != "None":
        members.append(member3)
    if member4 != "None":
        members.append(member4)
    if member5 != "None":
        members.append(member5)

    for member in members:
        await member.ban(reason="reason")
        banned_members = banned_members + member.name + "\n"
    
    multiban_embed = discord.Embed(title="Banned members: ", description=banned_members, color = discord.Colour.from_rgb(255, 184, 69))
    multiban_embed.set_author(name=f"Staff: {ctx.author.name}", icon_url=av)
    await ctx.send(embed=multiban_embed)



#casino
async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["Wallet"] = 0
        users[str(user.id)]["Bank"] = 0

    with open("bank.json", 'w') as f:
        json.dump(users, f)

    return True


async def get_bank_data():
    with open("bank.json", 'r') as f:
        users = json.load(f)
    return users

@bot.command(aliases=['balance'])
async def bal(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author
    await open_account(ctx.author)

    user = member

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["Wallet"]
    bank_amt = users[str(user.id)]["Bank"]

    embedBalance = discord.Embed(color = discord.Colour.from_rgb(155, 242, 206))
    embedBalance.add_field(name="Wallet Balance", value=wallet_amt)
    embedBalance.set_author(name=member, icon_url=member.avatar)
    embedBalance.add_field(name="Bank Balance", value=bank_amt)
    await ctx.send(embed=embedBalance)


@bot.command()
async def cash(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    earn = random.randrange(200, 1000)

    phrasesCash = [f"Someone gave your {earn} coins", f"You founded {earn} coins", f"You found a wallet with {earn} coins",
              f"Something wonderfuckable is beigned and the large pigeon gave you {earn} coins", f"Your cat has won a Nobel Prize. Get rewarded with {earn} coins", 
              f"Matrix decided to eat you, but ALL Perfect stopped him. You got {earn} coins", f"Shit, there is a flying gay. You filmed it on video and got {earn} coins", 
              f"Flying shark tried to eat you, but you was faster and ran away. Take {earn} coins"]

    cashEmbed = discord.Embed(color = discord.Colour.from_rgb(155, 242, 206), title=random.choice(phrasesCash))
    
    cashEmbed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
    
    await ctx.send(embed=cashEmbed)

    users[str(user.id)]["Wallet"] += earn

    with open("bank.json", 'w') as f:
        json.dump(users, f)


@bot.command()
async def slut(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()


    chance = random.randrange(1, 3)
    money = random.randrange(1000, 5000)
    if chance == 1:
        slutPhrases = [f"You jerked off {money} coins", f"Your asshole is so expensive, take {money} coins", f"Your ass earned {money} coins, be happy"]
        slutEmbed = discord.Embed(color = discord.Colour.from_rgb(155, 242, 206), title=random.choice(slutPhrases))
        users[str(user.id)]["Wallet"] += money
    else:
        slutPhrases = [f"You got pierced in the head with a dick, pay {round(money/3)} coins for treatment", f"You was ordered by Matrix, pay {round(money/3)} for moral healing",
                      f"You was fucked to death, pay {round(money/3)} coins for your funeral"]
        slutEmbed = discord.Embed(color = discord.Colour.from_rgb(232, 56, 56), title=random.choice(slutPhrases))
        users[str(user.id)]["Wallet"] -= round(money/3)

    slutEmbed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
    await ctx.send(embed=slutEmbed)

    with open("bank.json", 'w') as f:
        json.dump(users, f)



def amount_converter(amount):
    if amount == "all":
        return "all"

    return int(amount)



@bot.command(aliases=['dep'])
async def bank(ctx, amount : amount_converter = None):
        await open_account(ctx.author)

        user = ctx.author

        users = await get_bank_data()

        if amount == "all":
            amount = amount_converter(users[str(user.id)]["Wallet"])
            if users[str(user.id)]["Wallet"] == 0:
                bankEmbed = discord.Embed(color = discord.Colour.from_rgb(232, 56, 56), title=f"You haven't got money to deposit")
                bankEmbed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
                await ctx.send(embed=bankEmbed)
                return False

        if amount > users[str(user.id)]["Wallet"] or amount < 0:
            bankEmbed = discord.Embed(color = discord.Colour.from_rgb(232, 56, 56), title=f"You haven't got money to deposit")
        else:
            bankEmbed = discord.Embed(color = discord.Colour.from_rgb(155, 242, 206), title=f"You deposit {amount} coins on your bank account")
            users[str(user.id)]["Wallet"] -= amount
            users[str(user.id)]["Bank"] += amount
    
        bankEmbed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)

        await ctx.send(embed=bankEmbed)

        with open("bank.json", 'w') as f:
            json.dump(users, f)



@bot.command(aliases=['with'])
async def getmoney(ctx, amount : amount_converter = None):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()
    if amount == "all":
        amount = amount_converter(users[str(user.id)]["Bank"])
        if users[str(user.id)]["Bank"] == 0:
            bankEmbed = discord.Embed(color = discord.Colour.from_rgb(232, 56, 56), title=f"You haven't got money to do it")
            bankEmbed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
            await ctx.send(embed=bankEmbed)
            return False
    if amount > users[str(user.id)]["Bank"] or amount < 0:
        bankEmbed = discord.Embed(color = discord.Colour.from_rgb(232, 56, 56), title=f"You haven't got money to do it")
    else:
        bankEmbed = discord.Embed(color = discord.Colour.from_rgb(155, 242, 206), title=f"You put {amount} coins in wallet from your bank account")
        users[str(user.id)]["Wallet"] += amount
        users[str(user.id)]["Bank"] -= amount
    
    bankEmbed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)

    await ctx.send(embed=bankEmbed)

    with open("bank.json", 'w') as f:
        json.dump(users, f)


@bot.command()
async def rob(ctx, member : discord.Member):
    if member == ctx.author:
        crimeEmbed = discord.Embed(color = discord.Colour.from_rgb(232, 56, 56), title="You can't rob yourself")
        crimeEmbed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        await ctx.send(embed=crimeEmbed)
    else:
        await open_account(ctx.author)

        user = ctx.author

        users = await get_bank_data()
        chance = random.randrange(1, 3)
        money = random.randrange(300, 1000)
        if chance == 1:
            crimePhrases = [f"You got caught by the police, pay {money} coins to bride it", f"You got caught by the Matrix. -{money} coins. RUN SUKA RUN"]
            crimeEmbed = discord.Embed(color = discord.Colour.from_rgb(232, 56, 56), title=random.choice(crimePhrases))
            users[str(user.id)]["Wallet"] -= money

        elif chance == 2:
            crimePhrases = [f"You robbed {member.name}, you got {money} coins", f"You're a fucking vandal, take your {money} coins"]
            crimeEmbed = discord.Embed(color = discord.Colour.from_rgb(155, 242, 206), title=random.choice(crimePhrases))
            users[str(user.id)]["Wallet"] += money
            users[str(member.id)]["Wallet"] -= money
        crimeEmbed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)

        await ctx.send(embed=crimeEmbed)

        with open("bank.json", 'w') as f:
            json.dump(users, f)









bot.run(TOKEN)

