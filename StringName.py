'''
name = "Prabuddha"

for myValue in name:
    print(myValue, end="")
'''

'''
name = input("Enter your name ")
age = input("Enter your age ")
city = input("Enter your city ")
print("Your name is",name, "your age is", age, "your city is", city)
'''

while True:
    name = input("Enter your name ")
    age = input("Enter your age ")
    city = input("Enter your city ")

    myInput = name, age, city
    
    if myInput:
        print(f"Your name is {name}, your age is {age},your city is {city}")
        ask = input("Do you want to proceed further ")
        if ask == 'no':
            print("Bye")
            break

        
    
