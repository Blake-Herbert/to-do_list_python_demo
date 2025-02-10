import os

def display_list():
    os.system('cls')
    print(f"Welcome to the to-do list app! \n\nHere's your to-do list:")
    for item in to_do_list:
        print(f" * {item}")
    print("------------------------------")

to_do_list = [ "Study", "Code"]

while True :
    display_list()
    menu_choice = input("1. Add to List \n2. Remove from List \n3. End\n")

    match menu_choice :
        case "1":
            display_list()
            to_do_list.append(input("What would you like to add to the to-do list?\n"))
        case "2":
            display_list()
            try:
                to_do_list.remove(input("What would you like to remove from the list?\n"))
            except:
                display_list()
                input("Could not find that on the list. \nReturning to main menu, press enter key to continue...\n")
        case "3":
            os.system('cls')
            input("Ending program...")
            break