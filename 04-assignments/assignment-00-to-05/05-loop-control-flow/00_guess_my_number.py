import random

def main():
        
    while True:
        guess = int(input("Enter Num between 1 to 9...: " ))
        secret_Num = random.randint(1, 9)
        if guess < secret_Num: 
            print("low real num is: ", secret_Num)
        elif guess == secret_Num:
            print("Right Answer Congrats") 
        else:
            print("to high real num is: ", secret_Num)


# def main():
#     secret_number = random.randint(1, 99)
    
#     print("I am thinking of a number between 1 and 99...")

#     guess = int(input("Enter a guess: "))
#     while guess != secret_number:
#         if guess < secret_number: 
#             print("Your guess is too low")
#         else:
#             print("Your guess is too high")
            
#         print()
#         guess = int(input("Enter a new guess: "))  
        
#     print("Congrats! The number was: " + str(secret_number))
    
if __name__ == '__main__':
    main()