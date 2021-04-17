import discord
import os

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$join'):
        channel = message.author.voice.channel
        await channel.connect()
        message.guild.voice_client.play(discord.FFmpegPCMAudio(source="pigeonpy.mp3"))

    if message.content.startswith('$stop'):
        if message.guild.voice_client:
            message.guild.voice_client.stop()

    if message.content.startswith('$leave'):
        if message.guild.voice_client:  # If the bot is in a voice channel
            await message.guild.voice_client.disconnect()  # Leave the channel
            await message.channel.send('Kurururu pew')

    if message.content.startswith('$prayut'):
        if message.guild.voice_client:
            message.guild.voice_client.play(discord.FFmpegPCMAudio(source="prayut.mp4"))

@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.voice_client:
        if '{0.user}'.format(client) != str(member) and after.channel is not None:
            member.guild.voice_client.play(discord.FFmpegPCMAudio(source="pigeonpy.mp3"))


client.run(os.getenv('TOKEN'))

