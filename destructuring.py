#1

friends = [("Rolf", 25), ("Bob",35), ("Charlie",45), ("Denny",55)]

for name,age in friends:
    print(f"{name} is {age} years old.")

# Iterating over dictionaries

friend_ages = {"Rolf": 25, "Bob": 24, "Charlie": 32, "Denny": 34}

for friend in friend_ages:
    print(friend)

for age in friend_ages.values():
    print(age)

for name, age in friend_ages.items():
    print(f"{name} is {age} years old.")
