import discord
import logging
import configparser
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--area",default="config.ini", help="Area config file to use")
args = parser.parse_args()
areafile = args.area

config = configparser.ConfigParser()
config.read(['config.ini',areafile])

BOT_TOKEN=config.get('CONFIG', 'BOT_TOKEN')
channel_id = config.items( "areas" )
print (channel_id)
logging.basicConfig(level=logging.INFO)
client = discord.Client()

@client.event
async def on_ready():
    
    def check(m):
        return not m.pinned
 
    for ch in channel_id:
       channel = client.get_channel(int(ch[1]))
       print("Purging", channel, "...")
       purged = await channel.purge(limit=9999999, check=check)
       print("Purged", len(purged), "messages.")

    
    await client.logout()
    exit("Done!")

client.run(BOT_TOKEN)
channel_id.close()
