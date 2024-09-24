--DROP DATABASE farmington;
--CREATE DATABASE farmington;

CREATE TABLE username_colours (
	id VARCHAR(8) PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	hex VARCHAR(8) NOT NULL
);

CREATE TABLE flags (
	id VARCHAR(100) PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	fullName VARCHAR(100) NOT NULL,
	label VARCHAR(100) NOT NULL,
	flagIcon VARCHAR(100) NOT NULL,
	lbFlagIcon VARCHAR(100) NOT NULL,
	lbName VARCHAR(100) NOT NULL
);

CREATE TABLE flag_discord_emojis (
	id INT PRIMARY KEY,
	flagId VARCHAR(100) REFERENCES flags(id),
	guildId VARCHAR(30) NOT NULL,
	emoji VARCHAR(100) NOT NULL
);

CREATE TABLE power_level (
	id INT PRIMARY KEY,
	name VARCHAR(100)
);

CREATE TABLE users (
	id VARCHAR(8) PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	url VARCHAR(30) NOT NULL,
	colour1Id VARCHAR(8) REFERENCES username_colours(id) NOT NULL,
	colour2Id VARCHAR(8) REFERENCES username_colours(id),
	hasSupporterAnimation BIT,
	flagId VARCHAR(100) REFERENCES flags(id),
	powerLevelId INT REFERENCES power_level(id) NOT NULL,
	hasAvatarDecoration BOOL NOT NULL,
	avatarDecorationSeparateColours BIT,
	avatarDecorationColour1Id VARCHAR(8) REFERENCES username_colours(id),
	avatarDecorationColour2Id VARCHAR(8) REFERENCES username_colours(id),
	iconType INT,
	supporterIconType INT,
	supporterIconPosition INT
);

CREATE TABLE social_medias (
	id INT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	icon VARCHAR(100)
);

CREATE TABLE user_social_medias (
	userId VARCHAR(8) REFERENCES users(id),
	socialMediaId INT REFERENCES social_medias(id),
	url VARCHAR(100) NOT NULL,
	isVerified BOOL
);

CREATE TABLE pronouns (
	id SERIAL PRIMARY KEY,
	pronoun VARCHAR(50)
);

CREATE TABLE user_pronouns (
	userId VARCHAR(8) REFERENCES users(id),
	pronounId INT REFERENCES pronouns(id)
);

CREATE TABLE unregistered_players (
	id VARCHAR(38) PRIMARY KEY,
	name VARCHAR(150) NOT NULL,
	flagId VARCHAR(100) REFERENCES flags(id)
);

CREATE TABLE user_data (
	userId VARCHAR(8) REFERENCES users(id),
	fullGameRunCount INT,
	levelRunCount INT,
	pendingRunCount INT,
	rejectedRunCount INT,
	firstPlaceCount INT.
	secondPlaceCount INT,
	thirdPlaceCount INT,
	gamesPlayed INT,
	categoriesPlayed INT,
);

CREATE TABLE leaderboard_types (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

CREATE TABLE leaderboard (
	id SERIAL PRIMARY KEY,
	createTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	finishTime TIMESTAMP,
	leaderboardType INT REFERENCES leaderboard_types(id)
);

CREATE TABLE leaderboard_place (
	id SERIAL PRIMARY KEY,
	leaderboardId INT REFERENCES leaderboard(id),
	amount INT
);

CREATE TAbLE games (
	id VARCHAR(8) PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	url VARCHAR(100) NOT NULL
);

CREATE TABLE categories (
	id VARCHAR(8) PRIMARY KEY,
	gameId VARCHAR(8) REFERENCES games(id),
	name VARCHAR(100) NOT NULL
);

CREATE TABLE variables (
	id VARCHAR(8) PRIMARY KEY,
	categoryId VARCHAR(8) REFERENCES categories(id),
	name VARCHAR(100) NOT NULL,
	isSubcategory BOOL
);

CREATE TABLE variable_values (
	id VARCHAR(8) PRIMARY KEY,
	variableId VARCHAR(8) REFERENCES variables(id),
	name VARCHAR(100)
);

CREATE TABLE leaderboard_place_data (
	id INT PRIMARY KEY,
	leaderboardPlaceId INT REFERENCES leaderboard_place(id),
	userId VARCHAR(8) REFERENCES users(id),
	unregisteredPlayerId VARCHAR(38) REFERENCES unregistered_players(id),
	gameId VARCHAR(8) REFERENCES games(id),
	categoryId VARCHAR(8) REFERENCES categories(id),
	variableId VARCHAR(8) REFERENCES variables(id)
);

CREATE TABLE leaderboard_place_data_values (
	id INT PRIMARY KEY,
	leaderboardPlaceDataId INT REFERENCES leaderboard_place_data(id),
	valueId VARCHAR(8) REFERENCES variable_values(id)
);

CREATE TABLE database_users (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	userId VARCHAR(8),
	url VARCHAR(30)
);