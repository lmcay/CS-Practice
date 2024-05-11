def validation(check_num):
    if check_num == "1" or check_num== "2":
        return check_num
    else:
        print("Not Valid")

data = 0
while data != "1" or data != "2":
    data = input("Input Data: ")
    data = validation(data)
    if data == "1":
        print("ok this is one")
        break
    elif data == "2":
        print("ok this is two")
        break
