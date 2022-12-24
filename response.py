import random
import discord


def get_response(message: str):
    if message == '!random':
        return str(random.randint(1, 6))

    if message == '!help':
        return '`!random-random number between 1-6\n`!move-moves you to different channel'
    return ''

   


    

