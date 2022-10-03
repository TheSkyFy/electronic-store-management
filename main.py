import csv
import os
import re #regEX
import pandas as pd
from datetime import *

#--------------------------------------Display Menus-----------------------------------------------------

def admin_menu():
    print("\n======================\n")
    print("1.Add")
    print("2.Delete")
    print("3.Modify")
    print("4.Display All")
    print("5.Exit")
    print("\n======================\n")
    menu_choice()

def Main_Menu():
    print("\n======================\n")
    print("1.Display Category")
    print("2.Cart")
    print("3.Remove item")
    print("4.Place order")
    print("5.Exit")
    print("\n======================\n")
    menu_option()

#menu_choice() --> choice for admin menu
#menu_option() --> choice for customer menu

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
    print("\n-------------------WELCOME TO FERGO STORE--------------------\n")
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


#--------------------------------------Customer Login--------------------------------------------------

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
        print("\nThank you for visiting our store\n")
    else:
        print("ERROR\n")
        print("PLease enter a valid input\n")
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
            print("\n================================================================\n\n")
            
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
            print("\n================================================================\n\n")
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
            print("\n================================================================\n\n")
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
            print("\n================================================================\n\n")
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
        print("\n============================================\n")
        print('\n               ZROMA               \n')
        print("Items\n")
        for x in carts:
            print(x)
        print(f'Your total amount is Rs.{sum_amt}\n')
        print("\nThank you for shopping from ZROMA\n")
        print("\n============================================\n")

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

#-------------------------------------------------ADMIN Login--------------------------------------------------

def menu_choice():
    ch = int(input("Enter the required option no.\n>"))
    if ch == 1:
        admin_add()
    elif ch == 2:
        admin_del()
    elif ch == 3:
        admin_mod()
    elif ch == 4:
        admin_dis()
    elif ch == 5:
        print("Thank you for using this software")
        print('''
    3..................
    2..............
    1..........
        ''')
        print('Software closed')
        pass
    else:
        print("ERROR\n")
        print("PLease enter a valid input\n")
        menu_choice()


def admin_add():
    product_categ()
    ch = int(input("Choose the category in which you want to add item: "))
    if ch == 1:
        L = []
        s_no = int(input("Enter S.no: "))
        p_name = input("Enter name of the phone: ")
        pp = int(input("Enter price of the phone: "))
        L.append(s_no)
        L.append(p_name)
        L.append(pp)

        file_obj = open("Phones2_CS_project.csv",'a')
        writer_obj = csv.writer(file_obj)
        writer_obj.writerow(L)
        file_obj.close()
        pass

    if ch == 2:
        L = []
        s_no = int(input("Enter S.no: "))
        p_name = input("Enter name of the laptop: ")
        pp = int(input("Enter price of the laptop: "))
        L.append(s_no)
        L.append(p_name)
        L.append(pp)

        file_obj = open("Laptop_CS_project.csv",'a')
        writer_obj = csv.writer(file_obj)
        writer_obj.writerow(L)
        file_obj.close()
        pass

    if ch == 3:
        L = []
        s_no = int(input("Enter S.no: "))
        p_name = input("Enter name of the speaker: ")
        pp = int(input("Enter price of the speaker: "))
        L.append(s_no)
        L.append(p_name)
        L.append(pp)

        file_obj = open("Speakers_CS.csv",'a')
        writer_obj = csv.writer(file_obj)
        writer_obj.writerow(L)
        file_obj.close()
        pass

    if ch == 4:
        L = []
        s_no = int(input("Enter S.no: "))
        p_name = input("Enter name of the earphone: ")
        pp = int(input("Enter price of the earphone: "))
        L.append(s_no)
        L.append(p_name)
        L.append(pp)

        file_obj = open("Earphone_CS.csv",'a')
        writer_obj = csv.writer(file_obj)
        writer_obj.writerow(L)
        file_obj.close()
        pass

    else:
        print("All changes have been made")
        #To continue after admin_menu()
        pass

def admin_del():
    product_categ()
    choice = int(input("Select the category in which you want to delete item: "))
    if choice == 1:
        lines = list()
        del_ch = input("Enter the item no. which you want to delete: ")
        with open('Phones_CS_project.csv', 'r') as reader:
            read_obj = csv.reader(reader)
            for row in read_obj:
                lines.append(row)
                for field in row:
                    if field == del_ch:
                        lines.remove(row)

        with open('Phones_CS_project.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    elif choice == 2:
        lines = list()
        del_ch = input("Enter the item no. which you want to delete: ")
        with open('Laptop_CS_project.csv', 'r') as reader:
            read_obj = csv.reader(reader)
            for row in read_obj:
                lines.append(row)
                for field in row:
                    if field == del_ch:
                        lines.remove(row)

        with open('Laptop_CS_project.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        
    elif choice == 3:
        lines = list()
        del_ch = input("Enter the item no. which you want to delete: ")
        with open('Speakers_CS.csv', 'r') as reader:
            read_obj = csv.reader(reader)
            for row in read_obj:
                lines.append(row)
                for field in row:
                    if field == del_ch:
                        lines.remove(row)

        with open('Speakers_CS.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        
    elif choice == 4:
        lines = list()
        del_ch = input("Enter the item no. which you want to delete: ")
        with open('Earphone_CS.csv', 'r') as reader:
            read_obj = csv.reader(reader)
            for row in read_obj:
                lines.append(row)
                for field in row:
                    if field == del_ch:
                        lines.remove(row)

        with open('Earphone_CS.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        # del_ch = input("Enter the item no. which you want to delete: ")
        # with open('Phones_CS_project.csv', newline='') as csvfile:
        #     csvreader = csv.reader(csvfile)
        #     output = [x for x in csvreader if x != del_ch]

        # with open('temp.csv', 'w', newline='') as csvfile:
        #     csvreader = csv.writer(csvfile,)
        #     for x in output:
        #         csvreader.writerow(x)
        
    else:
        print("All changes have been made")
        print("Software Closed")
        pass
    print("Returing to main menu.......")
    admin_menu()


def admin_mod():
    product_categ()
    choice = int(input("Select the category in which you want to modify data: "))
    if choice == 1:
        L = []
        mod_ch = input("Enter the item no. which you want to modify: ")
        with open('Phones_CS_project.csv', 'r') as reader:
            read_obj = csv.reader(reader)
            for row in read_obj:
                L.append(row)
                for f in row:
                    if f == mod_ch:
                        print()
                        print(f'Product Name: {row[1]}')
                        print(f'Price: {row[2]}')
                        print()

                        ch1 = input('Do you want to change Product Name (Y/N)?\n>')
                        if ch1 == 'Y' or ch1 == 'y':
                            x= input("Enter the new Name of product\n>")
                            row[1]=x
                            print('Product Name updated successfully!')
                        else:
                            pass

                        ch2 = input('Do you want to change Price (Y/N)?\n>')
                        if ch2 == 'Y' or ch2 == 'y':
                            y= int(input("Enter the new Price of product\n>"))
                            row[2]=y
                            print('\nPrice updated sucessfully!')
                        else:
                            pass

        with open('Phones_CS_project.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(L)
        
    elif choice == 2:
        L = []
        mod_ch = input("Enter the item no. which you want to modify: ")
        with open('Laptop_CS_project.csv', 'r') as reader:
            read_obj = csv.reader(reader)
            for row in read_obj:
                L.append(row)
                for f in row:
                    if f == mod_ch:
                        print()
                        print(f'Product Name: {row[1]}')
                        print(f'Price: {row[2]}')
                        print()

                        ch1 = input('Do you want to change Product Name (Y/N)?\n>')
                        if ch1 == 'Y' or ch1 == 'y':
                            x= input("Enter the new Name of product\n>")
                            row[1]=x
                            print('Product Name updated successfully!')
                        else:
                            pass

                        ch2 = input('Do you want to change Price (Y/N)?\n>')
                        if ch2 == 'Y' or ch2 == 'y':
                            y= int(input("Enter the new Price of product\n>"))
                            row[2]=y
                            print('\nPrice updated sucessfully!')
                        else:
                            pass

        with open('Laptop_CS_project.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(L)
        
    elif choice == 3:
        L = []
        mod_ch = input("Enter the item no. which you want to modify: ")
        with open('Speakers_CS.csv', 'r') as reader:
            read_obj = csv.reader(reader)
            for row in read_obj:
                L.append(row)
                for f in row:
                    if f == mod_ch:
                        print()
                        print(f'Product Name: {row[1]}')
                        print(f'Price: {row[2]}')
                        print()

                        ch1 = input('Do you want to change Product Name (Y/N)?\n>')
                        if ch1 == 'Y' or ch1 == 'y':
                            x= input("Enter the new Name of product\n>")
                            row[1]=x
                            print('Product Name updated successfully!')
                        else:
                            pass

                        ch2 = input('Do you want to change Price (Y/N)?\n>')
                        if ch2 == 'Y' or ch2 == 'y':
                            y= int(input("Enter the new Price of product\n>"))
                            row[2]=y
                            print('\nPrice updated sucessfully!')
                        else:
                            pass

        with open('Speakers_CS.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(L)

    elif choice == 4:
        L = []
        mod_ch = input("Enter the item no. which you want to modify: ")
        with open('Earphone_CS.csv', 'r') as reader:
            read_obj = csv.reader(reader)
            for row in read_obj:
                L.append(row)
                for f in row:
                    if f == mod_ch:
                        print()
                        print(f'Product Name: {row[1]}')
                        print(f'Price: {row[2]}')
                        print()

                        ch1 = input('Do you want to change Product Name (Y/N)?\n>')
                        if ch1 == 'Y' or ch1 == 'y':
                            x= input("Enter the new Name of product\n>")
                            row[1]=x
                            print('Product Name updated successfully!')
                        else:
                            pass

                        ch2 = input('Do you want to change Price (Y/N)?\n>')
                        if ch2 == 'Y' or ch2 == 'y':
                            y= int(input("Enter the new Price of product\n>"))
                            row[2]=y
                            print('\nPrice updated sucessfully!')
                        else:
                            pass

        with open('Earphone_CS.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(L)

    else:
        print("All changes have been made")
        print("Software Closed")
        pass
    print()
    print("Returing to main menu.......")
    admin_menu()
    
def admin_dis():
    product_categ()
    option = int(input("Enter the required option no.\n>")) 
    if option == 1:
            column_names = ["SID", "Name", "Price"]
            print("\n================================================================\n")
            text = pd.read_csv("Phones_CS_project.csv", names=column_names)
            print(text)
            print("\n================================================================\n\n")
            
    elif option == 2:
            f = open('Laptop_CS_project.csv', 'r')
            column_names = ["SID", "Name", "Price"]
            print("\n================================================================\n")
            text = pd.read_csv("Laptop_CS_project.csv", names=column_names)
            print(text)
            print("\n================================================================\n\n")
            f.close

    elif option == 3:
            f = open('Speakers_CS.csv', 'r')
            column_names = ["SID", "Name", "Price"]
            print("\n================================================================\n")
            text = pd.read_csv("Speakers_CS.csv", names=column_names)
            print(text)
            print("\n================================================================\n\n")
            f.close
            
    elif option == 4:
            f = open('Earphone_CS.csv', 'r')
            column_names = ["SID", "Name", "Price"]
            print("\n================================================================\n")
            text = pd.read_csv("Earphone_CS.csv", names=column_names)
            print(text)
            print("\n================================================================\n\n")
            f.close
    elif option == 5:
        admin_menu()       
    else:
        print("ERROR")
        print("Please enter correct option!!")
        admin_dis()     
    admin_menu()
    

def login_pass():
    print("*"*30,"ADMIN LOGIN","*"*30)
    login1 = "12345678"
    pswd1 = "Yowai_Mo"
    login = input("KINDLY ENTER LOGIN ID: ")
    print()
    while login != login1:
        login = input("KINDLY RE-ENTER CORRECT LOGIN ID: ")
        print()
    pswd = input("KINDLY ENTER CORRECT PASSWORD: ")
    while pswd != pswd1:
        pswd = input("KINDLY RE-ENTER CORRECT PASSWORD: ")
            
    print()
    print("*"*24,"SUCCESSFULLY LOGGED IN!","*"*27)
    #menu_choice()
    #Write program from choices

#-------------------------------------------Main Run------------------------------------------------------

def run():
    print("1. Customer")
    print("2. Admin")
    ch = int(input("Enter the serial no.: "))
    if ch == 1:
        get_phone()
        get_email()
        get_pin_code()
        get_address()
        Main_Menu()
    elif ch == 2:
        login_pass()
        admin_menu()
        pass
run()
