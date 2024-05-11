oxford_shoes = "Oxford Shoes"
kitten_heels = "Kitten Heels"
sneakers = "Sneakers"
sandals = "Sandals"
ankle_boots = "Ankle Boots"
slippers = "Slippers"
shoes_price = (990,999,755,499,840,310)
shoes = (oxford_shoes, kitten_heels, sneakers, sandals, ankle_boots, slippers)
necklaces = "Necklace"
bracelet = "Bracelet"
ring = "Ring"
earrings = "Earrings"
perfume = "Perfume"
wristwatch = "Wristwatch"
vanity_price = (2999,1499,4999,3999,5999,3960)
vanity = (necklaces, bracelet, ring, earrings, perfume)
puffer_jacket = "Puffer Jacket"
windbreaker_jacket = "Windbreaker Jacket"
leather_jacket = "Leather Jacket"
coach_jacket = "Coach Jacket"
trench_coat = "Trench Coat"
raincoat = "Raincoat"
jacket_coat_price = (1499,2399,3999,1499,999,899)
jacket_coat = (puffer_jacket,windbreaker_jacket,leather_jacket,coach_jacket,trench_coat,raincoat)
slim_fit = "Slim fit"
bell_bottoms = "Bell bottoms"
jogging = "Jogging"
leggings = "Leggings"
slacks = "Slacks"
jeans = "Jeans"
pants_price = (180,205,195,180,170,180)
pants = (slim_fit,bell_bottoms,jogging,leggings,slacks,jeans)
crew_neck = "Crew neck"
blouse = "Blouse"
polo = "Polo"
turtle_neck = "Turtle neck"
v_neck = "V-neck"
off_shoulder = "Off shoulder"
shirt_price = (175,180,200,200,190,220)
shirt = (crew_neck,polo,v_neck,blouse,turtle_neck,off_shoulder)
shopping_list = []
price = []
def mainMenu():
    print("------==========WELCOME TO OUR CLOTHING STORE!==========------","\n\t\t\t[1]Shirts","\n\t\t\t[2]Pants","\n\t\t\t[3]Coat and jacket","\n\t\t\t[4]Vanity","\n\t\t\t[5]Shoes","\n[0]Exit the Program","   [6]CHECK OUT!","\t[7]View and Remove item from cart")
    option = (input("Enter your option: "))
    if option == "1":
        shirt()
    elif option == "2":
        pants()
    elif option == "3":
        caj()
    elif option == "4":
        vanity()
    elif option == "5":
        shoes()
    elif option == "6":
        total()
    elif option == "7":
        vnr()
    elif option == "0":
        again = (input("Are you sure you want to EXIT? (y or n): ")).lower()
        if again == "n":
           mainMenu()
        elif again == "y":
            print("Thanks for using this program. Have a nice day.")
            exit
    else:
        print("Invalid option.")
        mainMenu()
def shirt():
    print("\t\t\tSHIRT","\n\t\t\t[0]Crew Neck - P175","\n\t\t\t[1]Polo - P200","\n\t\t\t[2]V-Neck - P190","\n\t\t\t[3]Blouse - P180","\n\t\t\t[4]Turtle Neck - P200","\n\t\t\t[5]Off-Shoulder - P220")
    shirt = (crew_neck ,polo,v_neck ,blouse ,turtle_neck ,off_shoulder)
    shirt_price = (175,180,200,200,190,220)
    item = True
    while item:
        all_shirt =(input("What Shirt do you want?: "))
        while all_shirt != "0" and all_shirt != "1" and all_shirt != "2" and all_shirt != "3" and all_shirt != "4" and all_shirt != "5":
            print("Invalid option.")
            all_shirt =(input("What Shirt do you want?: "))
        if all_shirt == "0":
            shopping_list.append(shirt[0])
            price.append(shirt_price[0])
        elif all_shirt == "1":
            shopping_list.append(shirt[1])
            price.append(shirt_price[1])
        elif all_shirt == "2":
            shopping_list.append(shirt[2])
            price.append(shirt_price[2])
        elif all_shirt == "3":
            shopping_list.append(shirt[3])
            price.append(shirt_price[3])
        elif all_shirt == "4":
            shopping_list.append(shirt[4])
            price.append(shirt_price[4])
        elif all_shirt == "5":
            shopping_list.append(shirt[5])
            price.append(shirt_price[5])
        add_more = (input("Do you want to add more? (y or any key)")).lower()
        if add_more != 'y':
            item = False
    print("\t\tYour current items are:")
    for item in shopping_list:
        print("\t\t\t",f'{item:}')
    print("\t\t__________________________")
    for item in price:
        print("\t\t\t","P",f'{item:,}')
    anykey = input("press Enter to go back")
    mainMenu()
def pants():
    print("\t\t\tPANTS","\n\t\t\t[0]Slim Fit - P180","\n\t\t\t[1]Bell Bottoms - P205","\n\t\t\t[2]Jogging - P195","\n\t\t\t[3]Leggings - P180","\n\t\t\t[4]Slacks - P170","\n\t\t\t[5]Jeans - P180")
    pants = (slim_fit,bell_bottoms,jogging,leggings,slacks,jeans)
    pants_price = (180,205,195,180,170,180)
    item = True
    while item:
        all_pants =(input("What Pants do you want?: "))
        while all_pants != "0" and all_pants != "1" and all_pants != "2" and all_pants != "3" and all_pants != "4" and all_pants != "5":
            print("Invalid option.")
            all_pants =(input("What Pants do you want?: "))
        if all_pants == "0":
            shopping_list.append(pants[0])
            price.append(pants_price[0])
        elif all_pants == "1":
            shopping_list.append(pants[1])
            price.append(pants_price[1])
        elif all_pants == "2":
            shopping_list.append(pants[2])
            price.append(pants_price[2])
        elif all_pants == "3":
            shopping_list.append(pants[3])
            price.append(pants_price[3])
        elif all_pants == "4":
            shopping_list.append(pants[4])
            price.append(pants_price[4])
        elif all_pants == "5":
            shopping_list.append(pants[5])
            price.append(pants_price[5])
        add_more = (input("Do you want to add more? (y or n)")).lower()
        if add_more != 'y':
            item = False
    print("Your current items are:")
    for item in shopping_list:
        print("\t\t\t",f'{item:}')
    print("\t\t__________________________")
    for item in price:
        print("\t\t\t","P",f'{item:,}')
    anykey = input("press Enter to go back")
    mainMenu()
def caj():
    print("\t\t\tCOAT AND JACKET","\n\t\t\t[0]Puffer Jacket - P1,499","\n\t\t\t[1]WindBreaker Jacket - P2,399","\n\t\t\t[2]Leather Jacket - P3,999","\n\t\t\t[3]Coach Jacket - P1,499","\n\t\t\t[4]Trench Coat - P999","\n\t\t\t[5]Raincoat - P899")
    jacket_coat = (puffer_jacket,windbreaker_jacket,leather_jacket,coach_jacket,trench_coat,raincoat)
    jacket_coat_price = (1499,2399,3999,1499,999,899)
    item = True
    while item:
        all_caj =(input("What Coats and Jackets do you want?: "))
        while all_caj != "0" and all_caj != "1" and all_caj != "2" and all_caj != "3" and all_caj != "4" and all_caj != "5":
            print("Invalid option.")
            all_caj =(input("What Coats and Jackets do you want?: "))
        if all_caj == "0":
            shopping_list.append(jacket_coat[0])
            price.append(jacket_coat_price[0])
        if all_caj == "1":
            shopping_list.append(jacket_coat[1])
            price.append(jacket_coat_price[1])
        if all_caj == "2":
            shopping_list.append(jacket_coat[2])
            price.append(jacket_coat_price[2])
        if all_caj == "3":
            shopping_list.append(jacket_coat[3])
            price.append(jacket_coat_price[3])
        if all_caj == "4":
            shopping_list.append(jacket_coat[4])
            price.append(jacket_coat_price[4])
        if all_caj == "5":
            shopping_list.append(jacket_coat[5])
            price.append(jacket_coat_price[5])
        add_more = (input("Do you want to add more? (y or any key))")).lower()
        if add_more != 'y':
            item = False
    print("Your current items are:")
    for item in shopping_list:
        print("\t\t\t",f'{item:}')
    print("\t\t__________________________")
    for item in price:
        print("\t\t\t","P",f'{item:,}')
    anykey = input("press Enter to go back")
    mainMenu()
def vanity():
    print("\t\t\tVANITY","\n\t\t\t[0]Necklaces - P2,999","\n\t\t\t[1]Bracelet - P1,499","\n\t\t\t[2]Ring - P4,999","\n\t\t\t[3]Earrings - P3,999","\n\t\t\t[4]Perfume - P5,999","\n\t\t\t[5]wristwatch - P3,960")
    vanity = (necklaces, bracelet, ring, earrings, perfume,wristwatch)
    vanity_price = (2999,1499,4999,3999,5999,3960)
    item = True
    while item:
        all_vanity =(input("What Vanity do you want?: "))
        while all_vanity != "0" and all_vanity != "1" and all_vanity != "2" and all_vanity != "3" and all_vanity != "4" and all_vanity != "5":
            print("Invalid option.")
            all_vanity =(input("What Vanity do you want?: "))
        if all_vanity == "0":
            shopping_list.append(vanity[0])
            price.append(vanity_price[0])
        if all_vanity == "1":
            shopping_list.append(vanity[1])
            price.append(vanity_price[1])
        if all_vanity == "2":
            shopping_list.append(vanity[2])
            price.append(vanity_price[2])
        if all_vanity == "3":
            shopping_list.append(vanity[3])
            price.append(vanity_price[3])
        if all_vanity == "4":
            shopping_list.append(vanity[4])
            price.append(vanity_price[4])
        if all_vanity == "5":
            shopping_list.append(vanity[5])
            price.append(vanity_price[5])
        add_more = (input("Do you want to add more? (y or any key)")).lower()
        if add_more != 'y':
            item = False
    print("Your current items are:")
    for item in shopping_list:
        print("\t\t\t",f'{item:}')
    print("\t\t__________________________")
    for item in price:
        print("\t\t\t","P",f'{item:,}')
    anykey = input("press Enter to go back")
    mainMenu()
def shoes():
    print("\t\t\tSHOES","\n\t\t\t[0]Oxford shoes – P990","\n\t\t\t[1]Kitten heels – P999","\n\t\t\t[2]Sneakers – P755","\n\t\t\t[3]Sandals – P499","\n\t\t\t[4]Ankle boots – P840","\n\t\t\t[5]Slippers – P310")
    shoes = (oxford_shoes, kitten_heels, sneakers, sandals, ankle_boots, slippers)
    shoes_price = (990,999,755,499,840,310)
    item = True
    while item:
        all_shoes =(input("What Shoes do you want?: "))
        while all_shoes != "0" and all_shoes != "1" and all_shoes != "2" and all_shoes!= "3" and all_shoes!= "4" and all_shoes != "5":
            print("Invalid option.")
            all_ =(input("What Shoes do you want?: "))
        if all_shoes == "0":
            shopping_list.append(shoes[0])
            price.append(shoes_price[0])
        if all_shoes == "1":
            shopping_list.append(shoes[1])
            price.append(shoes_price[1])
        if all_shoes == "2":
            shopping_list.append(shoes[2])
            price.append(shoes_price[2])
        if all_shoes == "3":
            shopping_list.append(shoes[3])
            price.append(shoes_price[3])
        if all_shoes == "4":
            shopping_list.append(shoes[4])
            price.append(shoes_price[4])
        if all_shoes == "5":
            shopping_list.append(shoes[5])
            price.append(shoes_price[5])
        add_more = (input("Do you want to add more? (y or any key))")).lower()
        if add_more != 'y':
            item = False
    print("Your current items are:")
    for item in shopping_list:
        print("\t\t\t",f'{item:}')
    print("\t\t__________________________")
    for item in price:
        print("\t\t\t","P",f'{item:,}')
    anykey = input("press Enter to go back")
    mainMenu()
def vnr():
    print("\t\tThis is your current items")
    print("   (0 = 1st position, 1 = 2nd position, 2 = 3rd position,etc.)")
    for item in shopping_list:
        print("\t\t\t",f'{item:}')
    print("\t\t__________________________")
    for item in price:
        print("\t\t\t","P",f'{item:,}')
    remove = (input("What item would you like to remove?(press n to go back):"))
    remove_thing = True
    while remove_thing:
        if remove == 'n':
            anykey = input("press Enter to go back")
            mainMenu()
            remove_thing = False
        elif remove >= 'a' and remove <= 'z':
            print("Invalid option")
            vnr()
        else:
            shopping_list.pop(int(remove))
            price.pop(int(remove))
            vnr()
            remove_thing = False

def total():
    total = sum(price)
    print("The your total is: ",f'{total:,}')
    print("Thank you for shopping with us.")
    exit
    
print("")
mainMenu()
