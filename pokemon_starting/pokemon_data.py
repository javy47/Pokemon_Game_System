
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

pokemon_resistance = [
                    {'type': "NORMAL",'resistance': 'GHOST', 'immune': "YES" },

                    {'type': 'FIGHTING','resistance': 'ROCK', 'immune': "NO" },
                    {'type': 'FIGHTING','resistance': 'BUG', 'immune': "NO" },
                    {'type': 'FIGHTING','resistance': 'DARK', 'immune': "NO" },

                    {'type': "FLYING",'resistance': 'FIGHTING', 'immune': "NO" },
                    {'type': "FLYING",'resistance': 'BUG', 'immune': "NO" },
                    {'type': "FLYING",'resistance': 'GRASS', 'immune': "NO" },
                    {'type': "FLYING",'resistance': 'GROUND', 'immune': "YES" },

                    {'type': "POISON",'resistance': 'FIGHTING', 'immune': "NO" },
                    {'type': "POISON",'resistance': 'POISON', 'immune': "NO" },
                    {'type': "POISON",'resistance': 'GRASS', 'immune': "NO" },
                    {'type': "POISON",'resistance': 'FAIRY', 'immune': "NO" },
                    {'type': "POISON",'resistance': 'BUG', 'immune': "NO" },

                    {'type': "GROUND",'resistance': 'POISON', 'immune': "NO" },
                    {'type': "GROUND",'resistance': 'ROCK', 'immune': "NO" },
                    {'type': "GROUND",'resistance': 'ELECTRIC', 'immune': "YES" },

                    {'type': "ROCK",'resistance': 'NORMAL', 'immune': "NO" },
                    {'type': "ROCK",'resistance': 'FLYING', 'immune': "NO" },
                    {'type': "ROCK",'resistance': 'POISON', 'immune': "NO" },
                    {'type': "ROCK",'resistance': 'FIRE', 'immune': "NO" },

                    {'type': "BUG",'resistance': 'FIGHTING', 'immune': "NO" },
                    {'type': "BUG",'resistance': 'GROUND', 'immune': "NO" },
                    {'type': "BUG",'resistance': 'GRASS', 'immune': "NO" },

                    {'type': "GHOST",'resistance': 'POISON', 'immune': "NO" },
                    {'type': "GHOST",'resistance': 'BUG', 'immune': "NO" },
                    {'type': "GHOST",'resistance': 'NORMAL', 'immune': "YES" },
                    {'type': "GHOST",'resistance': 'FIGHTING', 'immune': "YES" },

                    {'type': "STEEL",'resistance': 'POISON', 'immune': "YES" },
                    {'type': "STEEL",'resistance': 'NORMAL', 'immune': "NO" },
                    {'type': "STEEL",'resistance': 'FLYING', 'immune': "NO" },
                    {'type': "STEEL",'resistance': 'ROCK', 'immune': "NO" },
                    {'type': "STEEL",'resistance': 'BUG', 'immune': "NO" },
                    {'type': "STEEL",'resistance': 'STEEL', 'immune': "NO" },
                    {'type': "STEEL",'resistance': 'GRASS', 'immune': "NO" },
                    {'type': "STEEL",'resistance': 'PSYCHIC', 'immune': "NO" },
                    {'type': "STEEL",'resistance': 'ICE', 'immune': "NO" },
                    {'type': "STEEL",'resistance': 'DRAGON', 'immune': "NO" },
                    {'type': "STEEL",'resistance': 'FAIRY', 'immune': "NO" },

                    {'type': "FIRE",'resistance': 'BUG', 'immune': "NO" },
                    {'type': "FIRE",'resistance': 'STEEL', 'immune': "NO" },
                    {'type': "FIRE",'resistance': 'FIRE', 'immune': "NO" },
                    {'type': "FIRE",'resistance': 'GRASS', 'immune': "NO" },
                    {'type': "FIRE",'resistance': 'ICE', 'immune': "NO" },
                    {'type': "FIRE",'resistance': 'FAIRY', 'immune': "NO" },

                    {'type': "WATER",'resistance': 'STEEL', 'immune': "NO" },
                    {'type': "WATER",'resistance': 'FIRE', 'immune': "NO" },
                    {'type': "WATER",'resistance': 'WATER', 'immune': "NO" },
                    {'type': "WATER",'resistance': 'ICE', 'immune': "NO" },

                    {'type': "GRASS",'resistance': 'GROUND', 'immune': "NO" },
                    {'type': "GRASS",'resistance': 'WATER', 'immune': "NO" },
                    {'type': "GRASS",'resistance': 'GRASS', 'immune': "NO" },
                    {'type': "GRASS",'resistance': 'ELECTRIC', 'immune': "NO" },

                    {'type': "ELECTRIC",'resistance': 'FLYING', 'immune': "NO" },
                    {'type': "ELECTRIC",'resistance': 'STEEL', 'immune': "NO" },
                    {'type': "ELECTRIC",'resistance': 'ELECTRIC', 'immune': "NO" },

                    {'type': "PSYCHIC",'resistance': 'FIGHTING', 'immune': "NO" },
                    {'type': "PSYCHIC",'resistance': 'PSYCHIC', 'immune': "NO" },

                    {'type': "ICE",'resistance': 'ICE', 'immune': "NO" },

                    {'type': "DRAGON",'resistance': 'FIRE', 'immune': "NO" },
                    {'type': "DRAGON",'resistance': 'WATER', 'immune': "NO" },
                    {'type': "DRAGON",'resistance': 'GRASS', 'immune': "NO" },
                    {'type': "DRAGON",'resistance': 'ELECTRIC', 'immune': "NO" },

                    {'type': "FAIRY",'resistance': 'FIGHTING', 'immune': "NO" },
                    {'type': "FAIRY",'resistance': 'BUG', 'immune': "NO" },
                    {'type': "FAIRY",'resistance': 'DARK', 'immune': "NO" },
                    {'type': "FAIRY",'resistance': 'DRAGON', 'immune': "YES" },

                    {'type': "DARK",'resistance': 'GHOST', 'immune': "NO" },
                    {'type': "DARK",'resistance': 'DARK', 'immune': "NO" },
                    {'type': "DARK",'resistance': 'PSYCHIC', 'immune': "YES" }
                    ]



