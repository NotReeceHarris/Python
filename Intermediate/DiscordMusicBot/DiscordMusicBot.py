import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import time

exts = list(filter(None, os.environ.get('PATHEXT', '').split(os.pathsep)))
Token = ''
Prefix = '.'
Client = commands.Bot(command_prefix=Prefix)
Status = 'Nothing | .help'

CurrentVolume = 100


# ------------------==============================------------------
@Client.event
async def on_ready():
    await Client.change_presence(status=discord.Status.online)
    await Client.change_presence(activity=discord.Game(Status))
    print(f'Bot Loaded in {round(time.time() - StartTime, 2)} as {Client.user.name}.')


@Client.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(Client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f'Bot connected to {channel}')

    await ctx.send(f'I have joined the channel. ({channel})')

@Client.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    Voice = get(Client.voice_clients, guild=ctx.guild)
    if Voice and Voice.is_connected():
        await Voice.disconnect()
        print(f'Bot disconnected from {channel}')
        await ctx.send(f'I have left the channel. ({channel})')
    else:
        print(f'Bot was told but wasnt in one')
        await ctx.send(f'Im not in a channel.')


@Client.command(pass_context=True, aliases=['p   ', 'pla', 'start', 's'])
async def play(ctx, url: str):
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove('song.mp3')
            print('Removed old song.mp3')
    except PermissionError:
        print('Trying to delete song file, but its playing')
        await ctx.send('Music Currently Playing')
        return

    await ctx.send("Getting Song Now!")
    Voice = get(Client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('Downloading audio now')
        ydl.download([url])

        for file in os.listdir('./'):
            if file.endswith('.mp3'):
                name = file
                os.rename(file, 'song.mp3')
                print(f'Renamed file {file} to song.mp3')

        Voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print(f'{name} has finished playing'))
        Voice.source = discord.PCMVolumeTransformer(Voice.source)
        Voice.source.volume = CurrentVolume

        nname = os.name.rsplit("-", 2)
        await ctx.send(f'Currently Playing: {nname}')
        print(f'Playing {nname}')
        await Client.change_presence(activity=discord.Game(nname))
        print(f'Changed status to {nname}')


# ------------------==============================------------------ START
StartTime = time.time()
Client.run(Token)
