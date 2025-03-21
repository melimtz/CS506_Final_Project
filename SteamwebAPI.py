import requests
import json
#class that gives us relevant information using steams api
class SteamwebAPI:
    def __init__(self, api_key, game_id):
        self.api_key = api_key 
        self.game_id = game_id
    
    def game_overview(self):
        #Url of the game's specific details
        url = f"https://store.steampowered.com/api/appdetails?appids={self.game_id}&key={self.api_key}"

        game = requests.get(url)
        code = game.status_code
        #checks if the request was able to proccess and had no errors
        if self.request_check(code):
            data = game.json()
            
            #The entire json file is in the data section
            game_info = data[self.game_id]['data']

            #game info, and price, and achievments
            print(f"Game Name: {game_info.get('name')}")
            if game_info.get('price_overview', {}).get('final_formatted') == None:
                print("Price: Free")
            else:
                print(f"Price: {game_info.get('price_overview', {}).get('final_formatted')}")
                
            print(f"Total Achievments: {game_info.get('achievements', {}).get('total')}")
        else:
            print(f"No data was found")

            
    def ratings(self):
        #Url of the ratings of the specific game
        url = f"https://store.steampowered.com/appreviews/{self.game_id}?json=1"

        rating = requests.get(url)
        code = rating.status_code

        #checks if the request was able to proccess and had no errors
        if self.request_check(code):
            reviews = rating.json()
            
            if "query_summary" in reviews:
                query_summary = reviews["query_summary"]
                print("Query Summary:")
                print(f"Total Reviews: {query_summary['total_reviews']}")
                print(f"Total Positive Reviews: {query_summary['total_positive']}")
                print(f"Total Negative Reviews: {query_summary['total_negative']}")
        else:
            print("No reviews were found")

    def current_players(self):
        url = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={self.game_id}"

        current_players = requests.get(url)

        data = current_players.json()
        #Checks the current player count of the specified game
        if "response" in data:
            response_summary = data["response"]
            print(f"Current Players: {response_summary['player_count']}")

    #error checking (check https://partner.steamgames.com/doc/webapi_overview/responses for more information)
    def request_check(self, code):
        if code == 200:
            return True
        elif code == 400:
            print("Bad request")
        elif code == 401:
            print("Unauthorized Access")
        elif code == 403:
            print("Forbidden")
        elif code == 404:
            print("Not Found")
        elif code == 405:
            print("Method Not Allowed")
        elif code == 429:
            print("Too Many Requests")
        elif code == 500:
            print("Internal Server Error")
        elif code == 503:
            print("Service Unavailable")
        return False



api_key = "01B13356A9555DBB675D8049FDA43AD1"
game_id = ["440", "570", "730", "381210"]

for game in game_id:
    steam_api =SteamwebAPI(api_key, game)
    steam_api.game_overview()
    steam_api.ratings()
    steam_api.current_players()

