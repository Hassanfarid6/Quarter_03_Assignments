
def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """

    print(lst[0])
    
    """ Prints the all element of a provided list."""
    # for element in lst:
    #     print(element)


def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    # for get all elemen in array
    # print(lst)

    return lst

def main():
    lst = get_lst()
    get_first_element(lst)


if __name__ == '__main__':
    main()