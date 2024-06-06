# Tuples are used to store multiple items in a single variable.

# A tuple is a collection which is ordered and unchangeable.

tuple1 = ("apple", "mango", "banana", "cherry")
print(tuple1)
print(type(tuple1))
print(len(tuple1))

# One item tuple, remember the comma:
tuple2 = ("Lucky",)
print(tuple2)

# Update the tuple

tuple3 = ("Python", "Django ", "Fullstack", "web-developer")
y = list(tuple3)
y.append("MySQL")
tuple3 = tuple(y)
print(tuple3)

# unpacking the tuple

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# multiply the tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)