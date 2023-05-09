import random


number =random.randint(1,100)

count = 0
while True:
    count +=1
    guess = int(input("enter your guess"))
    if guess > number:
        print("the gussed number is bigger")
    elif guess < number:
        print("the guessed number is smaller")
    else :
        print(f"you win! the number of your guessed:{count}")
        break