##def validation_order():
##    while True:
##        ask_if_order = input("Do you want to order? [1. Yes | 0. No, take me back to homepage]")
##        if ask_if_order == "1" or ask_if_order == "0":
##            return ask_if_order
##            break
##        else:
##            print("Invalid Input")
##
##print("Service 1\nService 2\nService 3")
##
##while True:
##    validation_order()
##    ask_if_order = validation_order()
##
##    if ask_if_order == 1:
##        print("order")
##    else:
##        break

fruit = ["apple", "banana", "grapes"]
vegetable = ["lettuce", "carrot", "squash"]

apple = 0
banana = 0
grapes = 0
print(vegetable)

while True:
    data = int(input("Input data: "))

    if data == 1 or data == 2 or data == 3:
        
        for i in fruit:
            data = i
            if i == "apple":
                apple += 1
            elif i == "banana":
                banana += 1
            elif i == "grapes":
                grapes += 1
    elif data == 0:
        break
    
print("apple is", apple)
print("banana is", banana)
print("grapes is", grapes)
    
            






















                
