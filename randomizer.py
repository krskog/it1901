import random

manual = True

li = input("Comma separated list of names (leave empty to read from names.txt)\n> ")

if (len(li)==0):
    manual = False
    try:
        with open('names.txt', 'r') as f:
            li = f.readlines()
    except FileNotFoundError:
        print("Could not find names.txt -- create it and try again, or input list manually")
        exit()


inp = input("How many random picks do you want? ")
num_rand = 1
if inp != "":
    try:
        num_rand = int(inp)
    except ValueError:
        print("Something went wrong during casting; using default value '%s'" % num_rand)
        
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
