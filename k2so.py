import requests
import discord 
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN =os.getenv("DISCORD_TOKEN")



# This script fetches data from the Star Wars API (SWAPI) and responds to Discord messages
def fetch_swapi_data():
    url = f"https://swapi.info/api/"
    try:
        response = requests.get(url)
        response.raise_for_status() #Check for HTTP errors
        data = response.json()
        print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

fetch_swapi_data()



intents = discord.Intents.default()
intents.message_content = True

def fetch_starships():
    url = f"https://swapi.info/api/starships"
    try:
        response = requests.get(url)
        response.raise_for_status()
        starships_data = response.json()
        # print(starships_data) uncomment to check the retrieved data <3
        return starships_data
    except requests.exceptions.RequestException as e:
        print(f"error fetching {e}")
        return None 


client = discord.Client(intents=intents)

def print_info(input_name):
    data= fetch_starships()
    
    for ship in data:
        if ship.get("name", "").lower().strip() == input_name.lower().strip():
            info_lines = [f"**{key}**: {value}" for key, value in ship.items()]
            return "\n".join(info_lines)
        
    return "spaceship doesn't exist 🤓"

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("!"):
       ship_name = message.content[1:] 
       ship_info = print_info(ship_name)
       await message.channel.send(ship_info)
        
client.run(TOKEN)












