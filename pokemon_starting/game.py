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

    

#Takes the trainer id
def load_trainers(id):
    db.execute('SELECT * FROM trainer WHERE id= :id',{'id': id})
    account = db.fetchone()

    # db.execute('SELECT * FROM pokemon_party WHERE trainer_id= :trainer_id',{'trainer_id': account[0]})
    # pokemon_trainer_list = db.fetchall()

    #******************continue here tomorrow***************************2
    pokemon_party = trainer_party(account[0])

    user = Trainer(account[1],account[0],pokemon_party)
    return user

#creates the trainers party
def trainer_party(trainer_id):
    db.execute('SELECT * FROM pokemon_party WHERE trainer_id= :trainer_id',{'trainer_id': trainer_id})
    pokemon_trainer_list = db.fetchall() 

    pokemon_party = []
    #If pokemon party_tranier list is empty prompt them to create their own team
    #also means you would have to skip the for loop below
    for pokemon in pokemon_trainer_list:

        db.execute('SELECT * FROM pokemon WHERE pokedex_id= :pokemon_id',{'pokemon_id':pokemon[2] })
        monster = db.fetchone()
        #Pokemon Name
        monster_name = monster[1]
        #Pokemon Level
        monster_level = monster[2]
        #First pokemon type
        monster_type1 = db.execute('SELECT type FROM pokemon_type WHERE id= :id', {'id': monster[3]}).fetchone()
        #second pokemon type
        monster_type2 = db.execute('SELECT type FROM pokemon_type WHERE id= :id', {'id': monster[4]}).fetchone()
        #pokemon base hp
        monster_hp = monster[5]
        #pokemon base attack
        monster_atk = monster[6]
        #pokemon base defense
        monster_def = monster[7]
        #pokemon base special attack
        monster_spatk = monster[8] 
        #pokemon base special defense
        monster_spdef = monster[9]
        #pokemon base speed
        monster_spe = monster[10]

        pkmn = Pokemon(monster_name, monster_level, monster_type1[0], monster_type2[0], monster_hp, monster_atk, monster_def, monster_spatk, monster_spdef, monster_spe)
        #assign all weakness and resistance to pokemon after their creation
        pkmn.pokemon_weak_resist(monster_type1[0],monster_type2[0])
      
        pokemon_party.append(pkmn)
    
    return pokemon_party


def loadUser():
    print("load user")

    username= input('Enter the username of your account: ')
    db.execute('SELECT * FROM trainer WHERE username= :username',{'username': username})
    name = db.fetchone()
    print(name)
  
    pokemon_party = trainer_party(name[0])

    user = Trainer(name[1], name[0], pokemon_party)
    print(user)
    greeting(user)


def print_pokemon(user):
     pokemon_traner_list = db.execute('SELECT * FROM pokemon_party WHERE trainer_id= :trainer_id',{'trainer_id': user.name}).fetchall()

    #  count=1
    #  for pokemon in user.pokemon_party:
    #      print("{choice}) Pokemon: {name} HP: {current_hp}/{max_hp}".format(choice=count,name=pokemon.name, current_hp= pokemon.current_hp, max_hp=pokemon.maximum_hp))
    #      count+=1

     for count, pokemon in enumerate(user.pokemon_party, start=1):
         print("{choice}) Pokemon: {name} HP: {current_hp}/{max_hp}".format(choice=count,name=pokemon.name, current_hp= pokemon.current_hp, max_hp=pokemon.maximum_hp))
         



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
            battle(user)
        elif answer == 3:
            trainPokemon()
        else:
            # user.heal_pokemon(user.pokemon_party[0])
            healPokemon(user)
#------------------------------------------------
#WIll work on these on a future date
def trainPokemon():
    pass

def battle(player1):
    db.execute('SELECT * FROM trainer')
    trainer_lst = db.fetchall()
    input_id = int(input('Which trainer would you like to battle?(1-{num})'.format(num=len(trainer_lst))))

    player2 = load_trainers(input_id)
    # Loaded the Second battler --Now to commence the battle

    p1_poke_counter = len(player1.pokemon_party)
    p2_poke_counter = len(player2.pokemon_party)

    p1_poke_fainted = 0
    p2_poke_fainted = 0

    p1_current_pokemon = player1.pokemon_party[0]
    p2_current_pokemon = player2.pokemon_party[0]

    battle_over_flag = False
    while not battle_over_flag:
        #checking to see if pokemon is fainted or not
        p1_current_pokemon.pokemon_alive
        p2_current_pokemon.pokemon_alive
        if p1_current_pokemon.fainted == True:
            print("{pokemon} hp has dropped to 0".format(pokemon=p1_current_pokemon.name))
            p1_current_pokemon = switch_pokemon(player1, id(p1.p1_current_pokemon))

        print("What would you like to do?")
        answer = choice(3,"1)Fight\n2)Heal\n3)Switch")
        if answer == 1:
            pass
        elif answer == 2:
            pass
        else:
            pass

        if p1_poke_fainted == p1_poke_counter:
            battle_over_flag = True
            print('Player 2 Has won the battle')
            break

        if p2_poke_fainted == p2_poke_counter:
            battle_over_flag = True
            print('Player 1 Has won the battle')
            break


def switch_pokemon(trainer, pokemon_id):
    switch_choices = [pokemon for pokemon in trainer.pokemon_party if id(pokemon) != pokemon_id if pokemon.fainted == False ]   
    for i in range(0,len(switch_choices)):
        print("%s) %s"%(i+1, switch_pokemon[i]))
    answer = choice(len(switch_choices,'Which pokemon do you want to sub into battle?(1-%s)'%(len(switch_choices))))
    
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