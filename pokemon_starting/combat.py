import sqlite3
from Trainer import Trainer
from pokemon import Pokemon
from partycreator import *

conn = sqlite3.connect('pokemon.db')
db = conn.cursor()


def load_enemy(enemy_id):
    """
    creates a trainer object that will conduct battle with the user

    keyword argument:
    enemy_id -- the id of the account that a user wants to fight
    """
    db.execute(f"SELECT * FROM trainer WHERE id={enemy_id}")
    enemy = db.fetchone()

    pokemon_party = trainer_party(enemy[0])
    user_2 = Trainer(enemy[1],enemy[0], pokemon_party)
    return user_2


def battle(player1, player2):
    """
    The user and the ai will both participate in turn base battle with their pokemon
    until one player is out of pokemon.The user can either attack or heal their pokemon once per turn

    keyword arguments:
    player1 -- the current user's trainer object
    player2 -- the ai's trainer object

    """
    print(f"-----{player1.name} VS {player2.name}-----")
    p1_active = player1.pokemon_party[0]
    p2_active = player2.pokemon_party[0]

    turns = 1
    while True:
        print(f"-----This is Turn #{turns}-----\n")
        if player_lost(player1):
            break
        if player_lost(player2):
            break
            
        #Check which pokemon is faster
        # first_attacker, second_attacker = speed_comparison(p1_active,p2_active)
        
        p1_answer = combat_choice()
        if p1_answer == 1:
            print(f"----- It is now {player1.name} Turn -----\n")
            p1_active.user_attack(player1, player2, p2_active)
            if p2_active.fainted:
                    player2.num_fainted_pokemon+=1
                    if player_lost(player2):
                        break
                    p2_active = auto_switch_pokemon(player2)
            else:
                print(f"----- It is now {player2.name} Turn -----\n")
                p2_active.ai_attack(player2, player1, p1_active)
                if p1_active.fainted:
                    player1.num_fainted_pokemon+=1
                    if player_lost(player1):
                        break
                    p1_active = switch_pokemon(player1)
            turns+=1
        else:
            print(f"----- It is now {player1.name} Turn -----\n")
            healPokemon(player1)
            print(f"----- It is now {player2.name} Turn -----\n")
            p2_active.ai_attack(player2, player1,p1_active)
            if p1_active.fainted:
                player1.num_fainted_pokemon+=1
                p1_active = switch_pokemon(player1)
            turns+=1


def player_lost(player):
    """
    This function check to see if all of a player's pokemon are fainted.
    Returns True or False

    keyword argument:
    player -- the trainer object
    """
    if player.num_fainted_pokemon == len(player.pokemon_party):
        result(player.name)
        return True
    
    return False

#called to produce the outcome of the battle
def result(player_name):
    """
    Prints out a message notifying who the loser of the match is

    keyword argument:
    player_name -- the name of the trainer object that lost the battle
    """
    print(f"{player_name} has lost this match best of luck next time \n")


#Compares the speed stats of the current active pokemons
def speed_comparison(pokemon1, pokemon2):
    """
    Determines which pokemon is faster

    keyword arguments:
    pokemon1 -- the current active pokemon of player 1
    pokemon2 -- the current active pokemon of the ai
    """
    if pokemon1.base_speed >= pokemon2.base_speed:
        first_go = pokemon1
        second_go = pokemon2
    else:
        first_go = pokemon2
        second_go = pokemon1
    
    return first_go, second_go
        
#replaces the active pokemon with a pokemon from the trainer party that is not fainted

def auto_switch_pokemon(player):
    """
    Changes the ai's pokemon after one of its pokemon faints

    keyword argument:
    player -- the ai's player object
    """
    print(f"---- {player.name} is switching pokemon ----")
    non_fainted = [pokemon for pokemon in player.pokemon_party if  not pokemon.fainted ]
    index = player.pokemon_party.index(non_fainted[0])
    print(f"{player.name} sends out")
    return player.pokemon_party[index]


def switch_pokemon(player):
    """
    Changes the user's pokemon after one of its pokemon faints

    keyword argument:
    player -- the user's player object
    """
    print(f"---- {player.name} is switching pokemon ----")
    non_fainted = [pokemon for pokemon in player.pokemon_party if  not pokemon.fainted ]
    display_pokemon(non_fainted)

    if len(non_fainted) > 1:
        answer = user_selection(len(non_fainted),f"Which pokemon do you want to switch to?(1-{len(non_fainted)}): ")
        index = player.pokemon_party.index(non_fainted[answer-1])
        return player.pokemon_party[index]
    
    if len(non_fainted) == 1:
        index = player.pokemon_party.index(non_fainted[0])
        return player.pokemon_party[index]
    
    

#lets a player decide if they want to heal or attack their opponent
def combat_choice():
    """
    Lets the user decide between attacking or healing
    """
    print("1)Attack \n2)Heal")
    return  user_selection(2,"What do you want to do?(1 or 2): ")
