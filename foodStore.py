# while True:
#     data = input("Hello sir what you will like to eat veg/non veg  ")
#     if data == 'veg':
#       food = input("Pav bhaji, Pulav ")
#       if food == "pav bhaji":
#         print("Here's your pav-bhaji half : 100rs / full : 150rs")
#       elif food == "pulav":
#         print("Pulav half : 100rs / full : 150rs ")
#     elif data == 'non veg':
#      food = input("Biryani, Butter chicken ")
#      if food == 'biryani':
#       print("Here's your biryani half : 100rs / full : 150rs")
#      if food == 'butter chicken':
#       print("Here's your biryani half : 100rs / full : 150rs")
#     more = input("Would uou like to anything else sir ")
#     if more == 'no':
#       print("Thank you !")
#       break


while True:
    data = input("Hello sir what would you like to eat, (veg/non veg)? ")
    if data == 'veg':
        food = input("Pav bhaji, Pulav: ")
        if food == "pav bhaji":
            print("Here's your pav-bhaji. Price: Half - 100rs, Full - 150rs")
        elif food == "pulav":
            print("Here's your Pulav. Price: Half - 100rs, Full - 150rs ")
        qty = input("Half or full ")
        if qty == 'half':
            print("Here's half", food)
        elif qty == 'full':
                print("Here's full", food)
    elif data == 'non veg':
        food = input("Biryani, Butter chicken: ")
        if food == 'biryani':
            print("Here's your biryani. Price: Half - 100rs, Full - 150rs")
        elif food == 'butter chicken':
            print("Here's your butter chicken. Price: Half - 100rs, Full - 150rs")
        qty = input("Half or full ")
        if qty == 'half':
            print("Here's half", food)
        elif qty == 'full':
                print("Here's full", food)
    more = input("Would you like anything else, sir? (yes/no) ")
    if more == 'no':
        print("Thank you! Enjoy your food")
        break

    
