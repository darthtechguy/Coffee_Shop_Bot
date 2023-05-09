# -*- coding: utf-8 -*-
"""
Spyder Editor

Created by Curtis Barry
Based on example from Network Chuck Coffee shop bot python tutorial.
"""
print("Hello, welocme to the coffee shop!") #Initial greeting
customer_name = input("Can I have your name to get started on your order?\n") #defining the customer name variable

print("\nThank you",customer_name,"for coming in today!\n") #Greeting customer with variable string

menu ="\nBlack Coffee, \nEspresso, \nLatte, \nand Cappucino." # Menu items to be listed

print(customer_name, "what would you like from our menu?\nHere are our avaliable options.\n" + menu) # Printing menu items to customer

order = input().lower() # Variable  set to to turn any case into lower case to be compaired with the if statement strings

def money (customer_name, payment): # Function asking customer for payment type as card or cash only
    if payment == 'cash':
        print('\nThank you, here is your reciept. Have a wonderful day '+ customer_name + '.')
        input('Press any key to quit')
    elif payment == 'card':
        print('\nOkay,'+ customer_name + ' you can swipe when the keypad lights up.\n')
        input('Press any key to quit')
    else:
        print("\nI'm sorry, we can not accept that form of payment.")
        input('Press any key to quit')

def encounter (customer_name, order): # Function asking customer how many items and giving them a total, and asks what payment type as an argument for the money function.
    while True:
        if order == 'black coffee':
            quant = int(input("\nHow many would you like?\n"))
            cost = 3.00 * quant
            print("\nSounds great " + customer_name + " we will have your",quant," " +order+"'s ready for you shortly.\nThat will be $",float(cost))
            payment = input("\n" + customer_name + " will you be paying with cash or card today?\n").lower()
            money (customer_name, payment)
            break
        elif order == 'espresso':
            quant = int(input("\nHow many would you like?\n"))
            cost = 3.50 * quant
            print("\nSounds great " + customer_name + " we will have your" , quant ," " +order +"'s ready for you shortly.\nThat will be $",float(cost))
            payment = input("\n" + customer_name + " will you be paying with cash or card today?\n").lower()
            money (customer_name, payment)
            break
        elif order == 'latte':
            quant = int(input("\nHow many would you like?\n"))
            cost = 3.25 * quant
            print("\nSounds great " + customer_name + " we will have your" ,quant," " +order +"'s ready for you shortly.\nThat will be $", float(cost))
            payment = input("\n" + customer_name + " will you be paying with cash or card today?\n").lower()
            money (customer_name, payment)
            break
        elif order == 'cappucino':
            quant = int(input("\nHow many would you like?\n"))
            cost = 4.00 * quant
            print("\nSounds great " + customer_name + " we will have your" , quant ," " +order +"'s ready for you shortly.\nThat will be $",float(cost))
            payment = input("\n" + customer_name + " will you be paying with cash or card today?\n").lower()
            money (customer_name, payment)
            break
        else:
            print("\nI'm sorry, we dont carry that.")
            break


encounter(customer_name, order) # Calling encounter function to start the order process


again = input('\n'+customer_name + ' can I get you something else from the menu?\n') # Variable to repeate process by calling encounter function, or ending the program

def repeate (again): # Function defining the re initiation of the repetition process
    if again == 'yes':
        print(customer_name, "what would you like from our menu?\nHere are our avaliable options.\n" + menu)
        order = input().lower()
        encounter(customer_name, order)
    if again == 'no':
        print ('\nIf you change your mind, we will be happy to see you again!')
        input('Press any key to quit')
    else:
        input('Press any key to quit')
        
repeate(again) # Function being called to restart process
