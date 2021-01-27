import sqlite3
from Trainer import Trainer
from pokemon_data import Pokemon_Types
import random

conn = sqlite3.connect('pokemon.db')
db = conn.cursor()


#creating a class for pokemon
class Pokemon():
    def __init__(self, name, level, pokemon_type1, pokemon_type2, base_hp, base_attack, base_defense, base_spatk, base_spdef, base_speed, fainted=False):
        #Database Provided
        self.name = name
        self.level = level
        self.pokemon_type1 = pokemon_type1
        self.pokemon_type2 = pokemon_type2
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.base_spatk = base_spatk
        self.base_spdef = base_spdef
        self.base_speed = base_speed

        #Automatically Provided
        self.maximum_hp = base_hp
        self.current_hp = base_hp
        self.fainted = fainted

        #Add Description for pokemon moves later
        self.moves = [{"name":"Tackle", "damage": 35, "damage_type": "Normal"}]
        self.maximum_level = 100

        #Create a function to assign weakness
        self.weakness = []

        #Work on this later --need to make this more robust
            # self.nature = nature
            # self.phy_atk = phy_atk
            # self.defense = defense
        
    # Returns all data on the pokemon that a user is printing
    def __repr__(self):
        all_moves = ""
        for move in self.moves:
            all_moves = all_moves + move["name"]+"|"+ "Power:"+ str(move["damage"])+"\n"

        return "Pokemon Name: {name} \nHP: {current_hp}/{max_hp}\nLevel: {level} \nType1: {pokemon_type1}\nType2: {pokemon_type2}\n---------------\nWeakness:\n{weakness}\n---------------\nMoves:\n{Moves}".format(
            name= self.name.capitalize() ,current_hp=self.current_hp,max_hp=self.maximum_hp, level = self.level, pokemon_type1 = self.pokemon_type1,pokemon_type2= self.pokemon_type2,weakness=self.weakness, Moves=all_moves)

    #Used to assign each pokemon with a weakness
    def pokemon_weakness(self, type1, type2):
       
        db.execute('SELECT weakness FROM pokemon_type WHERE type= :type',{'type':type1 })
        type1_weakness = db.fetchall()

        for item in type1_weakness:
            self.weakness.append({'type': item[0], 'multiplier': 2})

        db.execute('SELECT weakness FROM pokemon_type WHERE type= :type',{'type':type2 })
        type2_weakness = db.fetchall()

        #Making sure that any overlapping weaknesses are stacked instead of showin gup 2x
        temp = 0
        for typei in type2_weakness:
            for i in range(0,len(self.weakness)):
                print(self.weakness[i]['type'])
                if typei[0] == self.weakness[i]['type']:
                    self.weakness[i]['multiplier']*=2
                    # print('There is a duplicate of TYPE:'+self.weakness[i]['type'])
                    temp = i
                    break

            if typei[0] != self.weakness[temp]['type']:       
                self.weakness.append({'type': typei[0], 'multiplier': 2})
        
        #Time to take the pokemon resistances into account
        #  db.execute('SELECT resistance FROM pokemon_type WHERE type= :type',{'type':type2 })
        
     


    #When a pokemon gains enough exp its level should go up. This function does exactly that. This method should not work after lvl 100
    # Simplistic version of leveling up for now
    def level_up(self):
        if self.level < self.maximum_level:
            self.level+=1
            #simplistic approach
            self.base_hp+= random.randint(5,10)
            self.base_attack+= random.randinit(3,4)
            self.base_defense+= random.randinit(3,4)
            self.base_spatk+= random.randinit(3,4)
            self.base_spdef+= random.randinit(3,4)
            self.base_speed+= random.randinit(3,4)
            print("{pokemon} has gained a level".format(pokemon=self.name))
        else:
            print("{pokemon} level  is already maxed and will not go any higher")

    #This method will decrease the pokemons HP value by the amount given. Before that check can occurs the code checks to see if the pokemon is already fainted
    def decrease_hp(self,amount):
        if self.fainted is False:

            if self.current_hp - amount <= 0:
                self.fainted = True
                self.current_hp = 0
                
            else:
                self.current_hp-=amount
                return print("{Pokemon}'s HP has droped to {HP}/{MaxHP}".format(Pokemon=self.name, HP=self.current_hp,MaxHP=self.maximum_hp))
        print("Your pokemon {Pokemon} has fainted and cannot lose anymore hp".format(Pokemon=self.name))

    #This method will increase the pokemons HP value by the amount given if its Fainted Value is . Before that check can occurs the code checks to see if the pokemon is already fainted
    def increase_hp(self,amount):
     
        if self.current_hp == self.maximum_hp:
            return "Your pokemons HP is already full"
        elif self.current_hp == 0:
            self.fainted = True
            return "You can not use recovery items on Fainted Pokemon"
        elif (self.current_hp + amount) > self.maximum_hp:
            self.current_hp = self.maximum_hp
            return "your pokemon hp has increased"
        else:
            self.current_hp += amount
            return "Your pokemon has been healed"

    #If the pokemon is fainted then this method will function.
    def revive(self):
        if self.fainted is True:
            self.current_hp = self.maximum_hp/2
        else:
            print("The item revive has no effect on pokemon not fainted")


#---------------------------------------
    #Used for pokemon to attack each other. Using a *args in the case of multiple pokemon being attacked
    def attack(self,*pokemons):
        i=1
        for move in self.moves:
            print("{move}) Move Name:{name} Power:{power}".format(move=i, name=move["name"], power=move["damage"]))
            i+=1

        move_number = int(input("What move would you want {pokemon} to use?".format(pokemon=self.name)))
        # print(self.moves[move_number-1]["damage"])
        for pokemon in pokemons:
            #for Super Effective Moves 2x
            if self.moves[move_number-1]["damage_type"] in pokemon.pokemon_type["weakness"]:
                print("{Attacker} attacked {Victim} for {Damage} Damage".format(Attacker=self.name,Victim=pokemon.name,Damage=self.moves[move_number-1]["damage"] * 2) )
                pokemon.decrease_hp(self.moves[move_number-1]["damage"] * 2)

            #Add Elif later for resistance 1.2x

            #for Normal Damage 1x
            else:
                print("{Attacker} attacked {Victim} for {Damage} Damage \n".format(Attacker=self.name,Victim=pokemon.name,Damage=self.moves[move_number-1]["damage"]) )
                pokemon.decrease_hp(self.moves[move_number-1]["damage"])
                
    
    def learn_move(self, name, power, damage_type):
        for move in self.moves:
            if name == move["name"]:
                print("your pokemon already knows this move")
                return

        self.moves.append({"name": name, "damage": power, "damage_type": damage_type})
                      

#------------------------------------------------------------------------------------------------------------------------------------------------------                
#Testing the Pokemon Type
# print(Pokemon_Types[0]["type"])

#Testing Pokemon Class
#----------------------------------------------------------------------------------------------------


# Chimchar = Pokemon("Chimchar",5,"Fire",55,55,"Jolly")
# Bulbasaur = Pokemon("Bulbasaur",5,"Grass",55,55,"Calm")
# Psyduck = Pokemon("Psyduck",5,"Water",55,55,"Jolly")
# AshKetchum = Trainer("Ash",[Chimchar,Bulbasaur,Psyduck])
# print(AshKetchum)

# Chimchar.attack(Bulbasaur)
# AshKetchum.heal_pokemon(Bulbasaur)


# print(Chimchar)
# print(Bulbasaur)

# Chimchar.attack(Bulbasaur)
# Bulbasaur.learn_move("Razer Leaf", 35, "Grass")

# Bulbasaur.attack(Chimchar, Psyduck)

# print(Chimchar)
# print(Bulbasaur)
# print(Psyduck)

