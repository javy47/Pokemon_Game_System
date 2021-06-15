# from pokemon_data import Healing_Items
import sqlite3

conn = sqlite3.connect('pokemon.db')
db = conn.cursor()


class Trainer():
    """
    A class used to represent a trainer

    ....

    Attributes
    ----------

    name : str
        The name used to identify a user
    user_id : int
        a users database number
    pokemon_party : lst
        a list of pokemon objects
    
    Methods
    -------

    add_to_party(pokemon)
        adds a pokemon object to a players party list
    remove_from_party(pokemon)
        removes a pokemon object from a players party list
    heal_pokemon(pokemon)
        heals a pokemon by using an item    

    """

    def __init__(self, name, user_id, pokemon_party=None):

        """
        Parameters
        ----------
        name : str
            The name used to identify a user
        user_id : int
            a users database number
        pokemon_party : lst
            a list of pokemon objects

        """
        self.name = name
        self.id = user_id
        self.pokemon_party = pokemon_party
        self.num_fainted_pokemon = 0

    def __repr__(self):
        return f"Trainer({self.name},{self.id},{self.pokemon_party})"


    def __str__(self):
        print(f"Trainer: {self.name}\nPokemon Party:")
        if self.pokemon_party:
            for pokemon in self.pokemon_party:
                print(pokemon)
            return "Those are all the pokemon in your party"
        else:
            return "You current have no pokemon"

    def get_id(self):
        return self.id
    
    def get_pokemon(self, index):
        return self.pokemon_party[index]
    
    def update_team(self, updated_party):
        self.pokemon_party = updated_party
        print(self.pokemon_party)


    def change_name(self, new_name):
        self.name = new_name
    
    
    def add_to_party(self,pokemon):
        #If party is full(six pokemon) trainer can not add pokemon to the party
        if len(self.pokemon_party) == 6:
            print("Your party of pokemon is currently at capacity. If you wish to add a pokemon you need to remove one first")
        else:
            self.pokemon_party.append(pokemon)
            
            
    #removes a pokemon from a players party
    #if pokemon party size is greater than 0 then it will remove pokemon
    def remove_from_party(self,pokemon):
       if len(self.pokemon_party) > 0:
           self.pokemon_party.remove(pokemon)


    def heal_pokemon(self, pokemon_index, amount):
        return self.pokemon_party[pokemon_index].increase_hp(amount)


    def level_pokemon(self,pokemon_index, amount):
        return self.pokemon_party[pokemon_index].level_up()