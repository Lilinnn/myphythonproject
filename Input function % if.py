

#ifelse practice

#the input fuction requires a string value

door = input("number")

if door == "1":
    print('There is a nice vampire asking you if you enjoy life.')
    print('what do you do?')
    print('1. Smile and nod')
    print('2. Scream and run')

vampire = input("type a number")

if vampire == "1":
    print("Congratulations, you found a new friend!")
elif vampire == "2":
    print("Sorry, the vampire is faster. You become a dinner.")
else:
    print("You are not so good with numbers, are you?")

print(door)

name = "Julia"

print(f"Welcome to Pyladies {name} !")

vampire = input("A number")

if vampire == "1":
    print(f"Congratulations {name}, you found a new friend!")
elif vampire == "2":
    print(f"Sorry {name}, the vampire is faster, You become a dinner.")
else:
    print("You are not so good with numbers, are you?")

print(vampire)