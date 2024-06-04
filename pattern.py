'''
row = 1
while row <= 5:
    col = 1
    while col<=4:
        if col == 1 or col==4 or row==3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        col+=1
    print()
    row+=1

'''
'''
row = 1
while row <=5:
    col = 1
    while col<=5:
        if row==1 or row==5 or col==3 or col==3 or col==1 or col==5:
             print("*", end=" ")
        else:
            print(" ", end=" ")
        col+=1
    print()
    row+=1
''' 
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1
    
