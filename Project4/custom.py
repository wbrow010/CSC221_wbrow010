import requests
import plotly.express as px

url = "https://pokeapi.co/api/v2/pokemon/"

pokemon_data = []

# gets only the original 151 pokemon
for i in range(1, 152):
    response = requests.get(url + str(i))
    if response.status_code == 200:
        data = response.json()
        pokemon_data.append({
            "name": data["name"],
            "height": data["height"]
        })

sorted_pokemon = sorted(pokemon_data, key=lambda x: x["height"], reverse=True)

# Extracting data for visualization
pokemon_names = [pokemon['name'] for pokemon in sorted_pokemon[:10]]
pokemon_heights = [pokemon['height'] for pokemon in sorted_pokemon[:10]]

# Create a bar chart
fig = px.bar(x=pokemon_names, y=pokemon_heights, labels={'x': 'Pokemon', 'y': 'Height (dm)'}, title='Top 10 Tallest Pokémon')

# Show the chart
fig.show()