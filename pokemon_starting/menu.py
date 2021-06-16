import sqlite3
from Trainer import Trainer
from pokemon import Pokemon
from combat import *
from partycreator import *

conn = sqlite3.connect('pokemon.db')
db = conn.cursor()


def create_user():
    """Prompts a new user to setup their account. Once all their information is established, they are added to the database"""

    print("create user function")
    username= input('Please Enter a Trainer Name ')

    db.execute('SELECT username FROM trainer WHERE username= :user',{'user': username})
    test_name=db.fetchone()

    if not test_name:
        db.execute('INSERT INTO trainer (username) VALUES (:user)',{'user': username})
        conn.commit()

        db.execute('SELECT * FROM trainer WHERE username= :username',{'username': username})
        name = db.fetchone()

        create_party(name[0])
        pokemon_party = trainer_party(name[0])
        user = Trainer(name[1], name[0],pokemon_party)
        
        main_menu(user)

    else:
        print('---- SORRY USERNAME TAKEN ----')
        create_user()


#need to account for wrong input
def load_user():
    """
    An attempt is made to access the database base on the name a user enters. 
    If successful that users database information is used to construct a Trainer object
    """

    print("----- Loading User -----")
    username= input('Enter the username of your account: ')

    db.execute('SELECT * FROM trainer WHERE username= :username',{'username': username})
    name = db.fetchone()

    if not name:
        print(f'Account {username} does not exist. \n')
        main()
  
    pokemon_party = trainer_party(name[0])
    user = Trainer(name[1], name[0], pokemon_party)
    main_menu(user)


#constructs a trainers team
def create_party(id):
    """
    A user is prompted to select up to 6 pokemon from all pokemon in the database.
    Once all pokemon are selected, the pokemon and trainer id are added to pokemon_party table.

    Keyword argument:
    id -- A users database identification number

    """
   
    print('------ Creating Pokemon Team --------')
    answer = user_selection(6, 'How many pokemon would you like to add to your team?(1-6)')

    #quary all the pokemon in the database and display them
    db.execute('SELECT * FROM pokemon')
    pkmn_db = db.fetchall()
    print(len(pkmn_db))

    for pokemon in pkmn_db:
        print(f"{pokemon[0]}) {pokemon[1]}")

    for i in range(answer):
        answer = user_selection(len(pkmn_db), f'Which Pokemon do you want to add to your team?(1-{len(pkmn_db)}):')
        db.execute(f"INSERT INTO pokemon_party (trainer_id,pokemon_id) VALUES ({id},{answer})")
        conn.commit()
         

def main_menu(user=None):
    """
    Once a user has selected a character. 
    They are promtped with several options for battle, training, healing, or exiting the program
    
    Keyword argument:
    user -- This is a trainer object which is passed

    """
    options = [ 'Battle: [Try your skills with some combat between rivals]',
                'Train Pokemon: [Increase the combat prowess of your Pokemon]',
                'Heal: [Heal Your pokemon back into tip top shape]',
                'Exit Game\n'
                ]            
    while True:
        print(f'----- Welcome {user.name}, what would you like to do? ----- \n')

        for i, option in enumerate(options, start=1):
            print(str(i)+") "+option)
        
        text= f'What would you like to do?(1-{len(options)})'
        answer = user_selection(5, text)

        if answer == 1:
            print("Combat coming soon!!!!!")
            enemy = load_enemy(2)
            battle(user, enemy)
        elif answer == 2:
            if user.num_fainted_pokemon == len(user.pokemon_party):
                print("All of your pokemon are fainted. It is recommended that you heal your pokemon")
            else:
                train_pokemon(user)
        elif answer == 3:
            healPokemon(user)
        else:
            print("***** Thank you for playing. ***** ")
            break


def train_pokemon(user):
    """
    Prompts a user to select a pokemon on their team that they want to train

    Keyword argument:
    user -- This is the trainer object used to obtain a trainers pokemon party
    """
    display_pokemon(user.pokemon_party)
    pokemon_to_train = user_selection(len(user.pokemon_party),f"Which Pokemon do you want to train?(1-{len(user.pokemon_party)}):")

    user.level_pokemon(pokemon_to_train-1,1)
    print(user.pokemon_party[pokemon_to_train-1])


def editTeam(user):
    pass
#-------------------------------------------------

def main():

    print("Hello user welcome to beta 1 of my pokemon system \nWhat would you like to do?")
    #Will loop until the user selects the number 1 or 2
    choice_text = "1) Create a user \n2) Load a user \nAnswer Here: "
    answer = user_selection(2,choice_text)
    print('Ok you chose '+str(answer))
    if answer == 1:
        create_user()
    elif answer == 2:
        load_user()
    else:
        print( "Function does not exist")
    
    

if __name__== "__main__":
    main()