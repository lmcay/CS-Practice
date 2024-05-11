##apple_cost = 5.16
##
##fruits = ["Tents", "Tables", "a", "orange", "banana"]
##
##c_apple = fruits.count("apple")
##
##if c_apple > 0:
##    apple = c_apple * apple_cost
##else:
##    apple = 0
##fruits = list(dict.fromkeys(fruits))
##print(c_apple, apple, fruits)



items = ["[1]Tents","[2]Tables","[3]Chairs","[4]Table Cloth Linen","[5]Ribbons", "[6]Complete Utensils and Silverware (Spoon and Fork Set, Teaspoon, Serving Spoon, Glass, Plates and more...)"]
cart = []
for x in items:
    print(x)

while True:
    data = input("Input: ")
    if data not in items:
        print("Not in Items")
    else:
        cart.append(data)
