import random

n=9
arr = [2,3,6,1,0,12,14,16,7]

random_index = random.randint(0,n-1)
answer = arr[random_index]

num_guesses = 0
while True:
    guess = int(input("enter your guess"))
    num_guesses +=1

    if guess == answer:
        print("you win!!")
        break
    else:
        print("you guess is wrong.please try again")
        print("the number of your guesses:",num_guesses)