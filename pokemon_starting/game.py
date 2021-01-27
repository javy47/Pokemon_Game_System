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

    



def loadUser():
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
        # print(monster_type1)
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

        pkmn = Pokemon(monster_name, monster_level, monster_type1[0], monster_type2[0], monster_hp, monster_atk, monster_def, monster_spatk, monster_spdef, monster_spe)
        #assign all weakness to pokemon after their creation
        pkmn.pokemon_weakness(monster_type1[0],monster_type2[0])
        pokemon_party.append(pkmn)
    # print(pokemon_party[0],pokemon_party[1])



    user = Trainer(name[1], name[0], pokemon_party)
    print(user)
    greeting(user)

def print_pokemon(user):
     pokemon_traner_list = db.execute('SELECT * FROM pokemon_party WHERE trainer_id= :trainer_id',{'trainer_id': user.name}).fetchall()

     count=1
     for pokemon in user.pokemon_party:
         print("{choice}) Pokemon: {name} HP: {current_hp}/{max_hp}".format(choice=count,name=pokemon.name, current_hp= pokemon.current_hp, max_hp=pokemon.maximum_hp))
         count+=1



def greeting(user=None):

        print('Now that you have your account what would you like to do?')
        print('1) Edit Team: [You can ADD or REMOVE pokemon from your team]')
        print('2) Battle: [Try your skills with some combat between rivals]')
        print('3) Train Pokemon: [Increase the combat prowess of your Pokemon]')
        print('4) Heal: [Heal Your pokemon back into tip top shape]')
        text= 'What would you like to do?(1-4)'
        answer = choice(4, text)

        if answer == 1:
            editTeam()
        elif answer == 2:
            battle()
        elif answer == 3:
            trainPokemon()
        else:
            # user.heal_pokemon(user.pokemon_party[0])
            healPokemon(user)
#------------------------------------------------
#WIll work on these on a future date
def trainPokemon():
    pass

def battle():
    pass

def editTeam():
    pass
#-------------------------------------------------
      
def healPokemon(user):
    if len(user.pokemon_party) < 1:
        pass
    else:
        print_pokemon(user)
        choice = int(input('Which Pokemon would you like to heal?'))
        choice(len(user.pokemon_party))
        user.heal_pokemon(user.pokemon_party[choice-1])


def choice(num, text):

    lst = list(range(1,num+1))
    answer= 0
    while answer not in lst:
        try:
            answer = int(input(text))
            if answer not in (1,num):
                raise ValueError
            break
        except ValueError:
            print('Select a valid Number')

    return answer



def main():

    print("Hello user welcome to beta 1 of my pokemon system \nWhat would you like to do?")
    #Will loop until the user selects the number 1 or 2
    choice_text = "1) Create a user \n2) Load a user \nAnswer Here: "
    answer = choice(2,choice_text)
    print('Ok you chose '+str(answer))
    if answer == 1:
        createUser()
    elif answer == 2:
        loadUser()
    else:
        print( "Function does not exist")
    
    



if __name__== "__main__":
    main()