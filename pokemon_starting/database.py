import sqlite3
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('pokemon.db')
db = conn.cursor()

# #[GOOD TO GO]
# sql_create_trainer = db.execute("""CREATE TABLE trainer(
#     id integer PRIMARY KEY,
#     username text
    

# );""")
# #[GOOD TO GO]
# sql_create_join_pokemon_party = db.execute("""CREATE TABLE pokemon_party(
#     id integer PRIMARY KEY,
#     trainer_id integer,
#     pokemon_id integer,
#     FOREIGN KEY (trainer_id) REFERENCES trainer (id),
#     FOREIGN KEY (pokemon_id) REFERENCES pokemon (pokedex_id)

# );""")

# #Pokemon Table [GOOD TO GO]
# sql_create_pokemon_table = db.execute("""CREATE TABLE pokemon (
#     pokedex_id integer PRIMARY KEY,
#     name text NOT NULL,
#     level integer NOT NULL,
#     type1_id integer NOT NULL,
#     type2_id integer,
#     base_hp integer NOT NULL, 
# 	base_atk integer NOT NULL, 
# 	base_def integer NOT NULL, 
# 	base_spatk integer NOT NULL, 
# 	base_spdef integer NOT NULL,
# 	base_spe integer NOT NULL,
#     FOREIGN KEY (type1_id) REFERENCES pokemon_types (id),
#     FOREIGN KEY (type2_id) REFERENCES pokemon_types (id)
# );

# """)


# #Healing Items Table [GOOD TO GO]
# sql_create_hp_restoring_items = db.execute(""" CREATE TABLE hp_restoring_items (
#     id integer PRIMARY KEY,
#     name text NOT NULL UNIQUE,
#     description text NOT NULL,
#     healing_amount integer NOT NULL
# );""")

# #ALL HEALING ITEMS
# db.execute('INSERT INTO hp_restoring_items(name,description,healing_amount) VALUES ("Berry Juice","Restores 20 HP of a Pokémon.", 20)')
# db.execute('INSERT INTO hp_restoring_items(name,description,healing_amount) VALUES ("Energy Powder","Restores 60 HP, but lowers friendship of your Pokemon.", 60)')
# db.execute('INSERT INTO hp_restoring_items(name,description,healing_amount) VALUES ("Energy Root","Restores 120 HP, but lowers friendship of your Pokémon.", 120)')
# db.execute('INSERT INTO hp_restoring_items(name,description,healing_amount) VALUES ("Fresh Water","Restores 30 HP of a Pokémon.", 30)')
# db.execute('INSERT INTO hp_restoring_items(name,description,healing_amount) VALUES ("Full Restore","Restores HP to maximum and cures all status effects.", 1000)')
# db.execute('INSERT INTO hp_restoring_items(name,description,healing_amount) VALUES ("Hyper Potion","Restores 120 HP of a Pokémon.", 120)')
# db.execute('INSERT INTO hp_restoring_items(name,description,healing_amount) VALUES ("Lemonade","Restores 70 HP of a Pokémon.", 70)')
# db.execute('INSERT INTO hp_restoring_items(name,description,healing_amount) VALUES ("Max Potion","Restores HP to maximum", 1000)')
# db.execute('INSERT INTO hp_restoring_items(name,description,healing_amount) VALUES ("Moomoo Milk","Restores 10 HP of a Pokémon.", 100)')
# db.execute('INSERT INTO hp_restoring_items(name,description,healing_amount) VALUES ("Potion","Restores 20 HP of a Pokémon.", 20)')
# db.execute('INSERT INTO hp_restoring_items(name,description,healing_amount) VALUES ("Soda Pop","Restores 50 HP of a Pokémon.", 50)')
# db.execute('INSERT INTO hp_restoring_items(name,description,healing_amount) VALUES ("Super Potion","Restores 20 HP of a Pokémon.", 60)')
# db.execute('INSERT INTO hp_restoring_items(name,description,healing_amount) VALUES ("Sweet Heart","Restores 20 HP of a Pokémon.", 20)')
# #-------------------------------------------------------------------------------


# # sql_create_status = db.execute("""CREATE TABLE status(
# #     id integer PRIMARY KEY,
# #     name text NOT NULL,
# #     description text NOT NULL,
# #     effect
# # )""")

# # #ALL POKEMON STATUS

# #Pokemon Status Table 
# sql_create_pokemontype_table = db.execute("""CREATE TABLE pokemon_type(
#     id INTEGER PRIMARY KEY,
#     type text NOT NULL,
#     weakness text NOT NULL
# );""")
# #-------------------------------------------------------------------------------

# #ALL POKEMON TYPES:

# #FIRE (1-3)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("FIRE","WATER")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("FIRE","GROUND")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("FIRE","ROCK")')
# #WATER(4-5)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("WATER","ELECTRIC")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("WATER","GRASS")')
# #GRASS (6-10)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("GRASS","BUG")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("GRASS","FIRE")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("GRASS","FLYING")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("GRASS","ICE")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("GRASS","POISON")')
# #NORMAL(11)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("NORMAL","FIGHTING")')
# #FIGHTING (12-14)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("FIGHTING","FLYING")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("FIGHTING","FAIRY")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("FIGHTING","PSYCHIC")')
# #FLYING(15-18)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("FLYING","ROCK")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("FLYING","ELECTRIC")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("FLYING","ICE")')
# #POISON(19-20)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("POISON","GROUND")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("POISON","PSYCHIC")')
# #GROUND (21-23)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("GROUND","WATER")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("GROUND","GRASS")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("GROUND","ICE")')
# #ROCK (24-28)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("ROCK","GROUND")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("ROCK","FIGHTING")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("ROCK","STEEL")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("ROCK","WATER")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("ROCK","GRASS")')
# #BUGS (29-31)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("BUG","FLYING")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("BUG","ROCK")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("BUG","FIRE")')
# #GHOST (32-33)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("GHOST","GHOST")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("GHOST","DARK")')
# #STEEL (34-36)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("STEEL","GROUND")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("STEEL","FIGHTING")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("STEEL","FIRE")')
# #ELECTRIC (37)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("ELECTRIC","GROUND")')
# #PSYCHIC (38-40)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("PSYCHIC","BUG")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("PSYCHIC","GHOST")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("PSYCHIC","DARK")')
# #ICE (41-44)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("ICE","STEEL")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("ICE","FIRE")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("ICE","FIGHTING")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("ICE","ROCK")')
# #DRAGON (45-47)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("DRAGON","ICE")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("DRAGON","FAIRY")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("DRAGON","DRAGON")')
# #FAIRY (48-49)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("FAIRY","POISON")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("FAIRY","STEEL")')
# #DARK (50-52)
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("DARK","FIGHTING")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("DARK","BUG")')
# db.execute('INSERT INTO pokemon_type(type, weakness) VALUES ("DARK","FAIRY")')
# #-------------------------------------------------------------------------------


# #Starting off with the 10 original pokemon
# #-------------------------------------------------------------------------------
# db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("bulbasaur", 5, 6, 19,45,49,49,65,65,45)')
# db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("ivysaur", 5, 6,19, 60,62,63,80,80,60)')
# db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("venasaur", 5, 6,19, 80,82,83,100,100,80)')

# db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("charmander", 5, 1, 1, 39,52,43,60,50,65)')
# db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("charmeleon", 5, 1, 1, 58,64,58,80,65,80)')
# db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("charizard", 5, 1,15, 78,84,78,109,85,100)')

# db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("squirtle", 5, 4,4, 44,48,65,50,64,43)')
# db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("wartortle", 5, 4,4, 59,63,80,65,80,58)')
# db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("blastoise", 5, 4,4, 79,83,100,85,105,78)')

# db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("caterpie", 5, 29,29, 45,30,35,20,20,45)')


# #creating a demo user
# db.execute('INSERT INTO trainer(username) VALUES ("Javy")')

# #Pokemon party test
# db.execute('INSERT INTO pokemon_party (trainer_id,pokemon_id) VALUES (1,3)')
# db.execute('INSERT INTO pokemon_party (trainer_id,pokemon_id) VALUES (1,6)')





#Testing the data in the database



# db.execute('INSERT INTO pokemon_type VALUES ("FIRE","GROUND")')
db.execute('SELECT * FROM pokemon_type WHERE type="DARK"')
print(db.fetchall())
db.execute('SELECT * FROM pokemon  ')
print(db.fetchall())
db.execute('SELECT * FROM pokemon_party')
print(db.fetchall())
db.execute('SELECT * FROM trainer WHERE username= :user',{'user': "john"})
print(db.fetchone())

conn.commit()



conn.close()