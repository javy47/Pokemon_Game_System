
import sqlite3
from Trainer import Trainer
from pokemon import Pokemon

conn = sqlite3.connect('pokemon.db')
db = conn.cursor()

#loads the trainers pokemon team
def trainer_party(trainer_id):
    """
    Uses a users databse id to query the pokemon and trainer database join table and return all results where
    the trainer id matches the current trainer. That data is then taken and used to construct a list of pokemon
    objects
    
    Keyword argument:
    trainer_id -- a users database id

    """

    db.execute('SELECT * FROM pokemon_party WHERE trainer_id= :trainer_id',{'trainer_id': trainer_id})
    pokemon_trainer_list = db.fetchall() 

    pokemon_party = []
    #If pokemon party_tranier list is empty prompt them to create their own team

    for pokemon in pokemon_trainer_list:

        db.execute('SELECT * FROM pokemon WHERE pokedex_id= :pokemon_id',{'pokemon_id':pokemon[2] })
        monster = db.fetchone()
        # print(monster)
        #Pokemon Name
        monster_name = monster[1]
        #Pokemon Level
        monster_level = monster[2]
        #First pokemon type
        monster_type1 = db.execute('SELECT type FROM pokemon_type WHERE id= :id', {'id': monster[3]}).fetchone()
        #second pokemon type
        monster_type2 = db.execute('SELECT type FROM pokemon_type WHERE id= :id', {'id': monster[4]}).fetchone()
        #pokemon base hp
        monster_hp = monster[5]
        #pokemon base attack
        monster_atk = monster[6]
        #pokemon base defense
        monster_def = monster[7]
        #pokemon base special attack
        monster_spatk = monster[8] 
        #pokemon base special defense
        monster_spdef = monster[9]
        #pokemon base speed
        monster_spe = monster[10]

        pkmn = Pokemon(monster_name, monster_level, monster_type1[0], monster_type2[0], monster_hp, monster_atk, monster_def, monster_spatk, monster_spdef, monster_spe)
        #assign all weakness and resistance to pokemon after their creation
        pkmn.pokemon_weak_resist(monster_type1[0],monster_type2[0])
      
        pokemon_party.append(pkmn)
    
    return pokemon_party


def user_selection(num, text):
    """
    Takes input from a user and only accepts inputs that are within the specified range 

    Keyword arguments:
    num -- the amount of choices available
    text -- the input text that a function wants to display in the terminal

    """
    lst = list(range(1,num+1))
    answer= 0
    while answer not in lst:
        try:
            answer = int(input(text))
            
            if answer not in range(1,num+1):
                raise ValueError
            break
        except ValueError:
            print('Select a valid Number')

    return answer


def display_pokemon(pokemon_party):
    """
    Displays to the terminal every pokemon in a users party

    Keyword argument:
    pokemon_party -- a list of pokemon objects pertaining to a particular trainer
    """
    
    for count, i in enumerate(pokemon_party, start=0):
        print(f"{count+1}){pokemon_party[count]}")


def healPokemon(user):
    """
    Using input from a user to determine which healing item they will use on a specified pokemon

    Keyword argument:
    user -- This is a trainer object 
    """

    display_pokemon(user.pokemon_party)

    #Ask which pokemon needs healing?
    pokemon_to_heal = user_selection(len(user.pokemon_party),f"Which Pokemon do you want to heal?(1-{len(user.pokemon_party)}):")

    #Ask which item to use
    db.execute("SELECT * FROM hp_restoring_items")
    medicine = db.fetchall()

    for count, item in enumerate(medicine):
        print(f"{count+1}) {item[1]}")
        
    medicine_to_use = user_selection(len(medicine), f"Which Healing Item do youy want to use?(1-{len(medicine)})")
    print(user.heal_pokemon(pokemon_to_heal-1, medicine[medicine_to_use][3]))