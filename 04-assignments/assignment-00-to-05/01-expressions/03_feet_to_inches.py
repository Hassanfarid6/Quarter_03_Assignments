def feet_to_inches(feet):
    return feet * 12

def main():
    user_input = float(input("Enter the number of feet: "))
    inches = feet_to_inches(user_input)
    print("There are", inches, "inches in", user_input, "feet")
    




if __name__ == '__main__':
    main()