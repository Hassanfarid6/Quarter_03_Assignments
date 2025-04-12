import random

NUM_SIDES: int =6
def roll_dice():
    dice1:int = random.randint(1,NUM_SIDES)
    dice2:int = random.randint(1,NUM_SIDES)
    total:int = dice1 + dice2
    print(f"You rolled a {dice1} and a {dice2} for a total of {total}")
    return total
    
def main():
    user_input:int = int(input("Guesst the number between 2 and 12: "))
    total = roll_dice()
    
    if total == user_input :
        print("You win!")
    else:
        print("You lose!")
    
    
    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()