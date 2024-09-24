import discord
from typing import List
from enum import Enum
from speedruncompy import SpeedrunClient, GetSearch

async def src_autocomplete(ctx: discord.ApplicationContext):
	return ["awdawd", "awdawd"]
	if current == "":
		return []

	print(interaction)

	search_results = await GetSearch(query=current, includeUsers=True, limit=25).perform_async()

	return [
		app_commands.Choice(name=user.name, value=user.id)
		for user in search_results.userList
	]