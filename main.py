import csv
import re #regEX
import pandas as pd
from datetime import *
#Study pandas Concept
#Concept used so far
# iloc,  pd.read_csv
#install pandas
#pip install pandas

#--------------------------------------Display Menus-----------------------------------------------------

def Main_Menu():
    print("\n=====================\n")
    print("1.Display Category")
    print("2.Cart")
    print("3.Remove item")
    print("4.Place order")
    print("5.Exit")
    print("\n======================\n")
    menu_option()


def product_categ():
    print("\n=====================\n")
    print("1. Phones")
    print("2. Laptops")
    print("3. Speakers")
    print("4. Earphones")
    print("5. Return to Main menu")
    print("\n=====================\n")

#-----------------------------Customer Info--- Contact details, etc---------------------------------

def get_phone():
    print("-------------------WELCOME TO FERGO STORE--------------------\n")
    number = int(input('Please type in your phone number.\n>'))
    print()
    mod_val = number % 1000000000 
    
    if not(mod_val < 1000000000 and mod_val != number):
        print('Phone number is invalid.\n')
        number = get_phone()
    
    return number

def get_email():
    email = input('Please type in your email.\n>')
    print()
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not(re.fullmatch(email_regex, email)):
        print('Email is invalid.\n')
        email = get_email()

def get_pin_code():
    pin_code_regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
    pin_code = input('Please type your pincode.\n>')
    print()
    
    if not(re.fullmatch(pin_code_regex, pin_code)):
        print('Invalid pincode.\n')
        pin_code = get_pin_code()

    return pin_code

def get_address():
    addinput = input("Please enter your address.\n>")
    print()

#-----------------------------------------Main Program-------------------------------------------------

carts = []
amount =[]


def menu_option():
    option = int(input("Enter the required option no.\n>"))
    if option == 1:
        display_categ()
    elif option == 2:
        shop_cart()
    elif option == 3:
        remove_item()
    elif option == 4:
        place_order()
    elif option == 5:
        print("Thank you for visiting our store")
    else:
        print("ERROR")
        print("PLease enter a valid input")
        menu_option()


def display_categ():
    product_categ()
    i=0
    option = int(input("Enter the required option no.\n>")) 
    if option == 1:
            column_names = ["SID", "Name", "Price"]
            print("\n================================================================\n")
            text = pd.read_csv("Phones_CS_project.csv", names=column_names)
            print(text)
            print("\n================================================================\n")
            
            optn = input("Do want to add any product to cart ( Y/N ): ")

            if optn == 'Y' or optn == 'y':
                item_no = int(input("Enter the item no. you want to add to cart: "))
                a = open(('Phones_CS_project.csv'),'r')
                # x = csv.DictReader(a)
                # for row in x:
                #     new = dict(row)
                #     print(new)
                #     items = new

                a = pd.read_csv('Phones_CS_project.csv')      #used iloc command of pandas
                itnm = a.iloc[item_no,1]
                itpr = a.iloc[item_no,2]
                print(f'{itnm}  Rs. {itpr}')                        
                carts.append(itnm)
                itpr_conv = int(itpr)
                amount.append(itpr_conv)
                
                print("Thanks! Your product has been added to cart!!")
                Main_Menu()
                
            else:
                Main_Menu()

    elif option == 2:
            f = open('Laptop_CS_project.csv', 'r')
            column_names = ["SID", "Name", "Price"]
            print("\n================================================================\n")
            text = pd.read_csv("Laptop_CS_project.csv", names=column_names)
            print(text)
            print("\n================================================================\n")
            f.close

            optn = input("Do want to add any product to cart ( Y/N ): ")

            if optn == 'Y' or optn == 'y':
                item_no = int(input("Enter the item no. you want to add to cart: "))
                a = pd.read_csv('Laptop_CS_project.csv')      #used iloc command of pandas
                itnm = a.iloc[item_no,1]
                itpr = a.iloc[item_no,2]
                print(f'{itnm}  Rs. {itpr}')                         
                carts.append(itnm)
                itpr_conv = int(itpr)
                amount.append(itpr_conv)

                print("Thank your product has been added to cart!!")
                Main_Menu()

            else:
                Main_Menu()

    elif option == 3:
            f = open('Speakers_CS.csv', 'r')
            column_names = ["SID", "Name", "Price"]
            print("\n================================================================\n")
            text = pd.read_csv("Speakers_CS.csv", names=column_names)
            print(text)
            print("\n================================================================\n")
            f.close
            
            optn = input("Do want to add any product to cart ( Y/N ): ")
            if optn == 'Y' or optn == 'y':
                item_no = int(input("Enter the item no. you want to add to cart: "))
                a = pd.read_csv('Speakers_CS.csv')      #used iloc command of pandas
                itnm = a.iloc[item_no,1]
                itpr = a.iloc[item_no,2]
                print(f'{itnm}  Rs. {itpr}')                         
                carts.append(itnm)
                itpr_conv = int(itpr)
                amount.append(itpr_conv)

                print("Thank your product has been added to cart!!")
                Main_Menu()
            
            else:
                Main_Menu()

    elif option == 4:
            f = open('Earphone_CS.csv', 'r')
            column_names = ["SID", "Name", "Price"]
            print("\n================================================================\n")
            text = pd.read_csv("Earphone_CS.csv", names=column_names)
            print(text)
            print("\n================================================================\n")
            f.close
            
            optn = input("Do want to add any product to cart ( Y/N ): ")
            if optn == 'Y' or optn == 'y':
                item_no = int(input("Enter the item no. you want to add to cart: "))
                a = pd.read_csv('Earphone_CS.csv')      #used iloc command of pandas
                itnm = a.iloc[item_no,1]
                itpr = a.iloc[item_no,2]
                print(f'{itnm}  Rs. {itpr}')                         
                carts.append(itnm)
                itpr_conv = int(itpr)
                amount.append(itpr_conv)

                print("Thank your product has been added to cart!!")
                Main_Menu()

            else:
                Main_Menu()
    else:
        print("ERROR")
        print("Please enter correct option!!")
        Main_Menu()       
    #cart = list(carts) 

def shop_cart():
    i = 0 
    if len(carts) == 0:
        print('Your cart is empty')
        print('Do some shopping first')
        Main_Menu()
    else:    
        while i < len(carts):
            carts[i] = f'{i+1}. ' + carts[i]
            i += 1
        for z in carts:
            print(z)

    # for m in amount:
    #     print(m)

    Main_Menu()

def place_order():
    opt = input("Do you want to place order, Y/N\n>")
    if opt == 'Y' or opt == 'y':
        deli_date()
    else:
        Main_Menu()

def deli_date():
    today = date.today()
    Begindate = today
    Enddate1 = Begindate + timedelta(days=3)
    Enddate2 = Begindate + timedelta(days=2)
    Enddate3 = Begindate + timedelta(days=1)
    print("Ending date")
    print(f'1. {Enddate1}\n2. {Enddate2}\n3. {Enddate3}\n')
    abcd = input("Choose delivery date from above\n>")
    if abcd =='1':
        print(f'\nYour order will be deliver by {Enddate1}') 
        bill()
    elif abcd =='2':
        print(f'\nYour order will be deliver by {Enddate2}')
        bill()
    elif abcd =='3':
        print(f'\nYour order will be deliver by {Enddate3}')
        bill()
    else:
        print("Please enter correct option!!")
        deli_date()

def bill():
    #print(f'Your total amount is Rs.{total_amt}')
    if len(carts) == 0:
        print('Your cart is empty')
        print('I think you should shop for something')
        Main_Menu()
    else:
        sum_amt = sum(amount)
        print("\n------------------------------------------")
        print('\n               ZROMA               \n')
        print("Items\n")
        for x in carts:
            print(x)
        print(f'Your total amount is Rs.{sum_amt}\n')
        print("\nThank you for shopping from ZROMA")
        print("\n------------------------------------------")

def remove_item():
    for z in carts:
        print(z)
        print()
    remove_num = int(input("Enter the item no. you want to remove: "))
    
    if remove_num <= len(carts):
        carts.pop(remove_num - 1)
        amount.pop(remove_num -1)
    else:
        print("Item not in cart! \n Please enter correct number\n")
        print()
        remove_item()

    for x in carts:
        print(x)
    # for x in amount:
    #     print(x)
    # else:
    #     print("Item not in cart! \n Please enter correct number")
    #     remove_item()

    Main_Menu()


def run():
    get_phone()
    get_email()
    get_pin_code()
    get_address()
    Main_Menu()s
run()
