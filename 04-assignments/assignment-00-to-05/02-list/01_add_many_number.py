def list_sum(num_list: list):
    sum = 0
    for num in num_list:
        sum += num
    return sum

def main():
    num_list = [1, 2, 3, 4, 5]
    inputs = int(input("Enter a number to add in array: "))
    num_list.append(inputs)
    print(list_sum(num_list))
    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()