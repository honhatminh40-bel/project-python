import random

restaurant = [
    "Cơm tắm: for student",
    "Bánh mì: traditional food",
    "Phở: classical",
    "Gà rán KFC: fast food"

]
while True:
    a = input("Do you want some vietnamese food? (0: no/1: yes): ").strip()
    remaining_restaurant = restaurant.copy()
    if a == "0":
        print("Nah come on😭")
        break
    elif a == "1":
        print("Nice dude😘\nLet me recommend for you!!!")
        while remaining_restaurant:
            suggested_dish = random.choice(remaining_restaurant)
            print("Your order is: " + suggested_dish)
            remaining_restaurant.remove(suggested_dish)
            if remaining_restaurant:
                change = input("Wanna change?? (0: no/ 1: yes): ")
                if change != "1":
                    print("Have a nice day")
                    break
            else:
                print("We're out of food!\nSee you then=))")
        break
    else:
        print("Wrong type lmao, only accept 0 & 1.")
        