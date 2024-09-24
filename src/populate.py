import psycopg2
from speedruncompy import GetUserSummary, GetStaticData, SitePowerLevel, GetGameList

connection = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost")
cursor = connection.cursor()

with open("farmington-db-creator.sql") as file:
	cursor.execute(file.read())

static_data = GetStaticData().perform()

for flag in static_data.areas:
	cursor.execute("INSERT INTO flags(id, name, fullName, label, flagIcon, lbFlagIcon, lbName) VALUES (%s, %s, %s, %s, %s, %s, %s)", (flag.id, flag.name, flag.fullName, flag.label, flag.flagIcon, flag.lbFlagIcon, flag.lbName))

for colour in static_data.colors:
	cursor.execute("INSERT INTO username_colours(id, name, hex) VALUES (%s, %s, %s)", (colour.id, colour.name.capitalize(), colour.darkColor))

for network in static_data.socialNetworkList:
	cursor.execute("INSERT INTO social_medias(id, name) VALUES (%s, %s)", (network.id, network.name))

cursor.execute(
	"INSERT INTO power_level(id, name) VALUES (%s, %s), (%s, %s), (%s, %s), (%s, %s), (%s, %s)",
	(SitePowerLevel.BANNED, "Banned", SitePowerLevel.USER, "User", SitePowerLevel.CONTENT_MOD, "Content Moderator", SitePowerLevel.SITE_MOD, "Site Moderator", SitePowerLevel.SITE_ADMIN, "Admin")
)

for pronoun in ["Any/All", "He/Him", "She/Her", "They/Them", "It/Its"]:
	cursor.execute("INSERT INTO pronouns(pronoun) VALUES (%s)", [pronoun])

for type in ["WR", "Runs", "Games", "Verified", "categories", "co-op", "WRs Full Game", "WRS IL", "Runs IL", "Runs Full game", "Co-op Teams runs", "Podium", "Games with WRs", "Personal-bests", "Obsoletes", "Levels", "Most levels", "Most categories fg", "Most categories ils", "Most categories", "Most obtainable WRs fg", "Most obtainable WRs ils", "Most obtainable WRs", "Most moderators", "Most platforms", "Longest abreviation", "Longest game name", "longest cateogory name", "longest level name", "Variable with highest amount of values", "most amount of variables"]:
	cursor.execute("INSERT INTO leaderboard_types(name) VALUES (%s)", [type])

user_data = GetUserSummary(url="YUMmy_Bacon5").perform()
user = user_data.user
cursor.execute(
	"INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
	(user.id, user.name, user.url, user.color1Id, user.color2Id, user.colorAnimate, user.areaId, user.powerLevel, user.avatarDecoration.enabled, user.avatarDecoration.separateColors, user.avatarDecoration.color1Id, user.avatarDecoration.color2Id, user.iconType, user.supporterIconType, user.supporterIconPosition)
)

for user_network in user_data.userSocialConnectionList:
	cursor.execute(
		"INSERT INTO user_social_medias(userId, socialMediaId, url, isVerified) VALUES (%s, %s, %s, %s)",
		(user.id, user_network.networkId, user_network.value, user_network.verified)
	)

cursor.execute("SELECT * FROM pronouns")
pronous_table = cursor.fetchall()
for user_pronoun in user_data.user.pronouns:
	cursor.execute(
		"INSERT INTO user_pronouns(userId, pronounId) VALUES (%s, %s)",
		(user.id, list(filter(lambda x: x[1] == user_pronoun, pronous_table))[0][0])
	)

type_id = cursor.execute("SELECT id FROM leaderboard_types WHERE name = 'Longest name'")
cursor.execute("INSERT INTO leaderboard(leaderboardType) VALUES (%s)", [type_id])
leaderboard_id = cursor.lastrowid
for game in GetGameList().perform().gameList:
	cursor.execute("INSERT INTO leaderboard_place(leaderboardId, amount) VALUES (%s, %s)", (leaderboard_id,   ))