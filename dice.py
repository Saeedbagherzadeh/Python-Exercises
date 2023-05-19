import random

counter = 0
while counter <2:
    number = random.randint(1,6)
    print("the number obtained by throwing the dice:",number)
     
    if number ==6:
        counter+=1