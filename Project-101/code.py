import random

response = input("Press y to roll the dice and n to exit: ")

def randomRoll(response):
    
    while response == "y":
        
        no = random.randint(1, 6)
    
        if(no == 1):
            print("[   0   ]")
            response = []
            response = input("Press y to roll the dice and n to exit: ")
        elif(no == 2):
            print("[ 0   0 ]")
            response = []
            response = input("Press y to roll the dice and n to exit: ")
        elif(no == 3):
            print("[ 0 0 0 ]")            
            response = []
            response = input("Press y to roll the dice and n to exit: ")
        elif(no == 4):
            print("[ 0   0 ]")
            print("[ 0   0 ]")
            response = []
            response = input("Press y to roll the dice and n to exit: ")
        elif(no == 5):
            print("[ 0   0 ]") 
            print("[   0   ]")
            print("[ 0   0 ]")       
            response = []
            response = input("Press y to roll the dice and n to exit: ")
        elif(no == 6):
            print("[ 0   0 ]")
            print("[ 0   0 ]")    
            print("[ 0   0 ]")
            response = []
            response = input("Press y to roll the dice and n to exit: ")
            
            
randomRoll(response)            
            