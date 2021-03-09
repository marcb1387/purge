# Dr.Purge
Bot to purge all text from discord channel 

Read here on how to create a Discord bot https://discordpy.readthedocs.io/en/latest/discord.html

make sure the bot has the permissions to manage messages on the server or channel you are working with.  

Copy the config example `cp config.ini.example config.ini` and `cp area.ini.example area.ini` put in your bot token details.
Place all channel ID's you want to clear into the channel_ids.txt file. 1 channel ID per line.

edit config with Bot Token once you have created the bot then run with cron when you want to clear a channel or manually `python3 purge.py -a area.ini`

area.ini can include all you channels and their names.

Requirment:  pip install discord.py https://pypi.org/project/discord.py/

Credit to Malte for the original.
