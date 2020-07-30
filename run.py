import os
from src.commands import bot
from src.token import get_token

if __name__ == '__main__':
    token = get_token()
    print("Token_key: ", token)
    bot.run(token)
