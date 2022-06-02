import random
  
choices = ["snake","water","gun"]

computer = random.choice(choices)
player = None
while player  not in choices:
      player = input("snake,water, or gun?:").lower()

      if player == computer:
        print("player: ",player)
        print("computer: ",computer)    
        print ("Tie!")

      elif player == "snake":
          if computer == "water":
            print("player: ",player)
            print("computer: ",computer)    
            print ("you loose !")

      elif player == "water":
        if computer =="snake":
           print("player: ",player)
           print("computer: ",computer)    
           print ("you Win")

      elif player == "snake":
          if computer =="gun":
           print("player: ",player)
           print("computer: ",computer)    
           print ("you loose!")

      elif player == "gun":
        if computer =="snake":
           print("player: ",player)
           print("computer: ",computer)    
           print ("you Win!")

      elif player == "gun":
        if computer =="water":
           print("player: ",player)
           print("computer: ",computer)    
           print ("you Win!")

      elif player == "water":
        if computer =="gun":
           print("player: ",player)
           print("computer: ",computer)    
           print ("you Loose!")
