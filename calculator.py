#BEGIN:

from colorama import Fore, Style
import time
import os

os.system("cls")

calculator_running = True

while calculator_running == True:

    print(" ")
    print(Fore.YELLOW + " CALCULATOR for MR.GROBLER")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" ")

    calculator_type = input(Fore.BLUE + " Enter Calculator Type: ")
    print(Style.RESET_ALL)

    #################################################################
    if calculator_type == "+":
        print(" ")
        number_one = input(Fore.CYAN + " Enter a Number: ")
        number_two = input(Fore.CYAN + " Enter another Number: ")
        (result) = float(number_one) + float(number_two)
        print(" ")
        print(Style.RESET_ALL)
        print(Fore.RED, number_one, Style.RESET_ALL + "+" + Fore.RED, number_two, Style.RESET_ALL + "=" + Fore.YELLOW, result)
        print(Style.RESET_ALL)
    #################################################################


        user_choice = input(" Proceed (y/n) ").lower()


        if user_choice == "y":
            calculator_running = True
            os.system("cls")

        elif user_choice == "n":
            calculator_running = False
            print(" ")
            time.sleep(2)
            print(" Saving Calculator....")
            time.sleep(1)
            user_choice = input(" PRESS ENTER TO EXIT")

        else:
            print(" ") 
            print(Fore.RED + " INVALID INPUT")
            time.sleep(1)
            print(Style.RESET_ALL)
            print(" ")
            print(" RESTARTING...")
            time.sleep(2)
            os.system("cls")
            print(Style.RESET_ALL)
          

    #################################################################
    elif calculator_type == "-":
        print(" ")
        number_one = input(Fore.GREEN + " Enter a Number: ")
        number_two = input(Fore.GREEN + " Enter another Number: ")
        result = float(number_one) - float(number_two)
        print(" ")
        print(Style.RESET_ALL)
        print(Fore.CYAN, number_one, Style.RESET_ALL + "-" + Fore.CYAN, number_two, Style.RESET_ALL + "=" + Fore.YELLOW, result)
        print(Style.RESET_ALL)
    #################################################################


        user_choice = input(" Proceed (y/n) ").lower()


        if user_choice == "y":
            calculator_running = True
            os.system("cls")

        elif user_choice == "n":
            calculator_running = False
            print(" ")
            time.sleep(2)
            print(" Saving Calculator....")
            time.sleep(1)
            user_choice = input(" PRESS ENTER TO EXIT")

        else:
            print(" ") 
            print(Fore.RED + " INVALID INPUT")
            time.sleep(1)
            print(Style.RESET_ALL)
            print(" ")
            print(" RESTARTING...")
            time.sleep(2)
            os.system("cls")
            print(Style.RESET_ALL)

    #################################################################
    elif calculator_type == "*":
        print(" ")
        number_one = input(Fore.RED + " Enter a Number: ")
        number_two = input(Fore.RED + " Enter another Number: ")
        result = float(number_one) * float(number_two)
        print(" ")
        print(Style.RESET_ALL)
        print(Fore.MAGENTA, number_one, Style.RESET_ALL + "x" + Fore.MAGENTA, number_two, Style.RESET_ALL + "=" + Fore.YELLOW, result)
        print(Style.RESET_ALL)
    #################################################################


        user_choice = input(" Proceed (y/n) ").lower()


        if user_choice == "y":
            calculator_running = True
            os.system("cls")

        elif user_choice == "n":
            calculator_running = False
            print(" ")
            time.sleep(2)
            print(" Saving Calculator....")
            time.sleep(1)
            user_choice = input(" PRESS ENTER TO EXIT")

        else:
            print(" ") 
            print(Fore.RED + " INVALID INPUT")
            time.sleep(1)
            print(Style.RESET_ALL)
            print(" ")
            print(" RESTARTING...")
            time.sleep(2)
            os.system("cls")
            print(Style.RESET_ALL)

    #################################################################
    elif calculator_type == "/":
        print(" ")
        number_one = input(Fore.MAGENTA + " Enter a Number: ")
        number_two = input(Fore.MAGENTA + " Enter another Number: ")
        result = float(number_one) / float(number_two)
        print(" ")
        print(Style.RESET_ALL)
        print(Fore.GREEN, number_one, Style.RESET_ALL + "/" + Fore.GREEN, number_two, Style.RESET_ALL + "=" + Fore.YELLOW, result)
        print(Style.RESET_ALL)
    #################################################################


        user_choice = input(" Proceed (y/n) ").lower()


        if user_choice == "y":
            calculator_running = True
            os.system("cls")

        elif user_choice == "n":
            calculator_running = False
            print(" ")
            time.sleep(2)
            print(" Saving Calculator....")
            time.sleep(1)
            user_choice = input(" PRESS ENTER TO EXIT")

        else:
            print(" ") 
            print(Fore.RED + " INVALID INPUT")
            time.sleep(1)
            print(Style.RESET_ALL)
            print(" ")
            print(" RESTARTING...")
            time.sleep(2)
            os.system("cls")
            print(Style.RESET_ALL)


    #################################################################
    else:
        os.system("cls")
        print(" ")
        print(Fore.RED + " INVALID INPUT!!")
        time.sleep(1)
        print(Style.RESET_ALL)
        print(" ")
        print(" RESTARTING...")
        time.sleep(2)
        os.system("cls")
        print(Style.RESET_ALL)
    #################################################################


#END