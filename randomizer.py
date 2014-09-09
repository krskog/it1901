import random
from colorama import init, Fore
init(autoreset=True)

manual = True

li = input("Comma separated list of names (leave empty to read from names.txt)\n> ")

inp = input("How many random picks do you want? ")

num_rand = 1
if inp != "":
    try:
        num_rand = int(inp)
    except ValueError:
        print("Something went wrong during casting; using default value '%s'" % num_rand)

if (len(li)==0):
    manual = False
    with open('names.txt', 'r') as f:
        li = f.readlines()
        
# Cleaning
for x in range(0, len(li)):
    if manual:
        name = li[x].strip()
    else:
        name = li[x].strip('\n')
    li[x] = name

def choose_random(li):
    rand = random.choice(li)
    li.remove(rand)
    return li, rand

counter = 0
while (counter < num_rand):
    counter += 1
    li, rand = choose_random(li)
    print("%3.0f: %s" % (counter, rand))   
