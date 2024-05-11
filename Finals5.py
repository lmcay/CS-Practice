def valid_password(password):
    valid = False
    
    if len(password) > 6:
        
        a,b,c,d,e = 0,0,0,1,0
        
        for char in password:
            
            if char >= "a" and char <= "z":
                a += 1
            if char >= "A" and char <= "Z":
                b += 1
            if char >= "0" and char <= "9":
                c += 1
            if char == " ":
                d = 0
            if char in special_characters:
                e += 1
        if a != 0 and b != 0 and c != 0 and d != 0 and e != 0:
            valid = True

        return valid

    else:
        return valid

special_characters = "!@#$%^&*()-+?_=,<>/"

while True:
    password = input("Create your password: ")
    check_validation = valid_password(password)

    if check_validation == True:
        break
    else:
        print("Password is not valid. Try agaiin.")

print("Password is valid.")



