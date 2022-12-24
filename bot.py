import discord
import response


async def send_message(message, user_message, is_private):
    try:
        rep = response.get_response(user_message)
        await message.author.send(rep) if is_private else await message.channel.send(rep)

    except Exception as e:
        print(e)


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
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said {user_message} in ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)