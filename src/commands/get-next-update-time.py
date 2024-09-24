import discord
from discord import app_commands
from discord.ext import commands
from ..utils import src_autocomplete

@commands.hybrid_command(
    name="get-next-update-time",
    description="Get the time of when the next update will happen"
)
@app_commands.autocomplete(user=src_autocomplete)
async def next_update(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")