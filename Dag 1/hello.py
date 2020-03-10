#Lesson 1&2: Printing
print ("Lesson 2: Printing")
print ("Hello World!")
print ("Hello" + "World!")
print (11)
print ("11")
print (11.0)
print ("11.0")
print (2+2)
print (5226+3778)
print ("2+2")
print ("2" + "2") #hej
print (22)
print ("Hey")
print ("Lause" + "McLovin")
3+3

#Lesson 3: String Variables
print ("name")
name = "Nick Jonas"
print (name)
print (len(name))
print ("Name: " + name)
print ("Name: %s" %name)
print ("Name: {}".format(name))

print ("String Methods")
print ("hello".upper())
print ("HELLO".lower())
title = "game of thrones"
print (title.capitalize())
print (title.title())
print ("Slices")
print ("stranger things"[9:15])
print (title[:4])
print (title[5:7])
print (title[8:])
print ("hello".upper())

#Lesson 4: Integers And Floats (Variables)
i = 20
x = 6.0
print (i)
print (x)
print (i + x)
print ("i + x")
print (i - x)
print (i * x)
print (i / x)
print (20%14)
print ("X is {}" .format (x))

#Lesson 5: Conditionals
print ("Does 3 equal 3?")
if 3 == 3:
   print (True)

x = 3
y = 2
print ("is {} greater than {}?".format(x, y))
if x > y:
    print (True)
else:
    print (False)

x = 2
y = 3
if x > y:
    print (True)
else:
    print (False)

player_a = "paper"
player_b = "rock"

if player_a == "rock" or player_b == "rock":   
    print ("Someone chose rock!")

if player_a == "rock" and player_b == "scissors":
    print ("player A wins!")

elif player_a == "rock" and player_b == "paper":
    print ("Player B wins!")
else:
    print("Tie!")

#Lesson 6: Loop
for x in range(0, 10):
    print (x)
for x in range (0, 11, 2):
    print (x)
for x in range (10, -1, -1):
    print (x)

title = "When You Look Me In The Eyes"
 
for index in range(0, len(title)):
    print (title[index])


title = "When You Look Me In The Eyes"
 
for index in range(len(title)-1, -1, -1):
    print (title[index])

title = "When You Look Me In The Eyes"
for letter in title:
    print (letter)


#Lesson 7: Lists
names = ["Joe", "Nick"]
print (names)
print (len(names))
names.append("Kevin")
print (names)
print (names [1])
for index in range(0, len(names)):
    print (names[index])

#Lesson 8: Dictionaries
capitals = {"Latvia":"Riga", "Japan":"Tokyo"}
print (capitals)
print (len(capitals))
capital = capitals["Latvia"]
print (capital)
capitals["China"] = "Beijing"
print (capitals)

for country in capitals:
    capital = capitals[country]
    print ("The capital of {} is {}.".format(country, capital))

#Lesson 9: Functions
def print_pi():
    print ("3.14")
def print_double (x):
    print (x * 2)
print_double(2)

def get_pi():
    return 3.14
x = get_pi()
print (x)

def get_double(x):
   return x * 2

def get_greatest(x, y):
   if x > y:
    return x
   else:
     return y
def is_even(x):
    if x % 2 == 0:
        return True
    else:
            return False
if is_even(42) == True:
    print ("Even!")
else:
    print ("Odd!")

#Lesson 10: User Input
name = input("What is your name? > ")
print ("Hello! {}.".format (name))

x = input ("Please enter a number. > ")
print (x)
print (x + x)

x = int(x)
print (x)
print (x + x)

if a_smile or b_smile == False:
    return False

print ("Hej!")
print("ELSKER STRANGER THINGS!")