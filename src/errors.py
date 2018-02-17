import discord, preload, pymongo, datetime
from discord.ext import commands
from discord.ext.commands import Context
class Errors:
    def __init__(self, bot):
        self.bot = bot

        @bot.event
        async def on_command_error(exception, ctx):
            print(exception)
            await self.bot.send_message(ctx.message.channel, embed = discord.Embed(
                title="Error",
                description=str(exception),
                color= 0xff1010
            ))

def setup(bot):
    bot.add_cog(Errors(bot))