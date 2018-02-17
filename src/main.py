import json
startup_extensions = ["clans", "errors", "clubinfo", "clubuser", "clubadmin"]

with open("./config.json") as f:
    config = json.loads(f.read())

from discord.ext import commands
bot = commands.Bot("-", description="A bot for Bubblegum :D")

@bot.event
async def on_ready():
    print("Ready!")
    print(bot.user.name)
    print(bot.user.id)
    print("-----------")



if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    bot.run(config["token"])