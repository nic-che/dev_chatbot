# DevPSU - Discord Bot

## Table of Contents
* [Overview](https://github.com/nic-che/dev_chatbot#overview)
* [Function Implementations](https://github.com/nic-che/dev_chatbot#function-implementations)
* [Commands](https://github.com/nic-che/dev_chatbot#commands)
* [Credits](https://github.com/nic-che/dev_chatbot#credits)

### Overview

### Function Implementations

### Commands

- typing
    - When a user types into the chat, the bot will recognize the action and announce "I see you typing, @[user]"

- hello
    - By simply including the world `hello` in any sentence, SolceBot will automatically respond with "Hello!"

- mention
    - In the case that someone mentions (@) the bot, SolceBot will automatically respond with "Mentioned!"

- react
    - When a user includes the world `react` in any sentence, SolceBot will recognize the command and react to the message with an assigned emoticon.

- translate
    - The command requires a string that the user would like to translate, followed by the target language for the string to be translated into. In this context, the string can either be a word or complete sentence.
        - > translate [string] to [language][^1]

    [^1]: As this function utilizes Python's googletrans library for the Google Translate API, some languages may not be included.

- places
    - To find a place of any type (e.g., restaurant, museum, hotel) near you:
        - > find [place] near me

    - To find a place in a certain location (e.g., boston, california, brooklyn):
        - > find [place] in [location]

    - To sort by popularity, simply include `by popularity` at the end of either of the previous statements.

    - To sort by distance, simply include `by distance` at the end of either of the previous statements.

- weather
    - To obtain information on weather in your area:
        - > weather near me
        - > temperature near me

    - To obtain information on weather in a certain location (e.g., boston, california, brooklyn):
        - > weather in [location]
        - > temperature in [location]

### Credits