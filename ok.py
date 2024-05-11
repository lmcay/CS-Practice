
def MENU_OPTION():
    menu_option = 0
    while menu_option < 1 or menu_option > 3:
        try:
            menu_option = int(input("What can we do for you today? "))
            if menu_option < 1 or menu_option > 3:
                print("Inputted Value is not on the choices. Try again")
            else:
                return menu_option
        except ValueError:
            print("Input must be an integer.Try again")
        
def BACK_OPTION():

    while True:
        try:
            back = int(input("Press 0 to go back"))
            if back == 0:
                break
            else:
                print("Inputted Value is not on the choices. Try again")
        except:
            print("Input must be an integer.Try again")
            
def ORDER():

    while True:
        try:
            order = int(input("Do you want to order[0. No(Back to HomePage) 1. Yes]: "))
            if order == 0:
                break
            elif order == 1:
                return order
                break
            else:
                print("Inputted Value is not on the choices. Try again")
        except:
            print("Input must be an integer.Try again")

def ORDERCODE():

    while True:
        order_code = input("Input your order code: ")
        if order_code == "W1":
            print("W1 PRICE")
            return order_code
            break
        else:
            print("Code Invalid")
            
def FINAL_VALIDATION():
    
    while True:
        try:
            final_valid = int(input("Do you want to order[0. No(Back to HomePage) 1. Yes]: "))
            if final_valid == 0:
                return final_valid
                break
            elif final_valid == 1:
                return final_valid
                break
            else:
                print("Inputted Value is not on the choices. Try again")
        except:
            print("Input must be an integer.Try again")
        



        




            
condition = 1

while condition == 1:
    print("1. First\n2. Info\n3. Exit")

    while True:
        menu_option = MENU_OPTION()

        if menu_option == 1:
            print("FIRST")

            BACK_OPTION()
            break

##        elif menu_option == 2:
##            print("Packages here")
##
##            while True:
##                order = ORDER()
##
##                if order == 0:
##                    continue
##                elif order == 1:
##                    print("What do you want to order")
##                    ordercode = ORDERCODE()
##
##                    #if ordercode == "code order":
##                    #then print receipt
##                    print(ordercode)
##                    while True:
##                        final_valid = FINAL_VALIDATION()
##                        if final_valid == 1:
##                            print("Thanks for your order. Expect it on two to three business days")
##                            break
##                        else:
##                            break
##                break
        elif menu_option == 3:
            condition = 0
            break
        break
    
else:
    print("done")
