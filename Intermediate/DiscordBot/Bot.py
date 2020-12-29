# ------------------==============================------------------ IMPORTS

import discord
from discord.ext import commands
from discord.utils import get
from discord import Intents
import time
import random
import os
import json
import praw

# ------------------==============================------------------ VARIABLES

jsonLoc = 'data.json'

# ------------------==============================------------------ JSON.VARIABLES

with open(jsonLoc, 'r') as f:
    data = json.load(f)

reddit = praw.Reddit(client_id=data["redditClientID"],
                    client_secret=data["redditSecret"],
                    username=data["redditUsername"],
                    password=data["redditPassword"],
                    user_agent=data["redditUserAgent"])
token = data["token"]
prefix = data["prefix"]
intents = Intents.all()
client = commands.Bot(command_prefix=prefix, intents=intents, help_command=None)
status = f'{data["status"]} {data["members"]}'
version = data["version"]
lastuptime = data["uptime"]
memberRole = data["memberRole"]
audioList = data["audioList"]
audioLoc = data["audioLoc"]
welcomeMessage = data["welcomeMsg"]
blacklistWords = data["wordBlacklist"]
blacklistUsers = data["userBlacklist"]
redditNsfw = data["redditNsfw"]
redditHentai = data["redditHentai"]
redditMeme = data["redditMeme"]
redditDogs = data["redditDogs"]
redditCats = data["redditCats"]
redditWholesome = data["redditWholesome"]
jsonWord = data["jsonWord"]

with open(jsonLoc, 'w') as f:
        json.dump(data, f, indent=2)

# ------------------==============================------------------ EVENTS
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    await client.change_presence(activity=discord.Game(status))
    with open(jsonLoc, 'r') as f:
        data = json.load(f)
    print(
        f'-----------------------\n'
        f'  Title   |   Details\n'
        f'-----------------------\n'
        f'loadTime  |  {round(time.time() - StartTime, 2)}\n'
        f'BotName   |  {client.user.name}\n'
        f'jsonName  |  {jsonLoc}\n'
        f'Prefix    |  "{prefix}"\n'
        f'Status    |  {status}\n'
        f'Version   |  {version}\n'
        f'LastUpTime|  {lastuptime}H\n'
        f'memberRole|  {memberRole}\n'
        f'Members   |  {data["members"]}\n'
        f'-----------------------\n'
    )
    data["uptime"] = 0.0

@client.event
async def on_member_join(member):
    with open(jsonLoc, 'r') as f:
        data = json.load(f)
    role = get(member.guild.roles, name = memberRole)
    await member.add_roles(role)
    data['members'] += 1
    await client.change_presence(activity=discord.Game(f'{data["status"]} {data["members"]}'))
    channel = client.get_channel(data["welcomeChannel"])
    CurrentMessage = random.choice(welcomeMessage)
    await discord.TextChannel.send(channel, CurrentMessage.format(member.mention))
    with open(jsonLoc, 'w') as f:
        json.dump(data, f, indent=2)
        
    

@client.event
async def on_member_remove(member):
    with open(jsonLoc, 'r') as f:
        data = json.load(f)

    if data['members'] > 0:
        data['members'] -= 1
    await client.change_presence(activity=discord.Game(f'{data["status"]} {data["members"]}'))

    with open(jsonLoc, 'w') as f:
        json.dump(data, f, indent=2)

@client.event
async def on_message(message):
    with open(jsonLoc, 'r') as f:
        data = json.load(f)
    data['uptime'] = float(round((time.time() - StartTime) / 3600, 2))
    with open(jsonLoc, 'w') as f:
        json.dump(data, f, indent=2)

    author = f"{message.author}"
    
    await client.process_commands(message)

# ------------------==============================------------------ COMMANDS

@client.command(pass_context=True, aliases=['t'])
async def test(ctx):
    print('Test')


@client.command(pass_context=True, aliases=['dogs', 'bark'])
async def dog(ctx):
    subreddit = reddit.subreddit(random.choice(redditDogs))
    section = subreddit.hot(limit=55)
    randSub = []
    for submission in section:
        if submission.url.endswith(".jpg") or submission.url.endswith(".png") or submission.url.endswith(".jpeg") or submission.url.endswith(".gif") or submission.url.endswith(".gifv"):
            randSub.append(submission)
    embedsubmission = random.choice(randSub)
    embed = discord.Embed(
        title = f'{embedsubmission.title}',
        description = f'`/r/{embedsubmission.subreddit}` | `/u/{embedsubmission.author}`',
        colour = discord.Colour.purple())
    embed.set_image(url=embedsubmission.url)
    embed.set_footer(text = f'👍 {embedsubmission.score} | 💬 {embedsubmission.num_comments}')
    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['pets', 'aww'])
async def wholesome(ctx):
    subreddit = reddit.subreddit(random.choice(redditWholesome))
    section = subreddit.hot(limit=55)
    randSub = []
    for submission in section:
        if submission.url.endswith(".jpg") or submission.url.endswith(".png") or submission.url.endswith(".jpeg") or submission.url.endswith(".gif") or submission.url.endswith(".gifv"):
            randSub.append(submission)
    embedsubmission = random.choice(randSub)
    embed = discord.Embed(
        title = f'{embedsubmission.title}',
        description = f'`/r/{embedsubmission.subreddit}` | `/u/{embedsubmission.author}`',
        colour = discord.Colour.purple())
    embed.set_image(url=embedsubmission.url)
    embed.set_footer(text = f'👍 {embedsubmission.score} | 💬 {embedsubmission.num_comments}')
    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['cats', 'meow'])
async def cat(ctx):
    subreddit = reddit.subreddit(random.choice(redditCats))
    section = subreddit.hot(limit=55)
    randSub = []
    for submission in section:
        if submission.url.endswith(".jpg") or submission.url.endswith(".png") or submission.url.endswith(".jpeg") or submission.url.endswith(".gif") or submission.url.endswith(".gifv"):
            randSub.append(submission)
    embedsubmission = random.choice(randSub)
    embed = discord.Embed(
        title = f'{embedsubmission.title}',
        description = f'`/r/{embedsubmission.subreddit}` | `/u/{embedsubmission.author}`',
        colour = discord.Colour.purple())
    embed.set_image(url=embedsubmission.url)
    embed.set_footer(text = f'👍 {embedsubmission.score} | 💬 {embedsubmission.num_comments}')
    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['funny', 'mem', 'dank', 'm'])
async def meme(ctx):
    subreddit = reddit.subreddit(random.choice(redditMeme))
    section = subreddit.top(limit=55)
    randSub = []
    for submission in section:
        if submission.url.endswith(".jpg") or submission.url.endswith(".png") or submission.url.endswith(".jpeg") or submission.url.endswith(".gif") or submission.url.endswith(".gifv"):
            randSub.append(submission)
    embedsubmission = random.choice(randSub)
    embed = discord.Embed(
        title = f'{embedsubmission.title}',
        description = f'`/r/{embedsubmission.subreddit}` | `/u/{embedsubmission.author}`',
        colour = discord.Colour.purple()
    )
    embed.set_image(url=embedsubmission.url)
    embed.set_footer(text = f'👍 {embedsubmission.score} | 💬 {embedsubmission.num_comments}')
    await ctx.send(embed=embed)



@client.command(pass_context=True, aliases=['animepuss', 'nsfwh'])
async def hentai(ctx):
    if ctx.channel.is_nsfw():
        subreddit = reddit.subreddit(random.choice(redditHentai))
        section = subreddit.top(limit=55)
        randSub = []
        for submission in section:
            if submission.url.endswith(".jpg") or submission.url.endswith(".png") or submission.url.endswith(".jpeg") or submission.url.endswith(".gif") or submission.url.endswith(".gifv"):
                randSub.append(submission)
        embedsubmission = random.choice(randSub)
        embed = discord.Embed(
            title = f'{embedsubmission.title}',
            colour = discord.Colour.purple())
        embed.set_image(url=embedsubmission.url)
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
            title = f'Try that again in a nsfw channel.',
            colour = discord.Colour.purple())
        await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['sex', 'nsfw'])
async def porn(ctx):
    if ctx.channel.is_nsfw():
        subreddit = reddit.subreddit(random.choice(redditNsfw))
        section = subreddit.hot(limit=55)
        randSub = []
        for submission in section:
            if submission.url.endswith(".jpg") or submission.url.endswith(".png") or submission.url.endswith(".jpeg") or submission.url.endswith(".gif") or submission.url.endswith(".gifv"):
                randSub.append(submission)
        embedsubmission = random.choice(randSub)
        embed = discord.Embed(
            title = f'{embedsubmission.title}',
            colour = discord.Colour.purple())
        embed.set_image(url=embedsubmission.url)
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
            title = f'Try that again in a nsfw channel.',
            colour = discord.Colour.purple())
        await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['commands', 'menu'])
async def help(ctx, *, option=None):
    if option == "play":
        embed = discord.Embed(
                title = f'Help Menu | Play',
                colour = discord.Colour.purple())
        with open(jsonLoc, 'r') as f:
            data = json.load(f)
        for command, desc in zip(data["audioList"], data["audioDesc"]):
            embed.add_field(name=f'`{prefix}{command}`', value=f'{desc}', inline=False)
        with open(jsonLoc, 'w') as f:
            json.dump(data, f, indent=2)
        await ctx.send(embed=embed)
    elif option == "2":
        embed = discord.Embed(
                title = f'Help Menu  `2/2`',
                colour = discord.Colour.purple())
        embed.add_field(name=f'Moderation ', value=f'`{prefix}purge `  | Be gone tho.. No? Be gone messages!\n`{prefix}kick  `  | The goodbye for now command\n`{prefix}ban   `  | Thor will strike them with Mjölnir\n`{prefix}unban `  | Fly around the world like superman', inline=False)
        await ctx.send(embed=embed)
    elif option == "1" or option == None:
        embed = discord.Embed(
                title = f'Help Menu  `1/2`',
                colour = discord.Colour.purple())
        embed.add_field(name=f'Memey ', value=f'`{prefix}meme  `  | Show your inner redditor\n`{prefix}nsfw  `  | Basically just P#@$\n`{prefix}hentai`  | Well you know what this is\n`{prefix}addword [input] (max 100)`  | add to my word list\n`{prefix}seeword  `  | see a random input in my word list', inline=False)
        embed.add_field(name=f'Wholesome ', value=f'`{prefix}dog   `  | Dog pictures\n`{prefix}cat   `  | Cat pictures\n`{prefix}aww   `  | Wholesome pictures', inline=False)
        embed.add_field(name=f'Utilities ', value=f'`{prefix}help  `  | I have 2 help pages :wink:\n`{prefix}ping  `  | Pong the connection\n`{prefix}uptime`  | You want **MY** uptime? :blush:\n', inline=False)
        #embed.add_field(name=f'Moderation ', value=f'`{prefix}purge `  | Be gone tho.. No? Be gone messages!\n`{prefix}kick  `  | The goodbye for now command\n`{prefix}ban   `  | Thor will strike them with Mjölnir\n`{prefix}unban `  | Fly around the world like superman', inline=False)
        #embed.add_field(name=f'Help Options ', value=f'`{prefix}help play  `  | Get audio clip list', inline=False)
        await ctx.send(embed=embed)




@client.command(pass_context=True, aliases=['bannish', 'begonethot'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, why=None):
    embed = discord.Embed(
            title = f'Bye Bye {member.name}',
            colour = discord.Colour.purple())
    await ctx.send(embed=embed)
    await member.ban(reason=f'{why} | Issued by {ctx.author}')
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title = f'Who are you? You dont have the correct ID to do that.',
            colour = discord.Colour.purple())
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title = f'Who? I cant ban nobody',
            colour = discord.Colour.purple())
        await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['k', 'begone'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, why=None):
    embed = discord.Embed(
            title = f'Bye Bye {member.name}',
            colour = discord.Colour.purple())
    await ctx.send(embed=embed)
    await member.kick(reason=f'{why} | Issued by {ctx.author}')
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title = f'Who are you? You dont have the correct ID to do that.',
            colour = discord.Colour.purple())
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title = f'Who? I cant kick nobody',
            colour = discord.Colour.purple())
        await ctx.send(embed=embed)

    
@client.command(pass_context=True, aliases=['clear', 'clean', 'wipe'])
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=5):
    if amount == -1:
        await ctx.channel.purge()
    elif amount <= 0:
        embed = discord.Embed(
            title = f'Wow you know how to delete nothing, can you show me because i cant.',
            colour = discord.Colour.purple())
        await ctx.send(embed=embed)
    else:
        await ctx.channel.purge(limit=amount + 1)
@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title = f'Are you sure you have permits to do that?',
            colour = discord.Colour.purple())
        await ctx.send(embed=embed)
    else:
        print('error: purge_error()')


@client.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(
            title = f'Pong! `{round(client.latency *1000)} ms`',
            colour = discord.Colour.purple())
    await ctx.send(embed=embed)

@client.command()
async def addword(ctx, *, input1=None):
    author = f"{ctx.author}"
    if input1 == None:
        embed = discord.Embed(
            title = f'Invalid input max 100 min 4 ({len(input1)})',
            colour = discord.Colour.purple())
        await ctx.send(embed=embed)
    elif 4 <= len(input1) <= 100:
        with open(jsonWord, 'r') as f:
            wordList = json.load(f)

        wordList["wordList"].append(f"{input1}   \n`BY {author}")
        wordList["size"] += 1


        if author not in wordList["usernames"]:
            wordList["usernames"].append(author)


        with open(jsonWord, 'w') as f:
            json.dump(wordList, f, indent=2)
    else:
        embed = discord.Embed(
            title = f'Invalid input max 100 min 4 ({len(input1)})',
            colour = discord.Colour.purple())
        await ctx.send(embed=embed)

@client.command(pass_context=True)
async def seeword(ctx):
    if ctx.channel.is_nsfw():
        with open(jsonWord, 'r') as f:
            wordList = json.load(f)

        embed = discord.Embed(
            title = f'{random.choice(wordList["wordList"])} | ({round(1 / wordList["size"], 4)}%)`',
            colour = discord.Colour.purple())
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
            title = f'Due to anyone being able to add to the list, we must make sure its is safe for all users',
            colour = discord.Colour.purple())
        await ctx.send(embed=embed)



@client.command(pass_context=True)
async def uptime(ctx):
    with open(jsonLoc, 'r') as f:
        data = json.load(f)
    embed = discord.Embed(
            title = f'I have been awake for `{data["uptime"]}` hours',
            colour = discord.Colour.purple())
    await ctx.send(embed=embed)
    

@client.command(pass_context=True, aliases=['unbannish', 'comebackthot'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, member=None):
    try:
        if member == None:
            embed = discord.Embed(
                title = f'Well i can\'t unban nobody',
                colour = discord.Colour.purple())
            await ctx.send(embed=embed)
        else:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    embed = discord.Embed(
                    title = f'Well invite {user.mention} back to the server then!',
                    colour = discord.Colour.purple())
                    await ctx.send(embed=embed)
                    return
    except:
        embed = discord.Embed(
            title = f'I can find that person in my deathNote make sure its correct (example#1234)',
            colour = discord.Colour.purple())
        await ctx.send(embed=embed)
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title = f'Are you sure you have permits to do that?',
            colour = discord.Colour.purple())
        await ctx.send(embed=embed)
    else:
        print('error: unban_error()')

@client.command(pass_context=True)
async def supersecretcommandonlyagodknows(ctx):
    with open(jsonLoc, 'r') as f:
        data = json.load(f)
    if data["secretcommand"] == "yes":
        subreddit = reddit.subreddit(random.choice(redditNsfw))
        section = subreddit.hot(limit=55)
        randSub = []
        for submission in section:
            if submission.url.endswith(".jpg") or submission.url.endswith(".png") or submission.url.endswith(".jpeg") or submission.url.endswith(".gif") or submission.url.endswith(".gifv"):
                randSub.append(submission)
        embedsubmission = random.choice(randSub)
        embed = discord.Embed(
            title = f'{embedsubmission.title}',
            colour = discord.Colour.purple())
        embed.set_image(url=embedsubmission.url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'How do you know about this command? (Disabled)',
            colour = discord.Colour.purple())
        await ctx.send(embed=embed)


# ------------------==============================------------------ START

StartTime = time.time()
client.run(token)