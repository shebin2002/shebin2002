import random

again= True 
while again:
    print(random.randint(1,6))
    a_roll =input("Want to roll again ?(y/n):")
    if a_roll.lower () =="y":
        continue
    else:
        break 