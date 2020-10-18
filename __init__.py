import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")



@client.event
async def on_message(message):
    if message.content.startswith("난 잘생겼어"):
        await message.channel.send("월월 월 워얼..!")
    if message.content.startswith("난 정상인이야"):
        await message.channel.send("월월 월 워얼..!")
    if message.content.startswith("난 개멋져"):
        await message.channel.send("월월 월 워얼..!")
    if message.content.startswith("뀨뀨"):
        await message.channel.send("월월 월 워얼..!")
    if message.content.startswith("난 개 멋짐"):
        await message.channel.send("월월 월 워얼..!")
    if message.content.startswith("ㅗ"):
        await message.channel.send("그르릉 월")
    if message.content.startswith("민회장귀요미"):
        await message.channel.send("개로서도 납득할수없는 소리입니다")

access_token = os.eviron["BOT_TOKEN"]        
client.run(acess_token)
