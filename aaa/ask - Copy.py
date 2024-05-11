total_addon_price = 0

total_package = 0

discount = .05

package_discount = 0

package_cost = 0

total_cost = 0

total_addon_cost= 0

print("\t\t\tTHE PARTY GUYS")

for i in range(1, 51):

    print("~", end='')

print("")



def package_1():

    print("Package 1")

    print("\t- 4 unit JBL 12” Line array speakers")

    print("\t- 4 units JBL 12” Professional delay speakers")

    print("\t- 2 units Professional Subwoofer System")

    print("\t- 2 units Professional Subwoofer System")

    print("\t- 1 set Mackie Professional power Amplifiers")

    print("\t- 1 unit Mackie 1402vlz Professional Mixer (6 microphone input)")

    print("\t- 2 units Professional Wireless microphones with stand")

    print("\t- 2 units Professional wired microphones with boom stand")

    print("\t- 1 set Professional Sound processors")

    print("\t- 1 unit ACER Laptop")

    print("\t- 1 lot various wires and accessories")

    print("\t\t Total = 45,000 with a discount of 5%")



def package_2():

    print("Package 2")

    print("\t- 16 units LED 3x54 R.G.B.W. for party lighting / strobe light effects")

    print("\t- 4 units light stand w/ T-bar (4 holes each)")

    print("\t- 2pc DMX light controller")

    print("\t- 1pc Smoke Machine")

    print("\t- 2 lot various wires and cables")

    print("\t- 4 units BTS Light stand")

    print("\t- 6 units Moving head lights")

    print("\t- 2 units LED Dream Ball")

    print("\t- 2 units 2500/3500 ANSI Lumens LCD Projector")

    print("\t- 2 units 6ft by 6ft Projector screen")

    print("\t\t Total = 35,500 with a discount of 5%")



def package_3():

    print("Package 3")

    print("\t- 4 units JBL 12” Line array speakers")

    print("\t- 4 units JBL 12” Professional delay speakers")

    print("\t- 2 units Professional Subwoofer System")

    print("\t- 2 units Professional Subwoofer System")

    print("\t- 1 set Mackie Professional power Amplifiers")

    print("\t- 1 unit Mackie 1402vlz Professional Mixer (6 microphone input)")

    print("\t- 2 units Professional Wireless microphones with stand")

    print("\t- 2 units Professional wired microphones with boom stand")

    print("\t- 1 set Professional Sound processors")

    print("\t- 1 unit ACER Laptop")

    print("\t- 1 lot various wires and accessories")

    print("\t- 16 units LED 3x54 R.G.B.W. for party lighting / strobe light effects")

    print("\t- 4 units light stand w/ T-bar (4 holes each)")

    print("\t- 1pc DMX light controller")

    print("\t- 1pc Smoke Machine")

    print("\t- 1 lot various wires and cables")

    print("\t\t Total = 55,000 with a discount of 5%")



def additional_sound():

    print("For Additional Sound System:")

    print("\t1 - 18\" Professional Sub-woofer system - 1,000 pesos")

    print("\t2 - Full range Active speaker system - 1,000 pesos ")

    print("\t3 - Wireless Microphone System - 1,000 pesos")



def additional_light():

    print("For Additional Lighting System Upgrades:")

    print("\t4 - Beam 200 Sharpy Moving head intelligent lighting system - 1,000 pesos")

    print("\t5 - 575w/1200w Follow Spotlight - 1,000 pesos")

    print("\t6 - Par 64 Bulb lighting system (1000 w) - 1,000 pesos")

    print("\t7 -Par LED lights - 1,000 pesos")

    print("\t8 - Various Roboscan Disco lights - 1,000 pesos")



def addon_order(total_addon_price):

    global total_cost, total_package, total_addon_cost

    total_addon_price = 0

    total_addon_cost = 0


    for i in range(1, 51):

        print("~", end='')

    print("")


    while 1:

        ask_addons =(input("Would you like to choose addons?(y/n)"))  

        if ask_addons.upper() == 'Y':

            run = True

            break

        elif ask_addons.upper() == 'N':

            run = False

            break

        else:

            print("Inputted is not \"y\" or \"n\"")

            pass


    option1 = "18 Professional Sub-woofer system - 1,000 pesos"

    option2 = "Full range Active speaker system - 1,000 pesos "

    option3 = "Wireless Microphone System - 1,000 pesos"

    option4 = "Beam 200 Sharpy Moving head intelligent lighting system - 1,000 pesos"

    option5 = "575w/1200w Follow Spotlight - 1,000 pesos"

    option6 = "Par 64 Bulb lighting system (1000 w) - 1,000 pesos"

    option7 = "Par LED lights - 1,000 pesos"

    option8 = "Various Roboscan Disco lights - 1,000 pesos"


    for i in range(1, 51):

        print("~", end='')

    print("")


    while run:


        addon = int(input("Input Your Addons:"))


        if addon in range(1, 9):

            addon = addon

            if addon == 1:


                print("You have chosen", option1)

                total_addon_price += 1000

                print("Total Price of Addons: P", total_addon_price)

            elif addon == 2:

                print("You have chosen", option2)

                total_addon_price += 1000

                print("Total Price of Addons: P", total_addon_price)

            elif addon == 3:

                print("You have chosen", option3)

                total_addon_price += 1000

                print("Total Price of Addons: P", total_addon_price)

            elif addon == 4:

                print("You have chosen", option4)

                total_addon_price += 1000

                print("Total Price of Addons: P", total_addon_price)

            elif addon == 5:

                print("You have chosen", option5)

                total_addon_price += 1000

                print("Total Price of Addons: P", total_addon_price)

            elif addon == 6:

                print("You have chosen", option6)

                total_addon_price += 1000

                print("Total Price of Addons: P", total_addon_price)

            elif addon == 7:

                print("You have chosen", option7)

                total_addon_price += 1000

                print("Total Price of Addons: P", total_addon_price)

            elif addon == 8:

                print("You have chosen", option8)

                total_addon_price += 1000

                print("Total Price of Addons: P", total_addon_price)


            for i in range(1, 51):

                print("~", end='')

            print("")


            addon_choose_more = str(input("Would you like to choose more?(y/n)"))


            if addon_choose_more == 'y':

                pass

            elif addon_choose_more == 'n':

                run = False

            else:

                print("Inputted is not \"y\" or \"n\"")

        elif addon >= 9 or addon <= 0:

            print("Input a number in range 1 to 8")

            pass

    total_cost = total_package + total_addon_price

    total_addon_cost = total_addon_cost

    return total_addon_cost, total_addon_price



def platform():

    run = True

    for i in range(1, 51):

        print("~", end='')

    print("")

    print("Payment methods available are\n1 - Cash on Delivery\n2 - Online Payment")

    option1 = 'Cash on Delivery'

    option2 = 'Online Payment'

    option3 = 'Gcash'

    option4 = 'Paymaya'

    while run:

        payment_method = int(input("Payment Method: "))


        if payment_method > 2 or payment_method < 1:

            print('Inputted number is not on the available methods')

            payment_method = int(input("Payment Method: "))

            pass

        if payment_method == 1:

            for i in range(1, 51):

                print("~", end='')

            print("")

            print("You chose", option1)

            run = False

        elif payment_method == 2:

            for i in range(1, 51):

                print("~", end='')

            print("")

            print("You chose", option2)

            for i in range(1, 51):

                print("~", end='')

            print("")

            print("Platform of Online Payment: ")

            print("1 - Gcash\t2 - Paymaya")

            payment_platform = int(input("Online Payment Platform: "))

            for i in range(1, 51):

                print("~", end='')

            print("")

            while payment_platform > 2 or payment_method < 1:

                print('Inputted number is not on the available platforms')

                payment_platform = int(input("Payment Platform: "))

            if payment_platform == 1:


                print("You chose", option3)            

                run = False

            elif payment_platform == 2:

                print("You chose", option4)

                run = False



def end():

    print("\t\tTHANK YOU FOR CHOOSING THE PARTY GUYS!!!")

    print("\nFOR QUESTIONS OR INQUIRIES")

    print("Landline: 112 - 2334")

    print("Contact:: 09876543211")

    print("Address: 40, Matahimik Street, San Pedro, Laguna")

    print("Email:thepartyguys@matahimikstrt.com")

    print("Studio is open 7am - 8pm(Mon - Sat) & 7am - 5pm(Sun)")



package_1()

for i in range(1, 51):

    print("~", end='')

print("")

package_2()

for i in range(1, 51):

    print("~", end='')

print("")

package_3()

for i in range(1, 51):

    print("~", end='')

print("")



print("\t\t\t Welcome To the Party Guys!")

package = int(input("What Package would you want? Package(1/2/3): Package "))

while package != 1 and package != 3 and package != 2:

    print("You have not selected the following package(1/2/3). Please select.")

    package = int(input("What Package would you want? Package(1/2/3): Package "))

    break


if package == 1:

    package_cost = 45000

    package_discount = package_cost * discount

    total_package = package_cost - package_discount

    package_chosen = 'Package 1'

elif package == 2:

    package_cost = 35000

    package_discount = package_cost * discount

    total_package = package_cost - package_discount

    package_chosen = 'Package 2'

elif package == 3:

    package_cost = 55000

    package_discount = package_cost * discount

    total_package = package_cost - package_discount

    package_chosen = 'Package 3'

for i in range(1, 51):

    print("~", end='')

match package:

    case 1:

        print("\nYou Chose:")

        package_1()

    case 2:

        print("\nYou Chose:")

        package_2()

    case 3:

        print("\nYou Chose:")

        package_3()

    case _:

        pass

for i in range(1, 51):

    print("~", end='')

print("")


additional_sound()

additional_light()


total_addon_cost, total_addon_price = addon_order(total_addon_price)


for i in range(1, 51):

    print("~", end='')

print("")

#Personal Information

name = input("\nName: ")

address = input("Address: ")


contact_number = int(input("Contact Number: "))


date_time_event = input("Date and Time of Event: ")

for i in range(1, 51):

    print("~", end='')

print("")



platform()


for i in range(1, 51):

    print("~", end='')

print("")


#Confirmation of Transaction

print("Confirmation of Transactions")

print("You Chose:", package_chosen)

print("Your name is:", name)

print("Your Address is at:", address)

print("Your Contact Number is:", contact_number)

print("The Equipments are rented on:", date_time_event)

print(package_chosen, "costs:", format(package_cost, '.2f'))

print("Package Discount is 5%")

print(package_chosen, "discounted:", format(package_discount, '.2f'))

print(package_chosen, "with discount:", format(total_package, '.2f'))

print("Total addons cost: ", format(total_addon_price, '.2f'))

print("Total cost of Purchase: ", format(total_cost, '.2f'))


for i in range(1, 51):

    print("~", end='')

print("")



end()





