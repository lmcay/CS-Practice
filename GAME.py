def validation_main(x):
    match x:
        case "1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"0":
            return x
        case _:
            print("Invalid Input")

def BACK():
    while True:
        back = input("Press 0 to go back to front page: ")
        if back == "0":
            return back
            break
        else:
            print("Invalid Input")

def CONFIRM_ORDER():
    while True:
        ask_if_order = input("Do you want to order? [1. Yes 0. No]: ")
        if ask_if_order == "0" or ask_if_order == "1":
            return ask_if_order
            break
        else:
            print("Input is not within the choices")

def validation_order():
    while True:
        code = input("Input order number: ")
        match code:
            case "1"|"2"|"3":
                return code
                break
            case _:
                print("Invalid order input")

def confirm_checkout(x):
    match x:
        case "1"|"2"|"3":
            return x
        case _:
            print("Invalid Input")

##---------------------------PARTY FOOD LIST-------------------------------------##
pack = "(Good for 20 People)"
iced_tea = "Iced Tea Bottomless"
water = "Ice Mineral Water"

party_food = [["Package 1: Occasional Package", "Package 2: Party Package Overload", "Package 3: Formal Package"],
              [pack, pack, pack],
              ["Mixed Veggies and Seafood", "Fried Garlic Rice", "Roast Beef"],
              ["Spaghetti & Meatballs", "Hotdogs", "Fried garlic and butter rice"],
              ["Plain Rice", "Crispy Chicken Tacos", "Chicken Cordon Bleu"],
              ["Garlic Chicken", "Pizza Hawaiian", "Roast Pork with Oyster Sauce"],
              ["Roast Beef", "Chicken Wings", "Pescada en Salsa Verde"],
              ["Pork and Chicken BBQ", "BBQ Pork Sliders", "Baked Spaghetti "],
              ["Fish Fillet", "Spaghetti & Meatballs", "Mixed Vegetables with Ham "],
              ["Pork Lumpia", "Sandwiches Roasted Beef", "Buko Fruit Salad  "],
              [iced_tea, iced_tea, iced_tea],
              [water, water, water],
              ["Price: 10,261 PHP", "Price: 11,707 PHP", "Price: 12,404PHP"]]
##---------------------------PARTY FOOD LIST-------------------------------------##

true = 1
total = 0
p_food_1, p_food_2, p_food_3 = 0,0,0

while true == 1:
    print("1. About Us\n2. Party Food\n3. Rentals and Party Needs\n4. Catering Services\n5. FAQ\n6. Contact Us\n7. Terms of Payment\n8. View your cart")
    while True:
        main_option = input("How can we help you today? ")
        main_option = validation_main(main_option)
        
        if main_option == "1": #ABOUT US OPTION 1
            print("Content")
            BACK()
            break
        elif main_option == "2": #PARTY FOOD OPTION 2
            for package in party_food:
                print("|", package[0], " "*(29-len(package[0])), "|", package[1], " "*(33-len(package[1])), "|", package[2], " "*(29-len(package[2])), "|")

            ask_if_order = CONFIRM_ORDER()
            if ask_if_order == "1":
                code = validation_order()
                if code == "1":
                    price = 10261
                    p_food_1 += 1
                elif code == "2":
                    price = 11707
                    p_food_2 += 1
                else:
                    price = 12404
                    p_food_3 += 1
                total += price
                print("We have added your order to your cart! Make sure to check it out!")
            else:
                break
        
        elif main_option == "5": #FAQ OPTION 5
            print("FAQ")
            BACK()
            break
        elif main_option == "6": #CONTACT US OPTION 6
            print("CONTACT US")
            BACK()
            break
        elif main_option == "7": #CART OPTION 7
            print("TERMS OF PAYMENT")
            BACK()
            break
        elif main_option == "8": #VIEW YOUR CART OPTION 8
            print("Your current total is", total)
            if total != 0:
                print("Your current orders are")
                if p_food_1 != 0:
                    print(p_food_1, "x Party Food Package 1")
                    for package in party_food:
                        print("|", package[0], " "*(29-len(package[0])), "|")
                if p_food_2 != 0:
                    print(p_food_2, "x of Party Food Package 2")
                    for package in party_food:
                        print("|", package[1], " "*(33-len(package[1])), "|")
                if p_food_3 != 0:
                    print(p_food_3, "x of Party Food Package 3")
                    for package in party_food:
                        print("|", package[2], " "*(29-len(package[2])), "|")
                while True:
                    checkout = input("Do you want to proceed with your order? [1. Yes 2. Back to homepage 3. Reset my order]")
                    checkout = confirm_checkout(checkout)
                    if checkout == "1":
                        true2 = 1
                        while true2 == 1:
                            name = input("Full Name: ")
                            number = input("Contact Number: ")
                            address = input("Venue Address: ")
                            date_order = input("Input date of order (Ex. January 3,2022): ")
                            date_req = input("Input date of order deadline (Ex. January 13, 2022): ")
                            guest_count = input("Guest Count: ")
                            payment = input("Mode of Payment [GCASH/Paymaya]")
                            print("FUll Name:",name,"\nContact Number:", number,"\nVenue Address:",address,"\nDate of order:",date_order,"\nDate of order deadline:",date_req,"\nGuest Count:",guest_count,"\nMode of Payment:",payment)
                            print("Make sure to print out all details accurately as our management will check the data and agreement created. If any of the data are inaccurate, we will terminate the order requested.")

                            while True:
                                confirmation = input("Have you confirmed your details? [1. Yes 2. Reset my details 3. Reset my order]")
                                if confirmation == "1":
                                    print("Thank you", name, "for placing this order. Your order will be process and you will be contacted by one of our staff within 1-3 business days. ")
                                    print("Your bill came to a total of", total, ". Prepare 50% of your total bill which is" , total/2, "php for the processing of your order.")
                                    true2 = 0
                                    total = 0
                                    break
                                elif confirmation == "2":
                                    break
                                elif confirmation == "3":
                                    total = 0
                                    true2 = 0
                                    break
                                else:
                                    print("Invalid Input")
                        else:
                            while True:
                                order_again = input("Do want to create another order? [1. Yes 2. No")
                                if order_again == "1":
                                    total = 0
                                    p_food_1, p_food_2, p_food_3 = 0,0,0
                                    break
                                elif order_again == "2":
                                    true = 0
                                    break
                                else:
                                    print("Invalid Input")
                        break
                    elif checkout == "2":
                        break
                    elif checkout == "3":
                        total = 0
                        p_food_1, p_food_2, p_food_3 = 0,0,0
                        break
                    else:
                        continue
                break
            else:
                BACK()

                
        elif main_option == "0":
            true = 0
            break
        
        else:
            
            continue
        break
else:
    print("Thanks for using this program")
        
