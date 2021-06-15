import sqlite3
import random

conn = sqlite3.connect('pokemon.db')
db = conn.cursor()


class Pokemon():
    """
    A class used to represent a Pokemon

    ...

    Attributes
    ----------
    name : str
        The name of the pokemon creature
    level : int
        The power level of a pokemon. ranges from 1 to 100
    pokemon_type1 : str
        The primary Type given to a pokemon
    pokemon_type2 : str
        The secondary type for a given pokemon.
    base_hp : int
        The base health points for a given pokemon
    base_attack : int
        THe base physical attack value for a given pokemon
    base_defense : int
        The base physical defense value for a given pokemon
    base_spatk : int
        The base special attack value for a given pokemon
    base_spdef : int
        The base special defense value for a given pokemon
    base_speed : int
        The base speed value for a given pokemon(used to determine which pokemon attacks first)
    fainted : bool
        A flag used to determine if a pokemon can continue combat(default is False)

    Methods
    -------
    pokemon_weak_resist(type1,type2)
        Produces two list containing information on a pokemon's weakness and resistances
    level_up()
        Increases the level and stats of a pokemon
    decrease_hp(amount)
        lowers a pokemons current health points value by amount provided
    increase_hp(amount)
        increases a pokemons current health point value by amount provided
    revive()
        restores the health points of a pokemon that is fainted
    user_attack(attacker,opponent,*pokemon)
        THe active user uses this method for there pokemon to attack each other. Using a *args in the case of multiple pokemon being attacked
    ai_attack(attacker,opponent,*pokemon)
        during comabt this is called to simulate a second trainer giving commands to their pokemon
    move_selection(num, text)
        used to keep player choice within its proper boundary
    learn_move(name, power, damage_type)
        used to update instance attribute 'moves' with new moves determined by trainer
    pokemon_alive()
        changes a pokemons fainted state if their health point is <= 0
    get_hp()
        returns the current health points of a pokemon
    get_fainted()
        returns a pokemons current fainted state

    """
    def __init__(self, name, level, pokemon_type1, pokemon_type2, base_hp, base_attack, base_defense, base_spatk, base_spdef, base_speed, fainted=False):
        #Database Provided
        '''
        Parameters
        ----------
        name : str
            The name of the pokemon creature
        level : int
            The power level of a pokemon. ranges from 1 to 100
        pokemon_type1 : str
            The primary Type given to a pokemon
        pokemon_type2 : str
            The secondary type for a given pokemon.
        base_hp : int
            The base health points for a given pokemon
        base_attack : int
            THe base physical attack value for a given pokemon
        base_defense : int
            The base physical defense value for a given pokemon
        base_spatk : int
            The base special attack value for a given pokemon
        base_spdef : int
            The base special defense value for a given pokemon
        base_speed : int
            The base speed value for a given pokemon(used to determine which pokemon attacks first)
        fainted : bool
            A flag used to determine if a pokemon can continue combat(default is False)
        
        '''
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

        self.maximum_hp = base_hp
        self.current_hp = base_hp
        self.fainted = fainted

        #_pokemon_weakness
        self.weakness = []
        #_pokemon_resistance
        self.resistance = []

        #FIX: create a function that adds move to a pokemon. [limt being no more that 4 moves]
        self.moves = [{"name":"Tackle", "damage": 35, "damage_type": "Normal"}]
        self.maximum_level = 100

    
    def __str__(self):
        all_moves = ""
        for move in self.moves:
            all_moves = all_moves + move["name"]+"|"+ "Power:"+ str(move["damage"])+"\n"
     
        return f"Pokemon Name: {self.name.capitalize()}\nHP: {self.current_hp}/{self.maximum_hp}\nLevel: {self.level} \nType1: {self.pokemon_type1}\nType2: {self.pokemon_type2}\n----------\nWeakness:\n{self.weakness}\n----------\nResistance:\n{self.resistance}\n----------\nMoves:\n{all_moves}"

    def __repr__(self):
        return f"Pokemon({self.name},{self.level},{self.pokemon_type1},{self.pokemon_type2},{self.base_hp},{self.base_attack},{self.base_defense},{self.base_spatk},{self.base_defense},{self.base_speed})"


    def _pokemon_resistance(self, type1, type2):
        db.execute('SELECT resistance, immune FROM pokemon_resistance WHERE type= :type',{'type':type1 })
        type1_resistance = db.fetchall()

        for resist in type1_resistance:
            self.resistance.append({'type': resist[0], 'multiplier': .5})
             
        if type1 != type2:
            db.execute('SELECT resistance, immune FROM pokemon_resistance WHERE type= :type',{'type':type2 })
            type2_resistance = db.fetchall()
            
            temp = 0
            for resist2 in type2_resistance:
                for i in range(0,len(self.resistance)):

                    if resist2[0] == self.resistance[i]['type']:
                        self.resistance[i]['multiplier']*=.5
                        temp = i
                        break

                if resist2[0] != self.resistance[temp]['type']:  
                    if resist2[1] == "YES":
                        self.resistance.append({'type': resist2[0], 'multiplier': 0})
                    else:
                        self.resistance.append({'type': resist2[0], 'multiplier': .5})


    def _pokemon_weakness(self, type1, type2):
        db.execute('SELECT weakness FROM pokemon_type WHERE type= :type',{'type':type1 })
        type1_weakness = db.fetchall()

        for item in type1_weakness:
            self.weakness.append({'type': item[0], 'multiplier': 2})

        if type1 != type2:
            db.execute('SELECT weakness FROM pokemon_type WHERE type= :type',{'type':type2 })
            type2_weakness = db.fetchall()

            #Making sure that any overlapping weaknesses are stacked instead of showing up 2x
            temp = 0
            for typei in type2_weakness:
                for i in range(0,len(self.weakness)):
                   
                    if typei[0] == self.weakness[i]['type']:
                        self.weakness[i]['multiplier']*=2
                        
                        temp = i
                        break

                if typei[0] != self.weakness[temp]['type']:       
                    self.weakness.append({'type': typei[0], 'multiplier': 2})
    

    def pokemon_weak_resist(self, type1, type2):
        self._pokemon_weakness(type1,type2)
        self._pokemon_resistance(type1, type2)
       
        #Removing all false weaknesses
        for value in range(0,len(self.resistance)):
            for val in self.weakness:
                if self.resistance[value]['type']  == val['type']:
                    temp = self.weakness[self.weakness.index(val)]['multiplier']
                    self.weakness[self.weakness.index(val)]['multiplier']*=self.resistance[value]['multiplier']
                    self.resistance[value]['multiplier']*=temp

        modified_weakness = [weakness for weakness in self.weakness if weakness['multiplier'] >= 2]
        self.weakness = modified_weakness

        modified_resistance = [resistance for resistance in self.resistance if resistance['multiplier'] <= .5]
        self.resistance = modified_resistance
        

    def level_up(self):
        if self.level < self.maximum_level:
            self.level+=1
            #simplistic approach
            hp_base = random.randint(5,10)
            self.base_hp+=hp_base
            self.maximum_hp+=hp_base

            self.base_attack+= random.randint(3,4)
            self.base_defense+= random.randint(3,4)
            self.base_spatk+= random.randint(3,4)
            self.base_spdef+= random.randint(3,4)
            self.base_speed+= random.randint(3,4)
            print(f"{self.name} has gained a level")
            
        else:
            print("{pokemon} level  is already maxed and will not go any higher")

    
    def decrease_hp(self,amount):
        if self.fainted is False:

            if self.current_hp - amount <= 0:
                self.fainted = True
                self.current_hp = 0  
            else:
                self.current_hp-=amount
                return print(f"{self.name}'s HP has been reduced to {self.current_hp}/{self.maximum_hp}")

        print(f"Your pokemon {self.name} has fainted")

    
    def increase_hp(self,amount):
        if self.current_hp == self.maximum_hp:
            return f"Your {self.name} HP is already full \n"
        elif self.current_hp == 0:
            self.fainted = True
            return f"You can not use health point items on your Fainted {self.name} \n"
        elif (self.current_hp + amount) > self.maximum_hp:
            self.current_hp = self.maximum_hp
            return f"{self.name} has been healed to full hp \n"
        else:
            self.current_hp += amount
            return f"Your {self.name} has been healed by {amount}. Current HP is {self.current_hp}/{self.maximum_hp} \n"


    def revive(self):
        if self.fainted is True:
            self.current_hp = self.maximum_hp/2
        else:
            print("The item revive has no effect on pokemon not fainted")


    def user_attack(self,attacker, opponent,*pokemons):
        for i, move in enumerate(self.moves, start=1):
            print(f"{i}) Move Name: { move['name']} Power:{move['damage']}")

        move_number = self.move_selection(len(self.moves),f"What move would you want {self.name.title()} to use?: \n")
        
        # print(self.moves[move_number-1]["damage"])
        for pokemon in pokemons:
            #for Super Effective Moves 2x
            if self.moves[move_number-1]["damage_type"] in pokemon.weakness:
                print(f"{attacker.name}'s {self.name} attacks {opponent.name}'s {pokemon.name} for {self.moves[move_number-1]['damage'] * 2} damage")
                pokemon.decrease_hp(self.moves[move_number-1]["damage"] * 2)

            #for resistance .5 or.25
            elif self.moves[move_number-1]["damage_type"] in pokemon.resistance:
                index = pokemon.resistance.index(self.moves[move_number-1]["damage_type"].upper())
                print(f"{attacker.name}'s {self.name} attacks {opponent.name}'s {pokemon.name} for {self.moves[move_number-1]['damage'] * pokemon.resistance[index]['multiplier']} damage")
                pokemon.decrease_hp(self.moves[move_number-1]["damage"] * pokemon.resistance[index]['multiplier'] )

            #for Normal Damage 1x
            else:
                print(f"{attacker.name}'s {self.name} attacks {opponent.name}'s {pokemon.name} for {self.moves[move_number-1]['damage']} damage")
                pokemon.decrease_hp(self.moves[move_number-1]["damage"])


    def ai_attack(self, attacker, opponent,*pokemons):
        for pokemon in pokemons:
            #for Super Effective Moves 2x
            if self.moves[0]["damage_type"] in pokemon.weakness:
                print(f"**{attacker.name}'s {self.nam.title()} attacks {opponent.name}'s {pokemon.name.title()} for {self.moves[0]['damage'] * 2} damage**\n")
                pokemon.decrease_hp(self.moves[0]["damage"] * 2)

            # for resistance .25x .5x
            elif self.moves[0]["damage_type"] in pokemon.resistance:
                index = pokemon.resistance.index(self.moves[0]["damage_type"].upper())
                print(f"{attacker.name}'s {self.name.title()} attacks {opponent.name}'s {pokemon.name.title()} for {self.moves[0]['damage'] * pokemon.resistance[index]['multiplier']} damage")
                pokemon.decrease_hp(self.moves[0]["damage"] * pokemon.resistance[index]['multiplier'] )

            #for Normal Damage 1x
            else:
                print(f"{attacker.name}'s {self.name.title()} attacks {opponent.name}'s {pokemon.name.title()} for {self.moves[0]['damage']} damage")
                pokemon.decrease_hp(self.moves[0]["damage"])
    

    def move_selection(self,num, text):
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

    #-----------------------------------NEEDS WORK--------------------------------
    def learn_move(self, name, power, damage_type):
        for move in self.moves:
            if name == move["name"]:
                print("your pokemon already knows this move")
                return

        self.moves.append({"name": name, "damage": power, "damage_type": damage_type})
    #-------------------------------------------------------------------------------

    def pokemon_alive(self):
        if self.current_hp <= 0:
            self.fainted = True
        else:
            self.get_hp()


    def get_hp(self):
        return self.current_hp
    
    
    def get_max_hp(self):
        return self.maximum_hp


    def get_fainted(self):
        return self.fainted
    
    




