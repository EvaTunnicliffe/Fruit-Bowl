def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string


def print_fruit(l):
    for x in l:
        output = "{} : {}".format(x[0], x[1])
        print(output)


def print_with_indexes(l):
    for i in range(0, len(l)):
        output = "{} : {} : {}".format(i, l[i][0], l[i][1])
        print(output)


def add_fruit(l):
    print_with_indexes(l)
    choice = get_integer("Choose your fruit that you would like to add to: ")
    quantity = get_integer("How many would you like to add: ")
    l[choice][1] += quantity
    output = "{} {} have been added to the list".format(quantity, l[choice][0])
    print(output)


def remove_fruit(l):
    print_with_indexes(l)
    choice = get_integer("Choose your fruit that you would like to remove from: ")
    quantity = get_integer("How many would you like to remove: ")
    l[choice][1] -= quantity
    output = "{} {} have been removed from the list".format(quantity, l[choice][0])
    print(output)


def main():
    fruit_list = [["Apples", 10],
                  ["Grapes", 500],
                  ["Lemons", 2]]
    run = True
    while run is True:

        # Things to print out
        # menu
        menu = '''
        P: Print out list of fruit
        A: Adding to fruit
        R: Removing existing fruit
        Q: Quit'''
        print(menu)
        choice = input("What would you like to do? ")
        if choice == "P":
            print_fruit(fruit_list)
        elif choice == "A":
            add_fruit(fruit_list)
        elif choice == "R":
            remove_fruit(fruit_list)
        elif choice == "Q":
            run = False


main()
