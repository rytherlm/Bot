import discord
from discord.ext import commands
import datetime
import random

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    await channel.send(f'Welcome to the server {member.mention}')

@bot.command()
async def random(ctx):
    """Generates a random number between 1 and 10."""
    await ctx.send(str(random.randint(1, 10)))

@bot.command()
async def time(ctx):
    """Displays the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    await ctx.send(current_time)

@bot.command()
async def flip(ctx):
    """Flips a coin and returns 'heads' or 'tails'."""
    number = random.randint(1, 2)
    if number == 1:
        await ctx.send("heads")
    else:
        await ctx.send("tails")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx):
    """Clears messages in the channel (requires 'manage_messages' permission)."""
    await ctx.channel.purge(limit=None)

@bot.command()
async def help(ctx):
    """Displays a list of available commands."""
    command_list = [command.name for command in bot.commands]
    help_text = '\n'.join(command_list)
    embed = discord.Embed(title="Available Commands", description=help_text, color=discord.Color.blue())
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command. Use '!help' to see available commands.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to execute this command.")

def run_discord_bot():
    bot.run('YOUR_TOKEN_HERE')

def main():
    run_discord_bot()

if __name__ =='__main__':
    main()
