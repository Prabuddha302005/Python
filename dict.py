# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

dict1 = {
    "Name": "Lucky",
    "_id": 7,
    "roll": "Full-Stack freelancer"
    }
print(dict1)
print(type(dict1))
print(len(dict1))
dict1["salary"] = "$2k"
print(dict1.get("_id"))
print(dict1.keys())
print(dict1.values())
print(dict1)
print(dict1.items())
dict1.update({"salary": "$4k"})
print(dict1)

# looping through the dictionaires

for x in dict1:
    print(x)

for x in dict1:
    print(dict1[x])

# Loop through both keys and values, by using the items() method:
print("Looping")
for x, y in dict1.items():
  print(x, y)

# Make a copy of a dictionary with the copy() method:
dict2 = dict1.copy() #Same can be done with dict() method
print(dict2)

# A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])