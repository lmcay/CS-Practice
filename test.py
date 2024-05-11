def four_option(option):
    if option == "1":
        option = 1
    elif option == "2":
        option = 2
    elif option == "3":
        option = 3
    elif option == "4":
        option = 4
    return option

def back():
    while True:
        back = input("Press [0] to go back.")
        if back != "0":
            print("Invalid Input")
        else:
            break

def ask_if_order():
    while True:
        ask_order = input("Input: ")
        if ask_order == "O":
            return ask_order
            break
        elif ask_order == "B":
            return ask_order
            break
        else:
            print("Invallid Input")

def pack_option():
    while True:
        pack_code = input("Input Pack Code: ")
        if pack_code == "1":
            pack_code = 1
            return pack_code
            break
        elif pack_code == "2":
            pack_code = 2
            return pack_code
            break
        elif pack_code == "3":
            pack_code = 3
            return pack_code
            break
        else:
            print("Invalid Input")
        

def rentalMenuPacks():
    print("""\t\t[1]Display Pack 1: 1050
\t\t[2]Display Pack 2: 1200
\t\t[3]Display Pack 3: 1500
\t\t[O]Order\t[B]-Back""")

def rentalMenuItems():
    print("""\t\t[1]Tents - 100
\t\t[2]Tables - 100
\t\t[3]Chairs - 20
\t\t[4]Table Cloth Linen -  50
\t\t[5]Ribbons - 15
\t\t[6]Complete Utensils and Silverware - 50((Spoon and Fork Set, Teaspoon, Serving Spoon, Glass, Plates and more...))
\t\t[O]-Order\t[B]\tBack""")

def options():  
    print("""\t\t[1]Packs
    \t\t[2]Individal Items
    \t\t[3]Cart
    \t\t[4] Back""")

def item_option():
    while True:
        item_code = input("Input Pack Code: ")
        if item_code == "1":
            item_code = 1
            return item_code
            break
        elif item_code == "2":
            item_code = 2
            return item_code
            break
        elif item_code == "3":
            item_code = 3
            return item_code
            break
        elif item_code == "4":
            item_code = 4
            return item_code
            break
        elif item_code == "5":
            item_code = 5
            return item_code
            break
        elif item_code == "6":
            item_code = 6
            return item_code
            break   
        else:
            print("Invalid Input")

def numberOfItems():
    while True:
        try:
            quantity = int(input("How many do you want to add? "))
            if quantity > 0:
                return quantity
                break
            else:
                print("Input must be greater than 0")
        except ValueError:
            print("Input must be an integer")

def show_outputs():
    if total != 0:
        if pack1 != 0:
            print("PACK 1:", pack1, "\tP", p1)
        if pack2 != 0:
            print("PACK 2:", pack2, "\tP", p2)
        if pack3 != 0:
            print("PACK 3:", pack3, "\tP", p3)
        if in1 != 0:
            print("Tents:", in1, "\tP", p4)
        if in2 != 0:
            print("Tables:", in2, "\tP", p5)
        if in3 != 0:
            print("Chairs:", in3, "\tP", p6)
        if in4 != 0:
            print("Table Cloth Linen:", in4, "\tP", p7)
        if in5 != 0:
            print("Ribbons:", in5, "\tP", p8)
        if in6 != 0:
            print("Complete Utensils and Silverware:", in6, "\tP", p9)
        print("Your total is", total)
    else:
        print("There are no current items in your shopping list.")

def ask_reset():
    while True:
        ask_reset = input("\t[R]Reset Order\t[B]Back")
        if ask_reset == "R" or ask_reset == "B":
            return ask_reset
            break
        else:
            print("Invalid Input")

def calc():
    if item_code == 1:
        total += 100*quantity
        in1 += quantity
        p4 += in1*100
    elif item_code == 2:
        total += 100*quantity
        in2 += quantity
        p5 += in2*100
    elif item_code == 3:
        total += 20*quantity
        in3 += quantity
        p6 += in3*20
    elif item_code == 4:
        total += 50*quantity
        in4 += quantity
        p7 += in4*50
    elif item_code == 5:
        total += 15*quantity
        in5 += quantity
        p8 += in5*15
    else:
        total += 30*quantity
        in6 += quantity
        p9 += in6*30
    
    
pack1,pack2,pack3,pack4=0,0,0,0
in1,in2,in3,in4,in5,in6 = 0,0,0,0,0,0
p1,p2,p3,p4,p5,p6,p7,p8,p9 = 0,0,0,0,0,0,0,0,0
total = 0
while True:
    options()
    select = input("How can we help you today?")
    rental_option = four_option(select)

    if rental_option == 1:
        rentalMenuPacks()
        ask_order = ask_if_order()
        if ask_order == "O":
            pack_code = pack_option()
            if pack_code == 1:
                total += 1050
                pack1 += 1
                p1 += pack1*1050
            elif pack_code == 2:
                total += 1200
                pack2 += 1
                p2 += pack2*1200
            else:
                total += 1500
                pack3 += 1
                p3 += pack3*1500
            print("Successfully added to your cart")
            continue #(THIS IS TO GO BACK TO THE OPTIONS)
        else:
            continue

    elif rental_option == 2:
        rentalMenuItems()
        ask_order = ask_if_order()
        if ask_order == "O":
            item_code = item_option()
            quantity = numberOfItems()
            calc()
##            if item_code == 1:
##                total += 100*quantity
##                in1 += quantity
##                p4 += in1*100
##            elif item_code == 2:
##                total += 100*quantity
##                in2 += quantity
##                p5 += in2*100
##            elif item_code == 3:
##                total += 20*quantity
##                in3 += quantity
##                p6 += in3*20
##            elif item_code == 4:
##                total += 50*quantity
##                in4 += quantity
##                p7 += in4*50
##            elif item_code == 5:
##                total += 15*quantity
##                in5 += quantity
##                p8 += in5*15
##            else:
##                total += 30*quantity
##                in6 += quantity
##                p9 += in6*30
            print("Successfully added to your cart")
            continue#(THIS IS TO GO BACK TO THE OPTIONS)
        else:
            continue
        
    elif rental_option == 3:
        show_outputs()
        ask_resets = ask_reset()
        if ask_resets == "R":
            pack1,pack2,pack3,pack4=0,0,0,0
            in1,in2,in3,in4,in5,in6 = 0,0,0,0,0,0
            p1,p2,p3,p4,p5,p6,p7,p8,p9 = 0,0,0,0,0,0,0,0,0
            total = 0
        else:
            continue

    else:
        print("Invalid Input")
        

