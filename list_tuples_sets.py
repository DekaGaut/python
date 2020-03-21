"""
DATA STRUCTURES

1.Sets are denoted by []
"""

friends = ["Rolf","Bob","Charlie","Dick"]

print(friends[0])
print(len(friends))

friends_set = [["Rolf",25],["Bob",24],["Charlie",23],["Dick",22]]
print(friends_set[0][0])

friends = ["Himanshu","Anupam","Avinash","Abhishek","Gautam"]
friends.append("Victor")
friends.remove("Victor")

"""
2.Tuples are denoted by ()
"""


"""
3. Sets are denoted by {}
Sets don't hold order.
Sets don't contain duplicate elements.
"""

art_friends = {"Rolf", "Anne"}
science_friends = {"Jen","Charlie"}

art_friends.add("Jen")
art_friends.add("Jen") # Duplicate values won't get added to the sets
art_friends.remove("Jen")

"""
Advanced set operations
"""

art_friends = {"gautam","himanshu","anupam","avinash","abhishek","ashish"}
science_friends = {"avinash","abhishek","ashish"}

art_not_science = art_friends.difference(science_friends)
print(art_not_science)

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

all_friends = art_friends.union(science_friends)
print(all_friends)

# Exercise
nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
user_input = input("Enter the name of a friend: ")
# Add the name to the empty set
user_friends.add(user_input)
# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
print(nearby_people.intersection(user_friends))



