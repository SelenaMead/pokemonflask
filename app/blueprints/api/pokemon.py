import requests
import os



class Pokemon:
    calls = []
    base_url = 'https://pokeapi.co/api/v2/pokemon/'
    
    def __init__(self): 
        #self.api_version = f'data/{version}/weather'
        #self.api_key = '02435e511927d661b86684bcc096de53'
        self.data = None
        self.calls.append(self)
        
    def __repr__(self):
       return f'<APICall: works>'

    def deck(pokemon):
        cards = []
        cards.append(pokemon)
        print(cards)
    
    def types(deck):
        int = []
        
        
    def run(self, pokemon):
        print('Loading...')
        
        response = requests.get(f'{self.base_url}/{pokemon}')
        self.data = response.json()
    def pokemon_dictonary(self, pokemon_type, pokemon, pokemon_height, pokemon_weight, pokemon_ability):
         pokemon_dict = {"Name": pokemon.title(),
                        "Specialty": pokemon_type,
                        "Height": pokemon_height,
                        "Weight": pokemon_weight,
                        "Ability": pokemon_ability}
         return pokemon_dict
    # def specialties():
        # fire, water, grass, rock, electric, and other
pokedeck = Pokemon()  
def sent_data_type(name):
    pokedeck.run(name)   
    
    pokedeck.calls
    pokedeck.data
    pokemon_type = pokedeck.data['types'][0]['type']['name']
   
    return pokemon_type

def sent_data_description(name):
    pokedeck.run(name)
    pokedeck.calls
    pokedeck.data
    pokemon_height = pokedeck.data['height']
    pokemon_weight = pokedeck.data['weight']
    pokemon_ability = pokedeck.data["abilities"][0]["ability"]['name']

    return "Height: " + str(pokemon_height) + " weight: " + str(pokemon_weight) + " ability: " + pokemon_ability
