"""
num = 5
fact = 1
i = 1
while i<=num:
    fact = fact * i
    i+=1

print(fact)
"""    
#Armstrong number

n = 12122
p = len(str(n))
n1 = n
arm=0
"""
while n!=0:
    arm = arm+(n%10)**p
    n=n//10
if n1 == arm:
    print(n1, "Is an Armstrong Number")
else:
    print(n1, "Is not an Armstrong Number")
"""
n = 12122
p = len(str(n))
n1 = n 
arm=0

for i in range(0,p,1):
    arm = arm+(n%10)**p
    n=n//10
if n1 == arm:
    print(n1, "Is an Armstrong Number")
else:
    print(n1, "Is not an Armstrong Number")
