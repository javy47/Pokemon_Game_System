
#For each pokemon create their type with a dict so that you can have it tied to each weakness
#------------------------------------------------------------------------------------------------------------------------------------------------------
pokemon_types = [
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


# pokemon_resistance = []

# pokemon_csv = open('../pokemonresist.txt', "r")
# for poketype in pokemon_csv:
#     category, resist, immune = poketype.split(',')
#     pokemon_resistance.append({'type': category, 'resistance': resist, 'immune': immune})


