import sqlite3
from Trainer import Trainer
from pokemon import Pokemon


conn = sqlite3.connect('pokemon.db')
db = conn.cursor()

def createUser():
    print("create user function")

    username= input('Please Enter a Trainer Name ')

  #Working right here  
    #Check to make sure that username is not in database
    db.execute('SELECT username FROM trainer WHERE username= :user',{'user': username})
    test_name=db.fetchone()

    #testValues(text)
    if test_name is None:
        db.execute('INSERT INTO trainer (username) VALUES (:user)',{'user': username})
        conn.commit()
        greeting()

    else:
        print('---- SORRY USERNAME TAKEN ----')
        createUser()

    



def  loadUser():
    print("load user")

    username= input('Enter the username of your account: ')
    db.execute('SELECT * FROM trainer WHERE username= :username',{'username': username})
    name = db.fetchone()
    print(name)
    db.execute('SELECT * FROM pokemon_party WHERE trainer_id= :trainer_id',{'trainer_id': name[0]})
    #trainer_id, pokemon_id
    pokemon_trainer_list= db.fetchall()
    #print(pokemon_trainer_list)

    pokemon_party = []
    #Goes through the reslt of the database query and adds each pokemon to that trainers party
    #This will loop for each pokemon the trainer has(Also looping over a tuple)

#If pokemon party_tranier list is empty prompt them to create their own team
#also means you would have to skip the for loop below
    for pokemon in pokemon_trainer_list:

        db.execute('SELECT * FROM pokemon WHERE pokedex_id= :pokemon_id',{'pokemon_id':pokemon[2] })
        monster = db.fetchone()
        #print('printing pokemon')
        #print(monster)
        #Pokemon Name
        monster_name = monster[1]
        #print("Pokemon: "+ monster_name)
        #Pokemon Level
        monster_level = monster[2]
        #print("pokemon level: "+ str(monster_level))
        #First pokemon type
        monster_type1 = db.execute('SELECT type FROM pokemon_type WHERE id= :id', {'id': monster[3]}).fetchone()
        #print(monster_type1[0])
        #second pokemon type
        monster_type2 = db.execute('SELECT type FROM pokemon_type WHERE id= :id', {'id': monster[4]}).fetchone()
        #print(monster_type2[0])
        #pokemon base hp
        monster_hp = monster[5]
        #print(monster_hp)
        #pokemon base attack
        monster_atk = monster[6]
        #print(monster_atk)
        #pokemon base defense
        monster_def = monster[7]
        #print(monster_def)
        #pokemon base special attack
        monster_spatk = monster[8]
        #print(monster_spatk)
        #pokemon base special defense
        monster_spdef = monster[9]
        #print(monster_spdef)
        #pokemon base speed
        monster_spe = monster[10]
       # print(monster_spe)
    
        pokemon_party.append(Pokemon(monster_name, monster_level, monster_type1[0], monster_type2[0], monster_hp, monster_atk, monster_def, monster_spatk, monster_spdef, monster_spe))
    # print(pokemon_party[0],pokemon_party[1])



    user = Trainer(name[1], name[0], pokemon_party)
    print(user)
    greeting(user)
    



def greeting(user=None):
    if user is None:
        print("Hello user welcome to beta 1 of my pokemon system \nWhat would you like to do?")

        #Will loop until the user selects the number 1 or 2
        answer = 0
        while not answer:
            try:      
                answer = int(input("1) Create a user \n2) Load a user \nAnswer Here: "))
                if answer not in (1,2):
                    raise ValueError
                break
            except ValueError:
                print('Please Select a Valid Number')

        print('Ok you chose '+str(answer))
        if answer == 1:
            createUser()
        elif answer == 2:
            loadUser()
        else:
            print( "Function does not exist")
    else:
        print('Now that you have your account what would you like to do?')
        print('1) Edit Team')
        print('2) Battle')
        print('3) Train Pokemon')
        print('4) Heal')
        choice= int(input)
        # user.heal_pokemon(user.pokemon_party[0])
        


         



def main():
    greeting()



if __name__== "__main__":
    main()