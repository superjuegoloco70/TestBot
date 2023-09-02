import random

def gen_pass(pass_length):
    elements = "abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def coin_flip():
    side = random.randint(1,2)
    if side == 1:
        return "Heads"
    elif side == 2:
        return "Tails"
    
