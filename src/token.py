import os

def get_token():    
    token_path = os.path.dirname(os.path.abspath(__file__)) + "/token.txt"
    t = open(token_path, "r", encoding="utf-8")
    token = t.read().split()[0]
    return token