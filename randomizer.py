import random

manual = True
namefile = 'names.txt'
li = []

str_input = input("Comma separated list of names (leave empty to read from names.txt)\n> ")

# If str_input is a file name, read from that file.
if "." in str_input:
    namefile = str_input.split(' ')[0]
    manual = False

# If no input OR filename input, read from file
if (len(str_input)==0 or not manual):
    manual = False
    try:
        with open(namefile, 'r') as f:
            li = f.readlines()
    except FileNotFoundError:
        print("Could not find names.txt -- create it and try again, or input list manually")
        exit()

# How many random selections do you want?
inp = input("How many random picks do you want? [1] ")
num_rand = 1
if inp != "":
    try:
        num_rand = int(inp)
    except ValueError:
        print("Something went wrong during casting; using default value '%s'" % num_rand)
        
# Create list if input was CSV
if manual:
    li = str_input.split(",")

# Cleaning lines
for x in range(0, len(li)):
    if manual:
        name = li[x].strip(" ")
    else:
        name = li[x].strip('\n')
    li[x] = name

# Choose random element from list
def choose_random(li):
    rand = random.choice(li)
    li.remove(rand)
    return li, rand

# Select number of random choices
counter = 0
while (counter < num_rand):
    counter += 1
    li, rand = choose_random(li)
    print("%3.0f: %s" % (counter, rand))   
