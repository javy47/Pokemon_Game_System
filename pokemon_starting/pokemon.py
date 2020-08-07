
#Creating a Trainer Class
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


#creating a class for pokemon
class Pokemon():
    def __init__(self, name, level, pokemon_type, maximum_hp, current_hp, nature, fainted=False, phy_atk=4, defense=4):
        self.name = name
        self.level = level
        self.pokemon_type = self.assign_type(pokemon_type)
        self.maximum_hp = maximum_hp
        self.current_hp = current_hp
        self.fainted = fainted
        #Add Description for pokemon moves later
        self.moves = [{"name":"Tackle", "damage": 35, "damage_type": "Normal"}]

        #Work on this later
        self.nature = nature
        self.phy_atk = phy_atk
        self.defense = defense
        
    
    def __repr__(self):
        all_moves = ""
        for move in self.moves:
            all_moves = all_moves + move["name"]+"|"+ "Power:"+ str(move["damage"])+"\n"

        return "Pokemon Name: {name} \nHP: {current_hp}/{max_hp}\nLevel: {level} \nType: {pokemon_type} \nNature: {nature}\n---------------\nMoves:\n{Moves}".format(name= self.name,current_hp=self.current_hp,max_hp=self.maximum_hp, level = self.level, pokemon_type = self.pokemon_type,nature=self.nature, Moves=all_moves)

    def assign_type(self,pokemon_type):
        for pk_type in Pokemon_Types:
            if pk_type["type"] == pokemon_type:
                return pk_type
            
    #When a pokemon gains enough exp its level should go up. This function does exactly that
    def level_up(self):
        self.level+=1
        print("{pokemon} has gained a level".format(pokemon=self.name))

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
        else:
            self.current_hp += amount

    #If the pokemon is fainted then this method will function.
    def revive(self):
        if self.fainted is True:
            self.current_hp = self.maximum_hp/2
        else:
            print("The item revive has no effect on pokemon not fainted")

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
                      
#For each pokemon create their type with a dict so that you can have it tied to each weakness
#------------------------------------------------------------------------------------------------------------------------------------------------------
Pokemon_Types = [
                    {"type": "Fire" ,"weakness":["Water","Ground","Rock"]},
                    {"type": "Water","weakness":["Electric","Grass"]},
                    {"type": "Grass" ,"weakness":["Bug","Fire","Flying","Ice","Poison"]},
                    {"type": "Normal","weakness":["Fighting"]},
                    {"type": "Fighting","weakness":["Flying","Psychic","Fairy"]},
                    {"type": "Flying","weakness":["Rock","Electric","Ice"]},
                    {"type": "Poison","weakness":["Ground","Psychic"]},
                    {"type": "Ground","weakness":["Water","Grass","Ice"]},
                    {"type": "Rock","weakness":["Fighting","Ground","Steel", "Water", "Grass"]},
                    {"type": "Bug","weakness":["Flying", "Rock", "Fire"]},
                    {"type": "Ghost","weakness":["Ghost", "Dark"]},
                    {"type": "Steel","weakness":["Fighting", "Ground", "Fire"]},
                    {"type": "Electric","weakness":["Ground"]},
                    {"type": "Psychic","weakness":["Bug","Ghost","Dark"]},
                    {"type": "Ice","weakness":["Fighting","Rock","Steel","Fire"]},
                    {"type": "Dragon","weakness":["Ice", "Dragon", "Fairy"]},
                    {"type": "Fairy","weakness":["Poison", "Steel"]},
                    {"type": "Dark","weakness":["Fighting","Bug","Fairy"]},
                ]
Healing_Items = [{"name": "potion", "amount": 20}]
#------------------------------------------------------------------------------------------------------------------------------------------------------                
#Testing the Pokemon Type
# print(Pokemon_Types[0]["type"])

#Testing Pokemon Class
#----------------------------------------------------------------------------------------------------


Chimchar = Pokemon("Chimchar",5,"Fire",55,55,"Jolly")
Bulbasaur = Pokemon("Bulbasaur",5,"Grass",55,55,"Calm")
Psyduck = Pokemon("Psyduck",5,"Water",55,55,"Jolly")
AshKetchum = Trainer("Ash",[Chimchar,Bulbasaur,Psyduck])
print(AshKetchum)

Chimchar.attack(Bulbasaur)
AshKetchum.heal_pokemon(Bulbasaur)


# print(Chimchar)
print(Bulbasaur)

# Chimchar.attack(Bulbasaur)
# Bulbasaur.learn_move("Razer Leaf", 35, "Grass")

# Bulbasaur.attack(Chimchar, Psyduck)

# print(Chimchar)
# print(Bulbasaur)
# print(Psyduck)

