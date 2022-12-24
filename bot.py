import discord
import datetime
import random


def get_response(message):
    message = message.lower()
    if message == 'random':
        return str(random.randint(1, 6000))
    elif message == 'time':
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return current_time
    elif message == 'flip':
        number = random.randint(1,2)
        if number ==  1:
            return "heads"
        else:
            return 'tails'
    if message == '!help':
        return '`random\ntime\nflip`'
    return "Bad input"

   
        


def run_discord_bot():
    TOKEN = 'MTA1NTcwMDYyMjU2NzAyMjYwMg.GKJR1v.eIVkG4Zc2qHhFN_UsL-cHkQYw5ad1jRCRLGd3g'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # if message.author.permissions_in(message.channel).manage_messages and message.content.lower() == "clear":
        #     await message.channel.purge_from(limit=None)
        if message.author == client.user:
            return
        user_message = message.content
        back = get_response(user_message)
        await message.channel.send(back)
        

    client.run(TOKEN)


def main():
    run_discord_bot()
if __name__ =='__main__':
    main()