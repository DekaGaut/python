"""
Like sets dictionaries cannot have duplicate keys.
Existing values could be changed 
"""
#1

friends = {"Rolf": 25, "Daniel": 26, "Ram": 27}
print(friends["Rolf"])
friends["Bob"] = 25
friends["Bob"] = 26
print(friends)

#2
friends_info =(
{"name": "Rolf", "age": 25},
{"name": "Bob", "age": 26},
{"name": "Charlie", "age": 27}
    )

print(friends_info[0]["name"])
print(friends_info[1]["age"])

#3 Turning a list into a dictionary using dict
animals = [("Tiger", "Bengal"), ("Rhino", "Assam")]
animals = dict(animals)
print(animals)

#4 Length and sum
x = [10,20,30,40,50]
total = sum(x)
length = len(x)
average = total/length
print(average)

#5 Join
friends = ["Avinash", "Anupam", "Abhishek", "Gautam", "Himanshu"]
comma_separated = ", ".join(friends)
print(f"My friends are {comma_separated}.")

print(comma_separated)
