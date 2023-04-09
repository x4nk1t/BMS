import functions

functions.welcome()
loop = True

while loop == True:
    functions.list_options()
    
    num = int(input("Enter value of the option: "))
    if num == 1:
        functions.order_bike()
    elif num == 2:        
        functions.add_stock()
    elif num == 3:
        functions.exit_system()
        loop = False
    else:
        functions.invalid_input()