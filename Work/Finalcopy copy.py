def main():  # this is the main funcion that I use to run my program
    print ("Welcome to the main menu of one complement calculator ") # I used the print stament to make the menu because is essay for me .
    print ("Select one of the fallowing options:")
    print ("(A). Decimal to Binary")
    print ("(B). Binary to Decimal")


    answer = input("Please Enter your selection:").upper() # I create this user input so the user can chose wich option he want to used

    if answer == "A": # if answer is A the program is going to call  decimal_to_binary  funtion
      decimal_number = int(input("Please enter your DECIMAL number: ")) # here is were the user his input, the number they want to translate
      binar_number = decimal_to_binary(decimal_number) # this is went the program call the fuction
      print(f"The binary representation of {decimal_number} is {binar_number}") # here is the answare the my funtion send back(the answere for the user input )
      print("Will you like to return to the main menu?") #  this line is like giving the user a option to quit or return to menu
      usrChoice = int(input("Insert a -1 if you want to quit a 1 if you want to return to menu ")) # user input to quit or continue
      if(usrChoice == 1):
         return main() # 1 will send the user back to funtion main (main menu)
      elif(userChoicee ==-1):
         print("Thank you for using the converter") # if user input is -1 will quit the program
      else:
         print("Wrong input going back to menu")
         return main() # any other input will give you a error message and will send you back to the main fuction


    if answer == "B":  # if the user input for answer is B he chose binary to decimal
      binary = input("Please enter a BINARY number: ") # here the user need to put the number the he want to translate
      decimal = binary_to_decimal(binary) # here im calling the  binary_to_decimal(binary) funtion to translate the user input
      print(f"The decimal representation of {binary} is {decimal}") # this is the answare send from  binary_to_decimal(binary)

      userChoicee = int(input("Insert a -1 if you want to quit a 1 if you want to return to menu "))
      if(userChoicee == 1): # if user put 1 will send you back to main
         return main()
      elif(userChoicee ==-1):
         print("Thank you for using the converter") # if user input is 1 will quit the program
      else:
         print("Wrong input going back to menu")
         return main() # any other input will send you to main


def binary_to_decimal(binary):
  decimal = 0 # initializes the variable before its used
  for digit in binary: # Loops it the length of binary
    decimal = decimal * 2 + int(digit)
  return decimal

def decimal_to_binary(n):
  binar = ""
  while n > 0:
    remainder = n % 2
    binar = str(remainder) + binar
    n //= 2
  return binar

if __name__ == '__main__':
    main()
