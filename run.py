import os
from src.commands import bot
#from src.token import get_token

if __name__ == '__main__':
    token_path = os.path.dirname(os.path.abspath(__file__)) + "/src/token.txt"
    t = open(token_path, "r", encoding="utf-8")
    token = t.read().split()[0]
    print("Token_key: ", token)
    bot.run(token)
