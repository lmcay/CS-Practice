

itemz = {"chairs" : 0,
         "tables" : 0,
         "silverware" : 0}


##data = input("Input Item: ")

##if data == "chairs":
##    num = int(input("How many items: "))
##    itemz["chairs"] = nums



##for x in itemz:
##    print(x,"=",itemz[x])


while True:
    data = input("Input Item: ")
    for x in itemz:
        if data == x:
            num = int(input("How many items: "))
            itemz[x] = num
            price = num*0.5
            break


    for x in itemz:
        if itemz[x] == 0:
            continue
        else:
            print(x,"=",itemz[x], price)
