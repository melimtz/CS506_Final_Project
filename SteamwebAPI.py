import requests
import csv
import asyncio
import aiohttp
import json
import pandas as pd
#class that gives us relevant information using steams api
class SteamwebAPI:
    def __init__(self, api_key, game_id):
        self.api_key = api_key 
        self.game_id = game_id
    
    async def game_overview(self, entry):
        #Url of the game's specific details
        url = f"https://store.steampowered.com/api/appdetails?appids={self.game_id}&key={self.api_key}"

        async with entry.get(url) as game:
            code = game.status
            #checks if the request was able to proccess and had no errors
            if self.request_check(code):

                data = await game.json()
                #The entire json file is in the data section
                if data.get(str(self.game_id), {}).get('success', False):
                    game_info = data.get(str(self.game_id), {}).get('data', {})
                    #game info, and price, and achievments
                    game_name = game_info.get('name', 'Unknown')
                    price = game_info.get('price_overview', {}).get('final_formatted', 'Free')
                    achievements = game_info.get('achievements', {}).get('total', 0)
                    return game_name, price, achievements
                else:
                    return "Unknown", "Free", 0
                
            else:
                return "Unknown", "Free", 0
            

            
    async def ratings(self,entry):
        #Url of the ratings of the specific game
        url = f"https://store.steampowered.com/appreviews/{self.game_id}?json=1"
        
        #checks if the request was able to proccess and had no errors
        async with entry.get(url) as rating:

            code = rating.status

            if self.request_check(code):
                reviews = await rating.json()
                if "query_summary" in reviews:
                    query_summary = reviews["query_summary"]
                    total_reviews = query_summary.get("total_reviews", 0)
                    positive_reviews = query_summary.get("total_positive", 0)
                    negative_reviews = query_summary.get("total_negative", 0)
                    return total_reviews, positive_reviews, negative_reviews
            else:
                return None, None, None

    async def current_players(self, entry):
        url = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={self.game_id}"

        async with entry.get(url) as current_players:
            
            code = current_players.status

            if self.request_check(code):
                #Checks the current player count of the specified game
                data = await current_players.json()
                
                player_count = data.get("response", {}).get("player_count", 0)
                return player_count
            return 0
        
    #error checking (check https://partner.steamgames.com/doc/webapi_overview/responses for more information)
    def request_check(self, code):
        if code == 200:
            return True
        else:
            
            return False
    
    async def game_data(self, entry):
        game_name, price, achievements = await self.game_overview(entry=entry)
        total_reviews, positive_reviews, negative_reviews = await self.ratings(entry=entry)
        current_players = await self.current_players(entry=entry)
        
        return {
            "game_name": game_name,
            "price": price,
            "achievements": achievements,
            "total_reviews": total_reviews,
            "positive_reviews": positive_reviews,
            "negative_reviews": negative_reviews,
            "current_players": current_players
        }



async def all_games(api_key, game_id):
    with open ('steam_games.csv', mode='w', newline='') as file:
        fields = ["game_name", "price", "achievements", "total_reviews", "positive_reviews", "negative_reviews", "current_players"]
        write = csv.DictWriter(file, fieldnames=fields)

        write.writeheader()

        async with aiohttp.ClientSession() as entry:
            task = []
            for game in game_id:
                steam_api = SteamwebAPI(api_key, game)
                task.append(steam_api.game_data(entry))


            game_list = await asyncio.gather(*task)

            for data in game_list:
                write.writerow(data)
            print("csv file was created")


api_key = "" # Your own api key



df_steam = pd.read_csv("set_id.csv")

game_ids = df_steam["index"].tolist()

short_games = game_ids[:100]



# Running the async function to fetch game data and write it to CSV
asyncio.run(all_games(api_key, short_games))

