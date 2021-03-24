from replit import db
import string, random, discord, os
from webserver import keep_alive

clean_database = False # If you set it to True, all your announcements will be deleted

if clean_database == True:
	for key in db.keys():
		del db[key]

keep_alive()

token = os.getenv("TOKEN") # Remember to create a TOKEN key in the .env file

owners = [723086691266461737, 498434550347726850] # Insert Authorized IDs here

client = discord.Client()

@client.event
async def on_ready():
    print("Started Announcement System")

def rnd():
	letters = string.ascii_letters
	result_str = "".join(random.choice(letters) for i in range(20))
	return result_str

@client.event
async def on_message(message):
	if message.author.bot:
		return
	if message.content.startswith("+ann"):
		if message.author.id in owners:
			if len(message.content[5:]) != 0:
				import datetime
				dt = datetime.datetime.today()
				year = dt.year
				month = dt.month
				day = dt.day
				string = rnd()
				db["message_" + string] = message.content[5:]
				db["date_" + string] = str(day) + "-" + str(month) + "-" + str(year)
				db["author_" + string] = message.author.name
				channel = client.get_channel(770034191252586496) # Announcements channel
				await channel.send(message.content[5:] + "\n\nhttps://ann.hcat.gq/announcement/" + string)
			else:
				embed = discord.Embed(title = "<:hc_dead:818209967936634881> You haven't typed in a message to announce.", color = 0x008AFC)
				await message.channel.send(embed=embed)
		else:
			embed = discord.Embed(title = "<:hc_dead:818209967936634881> You aren't a bot owner.", color = 0x008AFC)
			await message.channel.send(embed=embed)

client.run(token)