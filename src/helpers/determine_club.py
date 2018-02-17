import discord

GUM = 1
CANDY = 2
NONE = 3

GUM_ID = "414380333669285888"
CANDY_ID = "414380672698810368"

def whatClub(mem: discord.Member):
    if GUM_ID in [r.id for r in mem.roles]:
        return GUM
    if CANDY_ID in [r.id for r in mem.roles]:
        return GUM
    return NONE