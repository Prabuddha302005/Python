# cols = 1
# string = "Lucky"
# for row in string:
#     for col in string:
#         if col<=string-cols:
#             print("", end="")
#         else:
#             print(chr(row), end=" ")
#     cols+=1
#     print()
    

# name = input("Enter the string ")
# i = 0
# while i <len(name):
#     j = 0
#     while j <= i:
#         print(name[i], end=" ")
#         j += 1
#     print()
#     i += 1

# col = 1
# while col <=5:
#     row = 1
#     while row <= col:
#         if row == 1 and col == 1:
#          print("A")
#     print()
#     row+=1

# row = 1
# while row <= 5:
#     col = 1
#     while col<=4:
#         if row == 1:
#             print("A", end=" ")
#         elif col==1 and row!=1:
#             print("B", end=" ")
#         col+=1
#     row+=1
#     print()

# for row in range(1, 6, 1):
#     for col in range(1,6,1):
#         if row == 1:
#             print("A", end=" ")
#         elif col == 1:
#             print("B", end="")
#         col+=1
#     row+=1
#     print()


a = "my name is khan"
i = 0
while i < len(a):
    print(a[-i], end="")
    i+=1
