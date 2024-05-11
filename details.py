



def final_confirmation():
    while True:
        confirmation = input("Have you confirmed your details? [1] Yes [2] Reset my details]")
        match confirmation:
            case "1"|"2":
                return int(confirmation)
                break
            case _:
                print("Invalid Option")

def order_again():
    while True:
        order_again = input("Do you want to create another order? [1]Yes\n[2]No")
        match order_again:
            case "1"|"2":
                return int(order_again)
            case _:
                print("Invalid Option")

while True:
    print("Place your details and make sure it is valid")
    name = input("Full Name: ")
    number = input("Contact Number: ")
    address = input("Venue Address: ")
    date_order = input("Input date of order (Ex. January 3,2022): ")
    date_req = input("Input date of order deadline (Ex. January 13, 2022): ")
    guest_count = input("Guest Count: ")
    payment = input("Mode of Payment [GCASH/Paymaya]")
    print("FUll Name:",name,"\nContact Number:", number,"\nVenue Address:",address,"\nDate of order:",date_order,"\nDate of order deadline:",date_req,"\nGuest Count:",guest_count,"\nMode of Payment:",payment)
    print("Make sure to print out all details accurately as our management will check the data and agreement created.")
    confirmation = final_confirmation()
    if confirmation == 1:
        print("Thank you", name)
        print("Bill:", total)
        break
    else:
        continue

order_again = order_again()
if order_again == 1:
    continue
else:
    break
          
