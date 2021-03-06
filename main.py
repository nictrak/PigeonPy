import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$join'):
        contents = message.content.split()
        if len(contents) > 1:
            channel_name = message.content[len(contents[0])+1:]
            print(channel_name)
            channel = discord.utils.get(message.guild.voice_channels, name=channel_name, bitrate=64000)
        else:
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

