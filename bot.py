#python bot.py
import os
import discord
from dotenv import load_dotenv
from typing import Union
from discord import Message
from Bot_Functions import translate, places, weather
from ttt import ttt

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

class DevPSUBot(discord.Client):
    async def on_ready(self):       # runs events based on action
        print("logged on!")
        self.state = "message"
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

        #implement tic tac toe
        #END GAME after n mins
        if message.content == "ttt":
                        #if failed, change ttti to ttt1, ttt1 to ttt2 (already changed; if broken, switch back)
            self.state = "ttt1"
            self.player_1 = message.author
            await message.channel.send(f"Player 1 is {self.player_1}.")
            await message.channel.send(f"Please mention player 2.")
        if self.state == "ttt1" and message.author == self.player_1 and len(message.mentions) == 1:
            self.state = "ttt2"
            self.player_2 = message.mentions[0]
            await message.channel.send(f"Player 2 is {self.player_2}.")
            await message.channel.send("Use the numberpad for the input:\n```7 | 8 | 9\n--+---+--\n4 | 5 | 6\n--+---+--\n1 | 2 | 3\n```")
            await message.channel.send(f"{self.player_1}'s turn.")
            self.game = ttt()
        
        if message.content in {'1', '2', '3', '4', '5', '6', '7', '8', '9'} and self.state in {"ttt1", "ttt2"} and message.author in {self.player_1, self.player_2}:
            status = self.game.update_board(message.content, self.state)
            if status == -1:
                await message.channel.send("Invalid position; please try again.")
            elif status == 0:
                await message.channel.send(format_board(self.game.board))
                if self.state == "ttt1":
                    self.state == "ttt2"
                    await message.channel.send(f"{self.player_2}'s turn")       # Return to these lines; if players are not specifically mentioned, @
                else:
                    self.state = "ttt1"
                    await message.channel.send(f"{self.player_1}'s turn")
            elif status == 1:
                await message.channel.send(format_board(self.game.board))
                await message.channel.send(f"Player {self.state[3]} wins!")
                self.state = "message"
            elif status == 2:
                await message.channel.send(format_board(self.game.board))
                await message.channel.send(f"Stalemate!")
                self.state = "message"

    async def on_typing(self, channel, user, when):
        print(f"{user} is typing in {channel} at {when}")
        await channel.send(f"I see you typing, {user}")

#depending on user responses, reformat board beginning from index 1?
def format_board(x):
    return f"```{x[0]} | {x[1]} | {x[2]}\n--+---+--\n{x[3]} | {x[4]} | {x[5]}\n--+---+--\n{x[6]} | {x[7]} | {x[8]}"


client = DevPSUBot(intents=intents)
client.run(token)