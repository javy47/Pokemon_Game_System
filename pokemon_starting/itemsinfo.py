import pathlib
#This document will store all the information necesary for all items in pokemon


#Healing Items
healing_items = []

#if i run from terminal use ..\healingitems.txt
with open(pathlib.Path.cwd().joinpath('healingitems.txt')) as h_items:

    for item in  h_items:
        name, description, value = item.split(',')
        healing_items.append({'name': name, 'description': description, 'value': value})
    







#Evolutionary Items