import discord
from discord.ext import commands
from discord.commands import option
from utils import src_autocomplete

class Add_User(commands.Cog):
    def __init__(self, bot, src_client):
        self.bot = bot

    @commands.slash_command()
    @option("user", "The user to add", autocomplete=src_autocomplete)
    async def hello(self, ctx: discord.ApplicationContext, user: str):
        await ctx.respond("Hello!")