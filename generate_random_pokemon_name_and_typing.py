import requests,random,json

num = random.randint(1, 1118)
r = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(num) + "/")
data = r.json()
final = json.loads(json.dumps(data))
print(final["forms"][0]["name"])#.dumps(data, indent=1))
for type in final["types"]:
	print(json.loads(json.dumps(type))["type"]["name"])

p = requests.get("https://pokeapi.co/api/v2/pokemon-species/" + str(final["forms"][0]["name"]) + "/")
dataP = p.json()
finalP = json.loads(json.dumps(dataP))
for pokedexNum in finalP["pokedex_numbers"]:
	if pokedexNum["pokedex"]["name"] != "national":
		print(pokedexNum["pokedex"]["name"])