import discord, preload, pymongo, datetime
from discord.ext import commands
from discord.ext.commands import Context
from helpers.determine_club import whatClub
client = pymongo.MongoClient(preload.getMongoUri())
db = client.sugarhill

def is_admin(a=1):
    def predicate(ctx):
        print("called")
        print(ctx.message.channel.permissions_for(ctx.message.author))
        return ctx.message.channel.permissions_for(ctx.message.author).administrator
    return commands.check(predicate)

class ClubAdmin:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_admin()
    async def addflavour(self, ctx, flavrole: discord.Role, club, hidden: bool, cost: int):
        """
        Params:
         - <flavrole>: Mention the role to become a flavour
         - <club>: Gum or Candy
         - <hidden>: Whether other clubs can see it
         - <cost>: Sugar cost
        """
        if club not in ["Gum", "Candy"]: return await self.bot.send_message(ctx.message.channel, "Please use either `Gum` or `Candy` as club")
        db.flavours.insert_one({
            "name": flavrole.name,
            "hidden": hidden,
            "role": flavrole.id,
            "cost": cost,
            "club": club
        })
        await self.bot.say("Added :thumbsup:")

def setup(bot):
    bot.add_cog(ClubAdmin(bot))