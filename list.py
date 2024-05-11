

##birthday_package = [["Lychee","Lettuce", "Bird"],
##                    ["Apple", "Onion", "Cat"],
##                    ["Grapes", "Lettuce", "Cow"],
##                    ["Oranges", "Garlic", "Sheep"],
##                    ["Banana", "ALONGNAMEEEEE", "Elephant"],
##                    ["Cherry", "Spinach", "Goat"]]
##
##print("\t| Fruits   | Vegetables     | Animals   |")
##
##for data in birthday_package:
##    print("\t|", data[0], " "*(7-len(data[0])),"|", data[1], " "*(13-len(data[1])), "|", data[2], " "*(8-len(data[2])), "|")

##my_cart = []
##one, two, three, four = 0,0,0,0
##data_num = [1,2,3,4,0]
##while True:
##    data = int(input(""))
##    if data >= 1 and data <= 9:
##        my_cart.append(data)
##    elif data == 0:
##        break
##    else:
##        print("Not within the choices")
##
##for data in my_cart:
##    if data == 1:
##        one += 1
##    elif data == 2:
##        two += 1
##    elif data == 3:
##        three += 1
##    elif data == 4:
##        four += 1
##
## 
##if one != 0:
##    print("You've inputted 1", one, "time")
##if two != 0:
##    print("You've inputted 2", two, "time")
##if three != 0:
##    print("You've inputted 3", three, "time")
##if four != 0:
##    print("You've inputted 4", four, "time")

##print("You've inputted 1", one, "time")
##print("You've inputted 2", two, "time")
##print("You've inputted 3", three, "time")
##print("You've inputted 4", four, "time")
##print(my_cart)








##pack = "(Good for 20 People)"
##iced_tea = "Iced Tea Bottomless"
##water = "Ice Mineral Water"
##
##party_food = [["         PACKAGE CODE [1]", "         PACKAGE CODE [2]", "         PACKAGE CODE [3]"],
##              ["Package 1: Occasional Package", "Package 2: Party Package Overload", "Package 3: Formal Package"],
##              [pack, pack, pack],
##              ["Mixed Veggies and Seafood", "Fried Garlic Rice", "Roast Beef"],
##              ["Spaghetti & Meatballs", "Hotdogs", "Fried garlic and butter rice"],
##              ["Plain Rice", "Crispy Chicken Tacos", "Chicken Cordon Bleu"],
##              ["Garlic Chicken", "Pizza Hawaiian", "Roast Pork with Oyster Sauce"],
##              ["Roast Beef", "Chicken Wings", "Pescada en Salsa Verde"],
##              ["Pork and Chicken BBQ", "BBQ Pork Sliders", "Baked Spaghetti "],
##              ["Fish Fillet", "Spaghetti & Meatballs", "Mixed Vegetables with Ham "],
##              ["Pork Lumpia", "Sandwiches Roasted Beef", "Buko Fruit Salad  "],
##              [iced_tea, iced_tea, iced_tea],
##              [water, water, water],
##              ["Price: 10,261 PHP", "Price: 11,707 PHP", "Price: 12,404PHP"]]
##
##for package in party_food:
##    print("\t|", package[0], " "*(29-len(package[0])), "|", package[1], " "*(33-len(package[1])), "|", package[2], " "*(29-len(package[2])), "|")

##print()
####while True:
####    data = int(input("What package would you like to order? "))
##
##data = 1
##data2 = 1
##data3 = 3
##for package in party_food:
##    if data == 1:
##        print("|", package[0], " "*(29-len(package[0])), "|", end=" ")
##    if data2 == 1:
##        print("|", package[1], " "*(33-len(package[1])), "|")
##    if data3 == 3:
##        print("|", package[2], " "*(29-len(package[2])), "|", end=" ")
##            
    



##birthday_normal = [["BIRTHDAY PACKAGE","Set-up and Props Inclusion","Birthday Packages"],
##                   ["Plain Rice","Buffet Set-up",""],
##                   ["Garlic Rice","Formal Uniform for Caterers","Good for N People"],
##                   ["1 Beef Menu","Presentable Backdrop with",""],
##                   ["1 Chicken Menu","Color Motive","Package [1] - P 18,000"],
##                   ["1 Fish Menu","Complete Equipment for","30 People"],
##                   ["1 Vegetable Menu","Catering (Utensils)",""],
##                   ["1 Appetizer Dish","Complete Tables and Chairs","Package [2] - P 28,000"],
##                   ["1 Desert","with Presentable Center Piece","50 People"],
##                   ["1 Soup","and Color Motive",""],
##                   ["Purified Water W/Tube Ice","Presentable Cake Table/Stand","Package [3] - P 55,000"],
##                   ["Bottomless Softdrinks","Set-up and Photobooth","100 People"]]

##for bday1 in birthday_normal:
##        print("|", bday1[0], " "*(29-len(bday1[0])), "|", bday1[1], " "*(33-len(bday1[1])), "|", bday1[2], " "*(29-len(bday1[2])), "|")
##
##print("="*102)
##birthday_kiddie = [["BIRTHDAY PACKAGE - KIDDIE","Set-up and Props Inclusion","Birthday Packages - Kiddie"],
##                   ["Plain Rice","Loot Bags and Accent Lights",""],
##                   ["1 Beef Menu","Buffet Set-up","Package [4] - P 13,000"],
##                   ["1 Vegetable Menu","Formal Uniform for Caterers","Good for 30 People"],
##                   ["Spaghetti","Party Props (Hats, Lights, etc.)",""],
##                   ["Hotdog","Complete Equipment for","Package [5] - P21,000"],
##                   ["Cotton Candy Station","Catering (Utensils)","Good for 50 People"],
##                   ["Kiddie Cake","Complete Tables and Chairs ",""],
##                   ["1 Round Bottomless Softdrinks","with Presentable Center Piece ","Package [6] - P40,000"],
##                   ["Purified Water With Tube Ice","and Color Motive","Good for 100 People"]]
##
##for bday2 in birthday_kiddie:
##        print("|", bday2[0], " "*(29-len(bday2[0])), "|", bday2[1], " "*(33-len(bday2[1])), "|", bday2[2], " "*(29-len(bday2[2])), "|")

##wedding_pack = [["WEDDING PACKAGE","Set-up and Props Inclusion","Wedding Package"],
##                ["1 Rice Menu","Buffet Set-up",""],
##                ["1 Fish Menu","Formal Uniform for Caterers","Package A - P 24,000"],
##                ["1 Chicken Menu","Complete Wedding Equipments","Good for 30 People"],
##                ["1 Beef Menu","Entrance Arch , Red Carpet, etc.",""],
##                ["1 Vegetable Menu","Invitation Cards & A Special Gift","Package B - P38,000"],
##                ["1 Dessert Menu","Complete Equipment for ","Good for 50 People"],
##                ["1 Soup Menu","Catering (Utensils)",""],
##                ["Round Bottomless Softdrinks","Complete Catering Equipments","Package C - P75,000"],
##                ["Purified Water With Tube Ice","Wedding Party Host and Co-Host","Good for 100 People"]]
##
##for package in wedding_pack:
##        print("|", package[0], " "*(29-len(package[0])), "|", package[1], " "*(33-len(package[1])), "|", package[2], " "*(29-len(package[2])), "|")



birthday_normal = [["BIRTHDAY PACKAGE","Set-up and Props Inclusion","Birthday Packages"],
                   ["Plain Rice","Buffet Set-up",""],
                   ["Garlic Rice","Formal Uniform for Caterers","Good for N People"],
                   ["1 Beef Menu","Presentable Backdrop with",""],
                   ["1 Chicken Menu","Color Motive","Package [1] - P 18,000"],
                   ["1 Fish Menu","Complete Equipment for","30 People"],
                   ["1 Vegetable Menu","Catering (Utensils)",""],
                   ["1 Appetizer Dish","Complete Tables and Chairs","Package [2] - P 28,000"],
                   ["1 Desert","with Presentable Center Piece","50 People"],
                   ["1 Soup","and Color Motive",""],
                   ["Purified Water W/Tube Ice","Presentable Cake Table/Stand","Package [3] - P 55,000"],
                   ["Bottomless Softdrinks","Set-up and Photobooth","100 People"]]

for i in birthday_normal:
        print(i[0], " "*(29-len(i[0])), i[1], " "*(33-len(i[1])), i[2])

##
##data = [[1,2,3],
##        [4,5,6]]
##
##for i in data:
##        print(i[1])















