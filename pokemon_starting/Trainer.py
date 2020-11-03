# from pokemon_data import Healing_Items
import sqlite3

conn = sqlite3.connect('pokemon.db')
db = conn.cursor()

class Trainer():
    def __init__(self, name, user_id, pokemon_party=None):
        self.name = name
        self.id = user_id
        self.pokemon_party = pokemon_party
    
    def __repr__(self):
        #print trainers name and pokemon
        print("Trainer: {trainer}\nPokemon Party:".format(trainer=self.name))
        if self.pokemon_party is not None:
            for pokemon in self.pokemon_party:
                print(pokemon)
            return "Those are all the pokemon in your party"
        else:
            return "You current have no pokemon"

    #WORK ON THIS SO THAT IT WORKS WITH DB
    
    def add_to_party(self,pokemon):
        #If party is full(six pokemon) trainer can not add pokemon to the party
        if len(self.pokemon_party) == 6:
            print("Your party of pokemon is currently at capacity. If you wish to add a pokemon you need to remove one first")
        else:
            self.pokemon_party.append(pokemon)

    def heal_pokemon(self,pokemon):
        #Will take a healing item(has a specific amount of health it can heal)
        #pokemon.increase_hp(item.amount)
        db.execute("SELECT * FROM hp_restoring_items")
        healing_list = db.fetchall()
        print(healing_list)

        print("The following are all healing items available to the trainer: ")
        for item in healing_list:
            print("{num}) {name}: {description}\n".format(num=item[0],name=item[1], description=item[2]))
            
        
        choice = int(input("Which item do you want to use on {pokemon}".format(pokemon=pokemon.name)))
        
        print(pokemon.increase_hp(healing_list[choice-1][3]))