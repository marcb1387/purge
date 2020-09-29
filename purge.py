import discord
import logging

channel_id = open("config.txt", "r")

logging.basicConfig(level=logging.INFO)
client = discord.Client()

@client.event
async def on_ready():
    
    def check(m):
        return not m.pinned
 
    for ch in channel_id:
       channel = client.get_channel(int(ch))
       print("Purging", channel, "...")
       purged = await channel.purge(limit=9999999, check=check)
       print("Purged", len(purged), "messages.")

    
    await client.logout()
    exit("Done!")

client.run("BOT TOKEN")
channel_id.close()