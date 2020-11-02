from pokemon_data import Healing_Items
class Trainer():
    def __init__(self, name, pokemon_party=None):
        self.name = name
        self.pokemon_party = pokemon_party
    
    def __repr__(self):
        #print trainers name and pokemon
        print("Trainer: {trainer}\nPokemon Party:".format(trainer=self.name))
        for pokemon in self.pokemon_party:
            print(pokemon)
        return "Those are all the pokemon n your party"

    def add_to_party(self,pokemon):
        #If party is full(six pokemon) trainer can not add pokemon to the party
        if len(self.pokemon_party) == 6:
            print("Your party of pokemon is currently at capacity. If you wish to add a pokemon you need to remove one first")
        else:
            self.pokemon_party.append(pokemon)

    def heal_pokemon(self,pokemon):
        #Will take a healing item(has a specific amount of health it can heal)
        #pokemon.increase_hp(item.amount)
        counter = 1
        print("The following are all healing items available to the trainer: ")
        for item in Healing_Items:
            print("{num}) {item}: heals for {amount} HP".format(num=counter,item=item["name"],amount=item["amount"]))
            counter+=1
        
        choice = int(input("Which item do you want to use on {pokemon}".format(pokemon=pokemon.name)))
        
        pokemon.increase_hp(Healing_Items[choice-1]["amount"])