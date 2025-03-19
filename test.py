import requests

api_key = "01B13356A9555DBB675D8049FDA43AD1" # webAPI key, you will need to get this using your own steam account

game_id = "381210" #individual steam game id

url = f"https://store.steampowered.com/api/appdetails?appids={game_id}&key={api_key}"

response = requests.get(url)

if response.status_code == 200: 
    data = response.json()
    
    if data.get(str(game_id), {}).get('success'):
        game_info = data[str(game_id)]['data']
        
        if 'recommendations' in game_info:
            rating = game_info['recommendations']
            #prints the ammount of ratings the game has however it does not account for the good or bad
            print(f"Game Rating: {rating['total']} recommendations")
        else:
            print("No recommendations found.")
        #game info, discription, and price
        print(f"Game Name: {game_info.get('name')}")
        print(f"Description: {game_info.get('short_description')}")
        print(f"Price: {game_info.get('price_overview', {}).get('final_formatted')}")
        
    else:
        print("Game details not found.")
