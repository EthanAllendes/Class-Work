def get_menu():
    menu_dict = {
         '1':'Binary to Decimal',
         '2':'Decimal to Binary',
         '3':'Binary to hexadecimal',
         '4':'Decimal to hexadecimal',
         '5':'Hexadecimal to decimal',
         '6':'Hexadecimal to Binary',
         '7':'Octal to decimal',
         '8':'Decimal to Octal',
         'X':'done_selecting'

    }
    return menu_dict


def display_menu(menu_dict):
    for items, values in menu_dict.items():
        print(items+"."+ values.replace('_',' ').capitalize())
    menu_selection = input("Which one can I help you solve? ").upper()

    print("You picked {} ".format(menu_dict[menu_selection]))



choice = int(input("What can I help you solve today"))

    if choice == 1:
        num1 = float(input("Enter first decimal number: "))
        num2 = float(input("Enter second decimal number: "))
        result = decimal_functions[choice - 1](num1, num2)
        print("The result is:", result)

    elif choice == 2:
        num1 = float(input("Enter first decimal number: "))
        def decimal_to_binary(number):
            result = ""
            number = int(number)
            while number > 0:
                remainder = number % 2
                number = number // 2
                result = str(remainder) + result
            return result

    elif choice == 3:
        num1 = float(input("Enter first decimal number: "))
        num2 = float(input("Enter second decimal number: "))
        result = decimal_functions[choice - 1](num1, num2)
        print("The result is:", result)

    elif choice == 4:
        num1 = float(input("Enter first decimal number: "))
        num2 = float(input("Enter second decimal number: "))
        result = decimal_functions[choice - 1](num1, num2)
        print("The result is:", result)

    elif choice == 5:
        print("Exiting...")
    else:
        print("Invalid choice, please enter 1, 2, 3, 4, or 5.")
        decimal_menu()

    if choice == 6:
        print("Executing")


def check_selection(numbers):
    hex_list = ["A", "B", "C", "D", "E", "F", "0", "1",
                "2", "3", "4", "5", "6","7", "8", "9"]
    for number in numbers:
        if number.upper() not in hex_list:
           print("Not a Decimal number")
           return(False)
    return(True)



def main1():
    menu_selection = ''
    items_list = []
    while menu_selection != 'X':
        menu_dict = get_menu()
        menu_selection = display_menu(menu_dict)
        items_list.append(menu_dict[menu_selection])
        input("Hit Enter to continue!!")

    display_purchases(items_list)
def main2():
    num = input("Enter Decimal Number:")
    print("Decimal {} to Binary: {}".format(num, decimal_to_binary(num)))

if __name__ == '__main__':
        main1()
        main2()
