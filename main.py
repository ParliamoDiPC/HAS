from replit import db
import string, random, discord, os
from webserver import keep_alive

clean_database = False

if clean_database == True:
	for key in db.keys():
		del db[key]

keep_alive()

token = os.getenv("TOKEN")

owners = [723086691266461737, 498434550347726850]

client = discord.Client()

@client.event
async def on_ready():
    print("Started")

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
				random_number = rnd()
				db["message_" + random_number] = message.content[5:]
				db["date_" + random_number] = str(day) + "-" + str(month) + "-" + str(year)
				db["author_" + random_number] = message.author.name
				channel = client.get_channel(770034191252586496)
				await channel.send(message.content[5:] + "\n\nhttps://ann.hcat.gq/announcement/" + random_number)
			else:
				await message.channel.send("<:hc_dead:818209967936634881> You haven't typed in a message to announce.")
		else:
			await message.channel.send("<:hc_dead:818209967936634881> You aren't a bot owner.")

client.run(token)