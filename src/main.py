import os
import discord
from discord.commands import option
from speedruncompy import SpeedrunClient
from utils import src_autocomplete
from commands.add_user import Add_User

bot = discord.Bot()

src_client = SpeedrunClient(user_agent="farmington-bot; https://github.com/Farmington-Runners/discord-bot")

@bot.slash_command(name="add-user")
@option("user", "The user to add", autocomplete=src_autocomplete)
async def command(ctx: discord.ApplicationContext, user: str):
    await ctx.respond("Hey!")

@bot.event
async def on_ready():
    bot.add_cog(Add_User(bot, src_client))
    await bot.sync_commands()
    print("Ready")

from dotenv import load_dotenv
load_dotenv(dotenv_path="../.env")

bot.run(os.getenv("DISCORD_TOKEN"))