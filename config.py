from dotenv import load_dotenv
import os

#Fetch details from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
#Fetching database details is shifted to main.py
#DATABASE_DICT = dict(eval(os.getenv("DISCORD_DATABASE_DETAILS")))


prefix="!"

APPROVED_SERVERS=[797570077364977696,]
#BLACKLIST = []
#List of Cogs to run on startup;
STARTUP_COGS = [
    "cogs.UtilityCog","cogs.GameDealCog","cogs.Notifications","cogs.StockChecker","jishaku"
    ]

#Channels and Roles
stock_notifications_channel_id=849310570821713927



embed_colours=[0xFFFF00,#yellow
            0xFF0000,#red
            0xFF0000,#green
            0x00FFFF,#blue
            0xFF00FF,#pink
]

