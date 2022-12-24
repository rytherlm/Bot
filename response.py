import random


def get_response(message: str):
    p_message = message.lower()

    if p_message == '!move':
        

    if message == '!random':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`!random-random number between 1-6\n`!move-moves you to different channel'

   


    

