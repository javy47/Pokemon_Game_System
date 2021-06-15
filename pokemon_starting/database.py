from pokemon_data import pokemon_types, pokemon_resistance
from itemsinfo import healing_items
import sqlite3



# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('pokemon.db')
db = conn.cursor()

#[GOOD TO GO]

# Execute the creation of a user to the database
sql_create_trainer = db.execute("""CREATE TABLE trainer(
    id integer PRIMARY KEY,
    username text
    
);""")

#[GOOD TO GO]
sql_create_join_pokemon_party = db.execute("""CREATE TABLE pokemon_party(
    id integer PRIMARY KEY,
    trainer_id integer,
    pokemon_id integer,
    FOREIGN KEY (trainer_id) REFERENCES trainer (id),
    FOREIGN KEY (pokemon_id) REFERENCES pokemon (pokedex_id)

);""")

#Pokemon Table [GOOD TO GO]
sql_create_pokemon_table = db.execute("""CREATE TABLE pokemon (
    pokedex_id integer PRIMARY KEY,
    name text NOT NULL,
    level integer NOT NULL,
    type1_id integer NOT NULL,
    type2_id integer,
    base_hp integer NOT NULL, 
	base_atk integer NOT NULL, 
	base_def integer NOT NULL, 
	base_spatk integer NOT NULL, 
	base_spdef integer NOT NULL,
	base_spe integer NOT NULL,
    FOREIGN KEY (type1_id) REFERENCES pokemon_types (id),
    FOREIGN KEY (type2_id) REFERENCES pokemon_types (id)
);

""")


#Healing Items Table [GOOD TO GO]
sql_create_hp_restoring_items = db.execute(""" CREATE TABLE hp_restoring_items (
    id integer PRIMARY KEY,
    name text NOT NULL UNIQUE,
    description text NOT NULL,
    healing_amount integer NOT NULL
);""")


#ALL HEALING ITEMS   -- Adds all healing items to the database
for item in healing_items:
    db.execute(f"INSERT INTO hp_restoring_items(name,description,healing_amount) VALUES ('{item['name']}','{item['description']}',{int(item['value'])});")


#Pokemon Type Table 2x Effective
sql_create_pokemontype_table = db.execute("""CREATE TABLE pokemon_type(
    id INTEGER PRIMARY KEY,
    type text NOT NULL,
    weakness text NOT NULL
);""")

#ALL POKEMON TYPES:

#FIRE (1-3) # #WATER(4-5) # #GRASS (6-10) #NORMAL(11) #FIGHTING (12-14) #FLYING(15-17)
#POISON(18-19) #GROUND (20-22) #ROCK (23-27) #BUGS (28-30) #GHOST (31-332) #STEEL (33-35) 
#ELECTRIC (36) #PSYCHIC (37-39) #ICE (40-43) #DRAGON (44-46) #FAIRY (47-48) #DARK (49-51)

for poketype in pokemon_types:
    for weakness in poketype['weakness']:
        db.execute(f"INSERT INTO pokemon_type(type, weakness) VALUES ('{poketype['type'].upper()}','{weakness.upper()}');")

#-------------------------------------------------------------------------------

#Pokemon Resistances 1/2x Effective

sql_create_pokemonresistance_table = db.execute("""CREATE TABLE pokemon_resistance(
    id INTEGER PRIMARY KEY,
    type text NOT NULL,
    resistance text NOT NULL,
    immune text NOT NULL
);""")

for resist in pokemon_resistance:
    db.execute(f"INSERT INTO pokemon_resistance(type, resistance, immune) VALUES ({resist['type'].upper()},{resist['resistance'].upper()},{resist['immune'].upper()});")


#Starting off with the 10 original pokemon
#-------------------------------------------------------------------------------
db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("bulbasaur", 5, 6, 19,45,49,49,65,65,45)')
db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("ivysaur", 5, 6,19, 60,62,63,80,80,60)')
db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("venasaur", 5, 6,19, 80,82,83,100,100,80)')

db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("charmander", 5, 1, 1, 39,52,43,60,50,65)')
db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("charmeleon", 5, 1, 1, 58,64,58,80,65,80)')
db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("charizard", 5, 1,15, 78,84,78,109,85,100)')

db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("squirtle", 5, 4,4, 44,48,65,50,64,43)')
db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("wartortle", 5, 4,4, 59,63,80,65,80,58)')
db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("blastoise", 5, 4,4, 79,83,100,85,105,78)')

db.execute('INSERT INTO pokemon(name,level,type1_id,type2_id,base_hp,base_atk,base_def,base_spatk,base_spdef,base_spe) VALUES ("caterpie", 5, 29,29, 45,30,35,20,20,45)')


#creating a demo user
db.execute('INSERT INTO trainer(username) VALUES ("Javy")')
db.execute('INSERT INTO trainer(username) VALUES ("Voltsy")')

#Pokemon party test
db.execute('INSERT INTO pokemon_party (trainer_id,pokemon_id) VALUES (1,3)')
db.execute('INSERT INTO pokemon_party (trainer_id,pokemon_id) VALUES (1,6)')
db.execute('INSERT INTO pokemon_party (trainer_id,pokemon_id) VALUES (1,9)')

db.execute('INSERT INTO pokemon_party (trainer_id,pokemon_id) VALUES (2,9)')
db.execute('INSERT INTO pokemon_party (trainer_id,pokemon_id) VALUES (2,1)')





#Testing the data in the database



# db.execute('INSERT INTO pokemon_type VALUES ("FIRE","GROUND")')
# db.execute('SELECT * FROM pokemon_type WHERE type="DARK"')
# print(db.fetchall())
# db.execute('SELECT * FROM pokemon  ')
# print(db.fetchall())
# db.execute('SELECT * FROM pokemon_party')
# print(db.fetchall())
# db.execute('SELECT * FROM trainer WHERE username= :user',{'user': "john"})
# print(db.fetchone())

# db.execute('SELECT * FROM hp_restoring_items ')
# print(db.fetchall())

db.execute('SELECT * FROM pokemon_type ')
print(db.fetchall())

db.execute('SELECT * FROM pokemon_resistance ')
print(db.fetchall())
conn.commit()



conn.close()