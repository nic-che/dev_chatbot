import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

class DevPSUBot(discord.Client):
    async def on_ready(self):       # runs events based on action
        print("logged on!")

    async def on_message(self, message):
        print(f"message found!: {message.content} from {message.author} in {message.channel}")
        if message.author == client.user:      # self
            return
        if "hello" in message.content.lower():
            print(f"command recognized: hello")
            await message.channel.send("Hello!")    # seek command from channel
        if client.user in message.mentions:
            print("Bot mentioned!")
            await message.channel.send("Mentioned!")
        if "react" in message.content.lower():
            print("react command recognized")
            await message.add_reaction("😅")

    async def on_typing(self, channel, user, when):
        print(f"{user} is typing in {channel} at {when}")
        await channel.send(f"I see you typing, {user}")

client = DevPSUBot(intents=intents)
client.run(token)