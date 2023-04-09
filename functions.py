from datetime import datetime

NAME_INDEX = 0
COMPANY_INDEX = 1
COLOR_INDEX = 2
QUANTITY_INDEX = 3
PRICE_INDEX = 4

BILLS_PATH = "./bills/"
SHIPPING_PATH = './stocks/'

user_current_details = {}

def welcome():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\tWelcome to Bike Management System")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")

def list_options():
    print("\n")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    print("1. Order Bikes")
    print("2. Add Stock")
    print("3. Exit")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")

def add_stock():
    display_bikes()

    selected_id = 0

    while selected_id == 0:
        try:
            selected_id = int(input("Enter the bike id to add the quantity: "))
        except:
            print("Please enter valid bike id.")
    
    bike_list = get_bike_list()
    selected_bike = bike_list.get(selected_id)

    if selected_bike == None:
        print("Bike not found! Would you like to add new bike?\n1. Yes \n2. No")
        yesno = 0

        while yesno < 1 or yesno > 2:
            try:
                yesno = int(input("Enter the value of option: "))

                if yesno > 2:
                    print("\nPlease enter either 1 or 2!\n")
            except:
                print("Please enter either 1 or 2!")

        if yesno == 1:
            add_new_bike()
        else:
            add_stock()
    else:
        add_current_stock(selected_id)

def add_current_stock(bike_id):
    bike_list = get_bike_list()
    bike = bike_list.get(bike_id)

    name = bike[NAME_INDEX]
    company = bike[COMPANY_INDEX]
    color = bike[COLOR_INDEX]
    price = bike[PRICE_INDEX]
    shipping_name = input("Enter the name of shipping company: ")
    shipping_address = input("Enter the address of shipping company: ")
    delivery_date = input("Enter the delivery date: ")

    bike_quantity = 0
    while bike_quantity < 1:
        try:
            bike_quantity = int(input("Enter the quantity to add: "))
        except:
            print("\nPlease enter a valid number greater than 0\n")
    
    shipping_cost = 0
    while shipping_cost < 0:
        try:
            shipping_cost = int(input("Enter the shipping cost: "))
        except:
            print("\nPlease enter valid cost for devliery!")
    
    amount_paid = int(price.replace("$", "")) * bike_quantity

    content = f"""Shipping Company: {shipping_name} \nShipping Address: {shipping_address} \nDelivery Date: {delivery_date} \n\nBike Name: {name} \nCompany Name: {company} \nColor: {color} \nQuantity: {bike_quantity} \nPrice: {price} \nAmount paid: ${amount_paid}"""

    time_today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    file_name = SHIPPING_PATH + shipping_name + "_" + time_today + ".txt"
    file = open(file_name, "w")
    file.write(content)
    file.close()

    add_bike_stock(bike_id, bike_quantity)

    print("\nSuccessfully added the quantity to the stock.")

def add_new_bike():
    bike_name = input("Enter the name of bike: ")
    company_name = input("Enter the company of bike: ")
    bike_color = input("Enter the color of bike: ")

    bike_quantity = 0
    while bike_quantity < 1:
        try:
            bike_quantity = int(input("Enter the quantity of the bike: "))
        except:
            print("\nPlease enter a valid number greater than 0\n")

    bike_price = 0
    while bike_price < 1:
        try:
            bike_price = int(input("Enter the price of bike: "))
        except:
            print("\nPlease enter a valid number greater than 0\n")
    
    print("\nPlease confirm the details of the new bike\n")
    print("Bike Name: "+bike_name+"\nCompany Name: "+company_name+"\nColor: "+bike_color+"\nQuantity:"+str(bike_quantity)+"\nPrice: $"+str(bike_price))

    print("\nIs is correct?\n1. Yes \n2. No")
    yesno = 0
    while yesno < 1 or yesno > 2:
        try:
            yesno = int(input("Enter the value of option: "))

            if yesno > 2:
                print("\nPlease enter either 1 or 2!\n")
        except:
            print("\nPlease enter either 1 or 2!\n")

    if yesno == 1:
        file = open('bike.txt', 'a')
        file.write("\n"+bike_name+","+company_name+","+bike_color+","+str(bike_quantity)+",$"+str(bike_price))
        file.close()

        print("\nSuccessfully added the bike to the stock!")
    else:
        print("\nPlease enter the details again!\n")
        add_new_bike()

def get_user_details():
    print("")
    name = input("Enter your full name: ")
    address = input("Enter your address: ")
    email = input("Enter your email: ")

    phone = ""

    while phone == "":
        try:
            phone = int(input("Enter your phone number: "))
        except:
            print("\nPlease enter valid number for phone!\n")
    
    details = {}
    details["name"] = name
    details["address"] = address
    details["phone"] = phone
    details["email"] = email

    global user_current_details
    user_current_details = details
    
    return details

def exit_system():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\tThank you for using Bike Management System")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def bike_not_found():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("That bike id is not available. Please choose from 1 -", len(get_bike_list()))
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    order_bike()

def purchase_more():
    print("\n")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\tThank you for purchasing")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    yesno = 0
    print("Would you like to purchase more?\n1. Yes \n2. No ")
    while yesno < 1 or yesno > 2:
        try:
            yesno = int(input("Enter the value of option: "))

            if yesno > 2:
                print("\nPlease enter either 1 or 2!\n")
        except:
            print("\nPlease enter either 1 or 2!\n")

    if yesno == 1:
        order_bike()

def create_bill(bike_id, quantity):
    bike_list = get_bike_list()
    bike = bike_list.get(bike_id)

    if user_current_details == {}:
        user_details = get_user_details()
    else:
        user_details = user_current_details
        
    name = user_details.get("name")
    address = user_details.get("address")
    phone = user_details.get("phone")
    email = user_details.get("email")
    amount_paid = int(bike[PRICE_INDEX].replace("$", "")) * quantity

    bike_name = bike[NAME_INDEX]
    company_name = bike[COMPANY_INDEX]
    bike_color = bike[COLOR_INDEX]
    bike_price = bike[PRICE_INDEX]
    date_today = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    time_today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    remove_bike_stock(bike_id, quantity)

    file_name = BILLS_PATH + str(phone) + "_" + name + "_"+ time_today +".txt"
    file = open(file_name, "w")
    content = f"""Name: {name} \nAddress: {address} \nPhone: {phone} \nEmail: {email}\n\nBike Name: {bike_name} \nCompany Name: {company_name} \nColor: {bike_color} \nPrice: {bike_price}\nQuantity purchased: {quantity} \nAmount Paid: ${amount_paid} \nDate: {date_today} \nTime: {time}"""
    file.write(content)
    file.close()
    
    print("\nYour bill\n")
    print(content)

    purchase_more()
    
def add_bike_stock(bike_id, quantity_to_add):
    bike_list = get_bike_list()
    bike = bike_list.get(bike_id)
    new_content = []

    read = open("bike.txt", "r")

    for line in read:
        detail = line.replace("\n", "").split(",")
        bike_quantity = int(detail[QUANTITY_INDEX])

        if detail[NAME_INDEX] == bike[NAME_INDEX]:
            detail[QUANTITY_INDEX] = str(bike_quantity + quantity_to_add)
            
        new_content.append(','.join(detail))
    
    read.close()

    file = open("bike.txt", "w")
    file.write('\n'.join(new_content))
    file.close()

def remove_bike_stock(bike_id, quantity_to_remove):
    bike_list = get_bike_list()
    bike = bike_list.get(bike_id)
    new_content = []

    read = open("bike.txt", "r")

    for line in read:
        detail = line.replace("\n", "").split(",")
        bike_quantity = int(detail[QUANTITY_INDEX])

        if detail[NAME_INDEX] == bike[NAME_INDEX]:
            detail[QUANTITY_INDEX] = str(bike_quantity - quantity_to_remove)
            
        new_content.append(','.join(detail))
    
    read.close()

    file = open("bike.txt", "w")
    file.write('\n'.join(new_content))
    file.close()
    

def out_of_stock(bike_name):
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\t", bike_name, "is currently out of stock!")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
       
def less_stock(name, quantity):
    print("\n")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\tThe quantity you need of", name, "is not available.")
    print("\tAvailable Quantity:", quantity)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
def display_bikes():
    print("\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Bike ID\t\tBike Name\t\tCompany Name\tColor\t\tQuantity \tPrice")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    file = open("bike.txt", "r")
    id = 1

    for line in file:
        print(id, "\t\t"+ line.replace(",", "\t\t"))
        id = id + 1
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    file.close()

def get_bike_list():
    file = open("bike.txt", "r")
    id = 1

    bikes = {}

    for line in file:
        bikes[id] = line.replace("\n", "").split(",")
        id = id + 1
    
    return bikes

def order_bike():
    bike_list = get_bike_list()

    loop = True
    while loop == True:
        display_bikes()
        print("\n")
        bike_id = 0
        while bike_id == 0:
            try:
                bike_id = int(input("Enter the id of the bike you want to purchase: "))
            except:
                print("Please enter valid number for bike id!")

        if bike_id > len(bike_list) or bike_id < 1:
            bike_not_found()
        else:
            validate_quantity(bike_id)
            loop = False

def validate_quantity(bike_id):
    bike_list = get_bike_list()
    
    bike = bike_list.get(bike_id)
    name = bike[NAME_INDEX]
    quantity = int(bike[QUANTITY_INDEX])
    
    if quantity > 1:
        loop = True
        while loop == True:
            purchase_quantity = 0

            while purchase_quantity == 0:
                try:
                    purchase_quantity = int(input("Enter the quantity you want to purchase: "))
                except:
                    print("\nPlease enter valid number for quantity!\n")
            
            if purchase_quantity > 0:
                if quantity >= purchase_quantity:
                    loop = False
                    
                    create_bill(bike_id, purchase_quantity)
                else:
                    less_stock(name, quantity)
            else:
                print("Please enter a valid amount!")
    else:
        out_of_stock(name)
