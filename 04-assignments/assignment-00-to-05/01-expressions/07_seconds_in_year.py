YEAR = 365
HOURS = 24
MINUTES = 60
SECONDS = 60

def seconds_in_year(year):
    return (year * YEAR * HOURS * MINUTES * SECONDS)

def main():
    user_input = int(input("Enter a year: "))
    seconds = seconds_in_year(user_input)
    print("There are", seconds, "seconds in", user_input, "years")



if __name__ == '__main__':
    main()