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

class Clubs:
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True)
    async def clubs(self, ctx):
        """
        Shows all the clubs you can join
        """
        for club in db.clubs.find({}):
            await self.bot.send_message(ctx.message.channel, embed=discord.Embed(
                title = club["name"],
                description = club["description"],
                colour = 0xd16cf8,
                timestamp = datetime.datetime.today()
            ).set_thumbnail(url=club["icon"]).set_footer(text="TL;DR - You probably don't have permission"))

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

    @commands.command(pass_context=True, aliases=["flavors"])
    async def flavours(self, ctx):
        """
        Shows the flavours you can buy, in your club.
        """
        for club in db.clubs.find({}):
            await self.bot.send_message(ctx.message.channel, embed=discord.Embed(
                title = club["name"],
                description = club["description"],
                colour = 0xd16cf8,
                timestamp = datetime.datetime.today()
            ).set_thumbnail(url=club["icon"]))

def setup(bot):
    bot.add_cog(Clubs(bot))