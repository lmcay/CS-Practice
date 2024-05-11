
def WEDDING_PACKAGES():
    
    wedding_pack = [["WEDDING PACKAGE","Set-up and Props Inclusion","Wedding Package"],
                ["1 Rice Menu","Buffet Set-up",""],
                ["1 Fish Menu","Formal Uniform for Caterers","Package [1] - P 24,000"],
                ["1 Chicken Menu","Complete Wedding Equipments","Good for 30 People"],
                ["1 Beef Menu","Entrance Arch , Red Carpet, etc.",""],
                ["1 Vegetable Menu","Invitation Cards & A Special Gift","Package [2] - P38,000"],
                ["1 Dessert Menu","Complete Equipment for ","Good for 50 People"],
                ["1 Soup Menu","Catering (Utensils)",""],
                ["Round Bottomless Softdrinks","Complete Catering Equipments","Package [3] - P75,000"],
                ["Purified Water With Tube Ice","Wedding Party Host and Co-Host","Good for 100 People"]]

    print("O"+"="*102+"O")
    for package in wedding_pack:
        print("|", package[0], " "*(29-len(package[0])), "|", package[1], " "*(33-len(package[1])), "|", package[2], " "*(29-len(package[2])), "|")
    print("O"+"="*102+"O")

def BIRTHDAY_PACKAGES():
    birthday_normal = [["BIRTHDAY PACKAGE","Set-up and Props Inclusion","Birthday Packages"],
                   ["Plain Rice","Buffet Set-up",""],
                   ["Garlic Rice","Formal Uniform for Caterers","Good for N People"],
                   ["1 Beef Menu","Presentable Backdrop with",""],
                   ["1 Chicken Menu","Color Motive","Package [1] - P 18,000"],
                   ["1 Fish Menu","Complete Equipment for","30 People"],
                   ["1 Vegetable Menu","Catering (Utensils)",""],
                   ["1 Appetizer Dish","Complete Tables and Chairs","Package [2] - P 28,000"],
                   ["1 Dessert","with Presentable Center Piece","50 People"],
                   ["1 Soup","and Color Motive",""],
                   ["Purified Water W/Tube Ice","Presentable Cake Table/Stand","Package [3] - P 55,000"],
                   ["Bottomless Softdrinks","Set-up and Photobooth","100 People"]]

    birthday_kiddie = [["BIRTHDAY PACKAGE - KIDDIE","Set-up and Props Inclusion","Birthday Packages - Kiddie"],
                   ["Plain Rice","Loot Bags and Accent Lights",""],
                   ["1 Beef Menu","Buffet Set-up","Package [4] - P 13,000"],
                   ["1 Vegetable Menu","Formal Uniform for Caterers","Good for 30 People"],
                   ["Spaghetti","Party Props (Hats, Lights, etc.)",""],
                   ["Hotdog","Complete Equipment for","Package [5] - P 21,000"],
                   ["Cotton Candy Station","Catering (Utensils)","Good for 50 People"],
                   ["Kiddie Cake","Complete Tables and Chairs ",""],
                   ["1 Round Bottomless Softdrinks","with Presentable Center Piece ","Package [6] - P 38,000"],
                   ["Purified Water With Tube Ice","and Color Motive","Good for 100 People"]]

    print("O"+"="*102+"O")
    for package in birthday_normal:
        print("|", package[0], " "*(29-len(package[0])), "|", package[1], " "*(33-len(package[1])), "|", package[2], " "*(29-len(package[2])), "|")
    print("O"+"="*102+"O")
    for package in birthday_kiddie:
        print("|", package[0], " "*(29-len(package[0])), "|", package[1], " "*(33-len(package[1])), "|", package[2], " "*(29-len(package[2])), "|")
    print("O"+"="*102+"O")

BIRTHDAY_PACKAGES()
