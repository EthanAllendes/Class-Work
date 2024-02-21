def decimal_menu():
    print("Calculator")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. Binary to Hexadecimal")
    print("4. Decimal to Hexadecimal")
    print("5. Hexadecimal to Decimal")
    print("6. Hexadecimal to Binary")
    print("7. Octal to Decimal")
    print("8. Decimal to Octal")

    choice = int(input("What can I help you solve today"))

    if choice == 1:
        num1 = float(input("Enter binary number "))
        num2 = float(input(" "))
        result = decimal_functions[choice - 1](num1, num2)
        result = 0
        if len (number) > 0:
            power = len(str(number)) - 1 #determine greatest power
            for num in str(number) :
                result += int(num) * 2 ** power
                power -= 1     # decrease by 1
            return result

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
def main1() :
    num = input ("Enter Binary Number:")
    print("Binary to Decimal: {}").format("Hey Binary of 1011 is equal to 11: {}".format(binary_to_decimal(num)))

def main2():
    num = input("Enter Decimal Number:")
    print("Decimal {} to Binary: {}".format(num, decimal_to_binary(num)))


if __name__ == "__main__":
    main1()
    main2()
    main3()
    main4()
    main5()
    main6()
    main7()
    main8()
