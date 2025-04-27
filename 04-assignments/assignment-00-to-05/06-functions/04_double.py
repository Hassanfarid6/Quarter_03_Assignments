

def double_num (num):
    return num*2

def main():
    userInput = int(input("Enter a Number: "))
    num = double_num(userInput)
    print("Double that is", num)





# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()