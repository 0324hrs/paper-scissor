######randomization#########
#######mpython random module#######
import random
# 
random_int = random.randint(50, 100)
# 
print(random_int)

# generate random floating number
import random
# 
random_float = random.random()
# 
print(random_float)

######tossy coin game############
import random
# 
random_output = random.randint(0, 1)
if random_output == 1:
    print("Head")
else:
    print("Tail")

########################
###python list######

counties_in_kenya = ["mombasa", "voi", "kitui", "machakos", ]
# list manipulation
# mombasa to pwani
counties_in_kenya[0] = "pwani"
# adding another county using the append function
counties_in_kenya.append("Nyeri")
# adding more counties to our list
counties_in_kenya.extend(["kakamega", "kiambu", "kanairo", "kirinyaga"])
# removing our item from the list
counties_in_kenya.remove("kanairo")
# clearing everything from the list
# counties_in_kenya.clear()
print(counties_in_kenya)


#########exercise#########
import random

squad_names = input("Give the names of your squad members\n")
squad = squad_names.split(",")
# number of items in our list
squad_names_names = len(squad)
select_random = random.randint(0, squad_names_names-1)
bills_payer = squad[select_random]
# the comment below can do the same work as the five lines above
# bills_payer = random.choice(squad_names)
print(bills_payer + "is going to pay our bills today folks")

#####################################

