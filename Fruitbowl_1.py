
def print_fruit(l):
    for x in l:
        output = "{} : {}".format(x[0], x[1])
        print(output)


def main():
    run = True
    while run == True:
        fruit_list = (["Apples", 10],
                      ["Grapes", 500],
                      ["Lemons", 2])
        # Things to print out
        # menu
        menu = '''
        P: Print out list of fruit
        Q: Quit'''
        print(menu)
        choice = input("What would you like to do?")
        if choice == "P":
            print_fruit(fruit_list)
        elif choice == "Q":
            run = False


main()
