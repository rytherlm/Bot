import discord
import datetime
import random

def get_response(message, user_permissions):
    message = message.lower()
    if message == 'random':
        return str(random.randint(1, 10))
    elif message == 'time':
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return current_time
    elif message == 'flip':
        number = random.randint(1,2)
        if number ==  1:
            return "heads"
        else:
            return 'tails'
    elif message == 'clear' and user_permissions.manage_messages:
        return ''
    elif message == '!help':
        return '`random\ntime\nflip\nclear`'
    return "Bad input"

# TOKEN =#taken out becuase its mine lol
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    await channel.send(f'Welcome to the server {member.mention}')

@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
    if message.author.guild_permissions.manage_messages and message.content.lower() == "clear":
        await message.channel.purge(limit=None)
    if message.author == client.user:
        return
    user_permissions = message.author.guild_permissions
    user_message = message.content
    back = get_response(user_message, user_permissions)
    if back:
        await message.channel.send(back)

def run_discord_bot():
    client.run(TOKEN)

def main():
    run_discord_bot()

if __name__ =='__main__':
    main()
