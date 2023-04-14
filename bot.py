import os
import discord
from dotenv import load_dotenv
from Bot_Functions import translate, places, weather

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

class DevPSUBot(discord.Client):
    async def on_ready(self):       # runs events based on action
        print("logged on!")
        self.units = "imperial"
        self.unitList = ['imperial', 'standard', 'metric']

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

        #translate
        if 'translate' in message.content.lower():
            message_list = message.content.split()
            i = 1
            msg = ''

            #translate (string) to (language)
            if 'to' in message.content:
                if message_list[-1] == 'to':
                    await message.channel.send("Invalid command usage")
                else:
                    while i < len(message_list)-2:
                        msg += message_list[i]
                        i += 1
                    
                    lang = message_list[i+1]

                    await message.channel.send(translate.translator_func(msg, lang))

            elif 'to' not in message.content:
                await message.channel.send("Invalid command usage")

            # translate (string)
            else:
                while i < len(message_list):
                    msg += message_list[i]
                    i += 1
            
                await message.channel.send(translate.translator_func(msg))

        #places
        if 'find' in message.content.lower():
            #find (search_string) (verb) (location)
            message_list = message.content.lower().split()
            print(message)
            index = message_list.index("find")
            
            #set search string
            search_string = ""
            index += 1
            while message_list[index] != "near" and message_list[index] != "in":
                search_string = search_string + message_list[index]
                index += 1

            #set preference
            if message_list[index] == "near":
                preference = "distance"
            preference = "popularity"
            index += 1

            #set location
            location = ""
            while index < len(message_list):
                if index != len(message_list)-1:
                    location += message_list[index] + " "
                else:
                    location += message_list[index]
                index += 1
            await message.channel.send(places.find_places_nearby(location, search_string, preference))

        #weather
        #set units
        if 'set units to' in message.content.lower():
            new_unit = message.content.lower()[13:]
            if new_unit not in self.unitList:
                await message.channel.send("Invalid units. Please use one of the following:\n" + 'imperial\n' + 'standard\n' + 'metric')
            elif new_unit == self.units:
                await message.channel.send("Units are already set to: " + self.units)
            else:
                self.units = new_unit
                await message.channel.send("Units are changed to: " + self.units)

        #show current unit
        if message.content.lower() == "show units":
            await message.channel.send("Units are set to: " + self.units)

        #implement weather search
        if 'temperature' in message.content.lower() or 'weather' in message.content.lower():
            msgList = message.content.lower().split()

            #1) temperature, weather : weather near you
            if len(msgList) == 1:
                location = "me"

            #2) temperature/weather in <place> : weather in <place>
            else:
                location = ""
                i = 2
                while i < len(msgList):
                    location += msgList[i]
                    i += 1
            
            await message.channel.send(weather.find_weather(location, self.units))



    async def on_typing(self, channel, user, when):
        print(f"{user} is typing in {channel} at {when}")
        await channel.send(f"I see you typing, {user}")


client = DevPSUBot(intents=intents)
client.run(token)