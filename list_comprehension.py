#1 the following program is done in the normal way

numbers = [1,2,3,4,5,6]
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)

print(doubled_numbers)

#2 Using list comprehension the above program could be done in the following manner

numbers = [1,2,3,4,5,6,7]
doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)

square_numbers = [n**2 for n in range(10)]
print(square_numbers)

#3

ages = [23,25,25,26,24]
 
friend_ages = [f"My friend is {age} years old." for age in ages]
print(friend_ages)

#4

friends = ["ROlf", "Bob", "Charlie", "Tom"]
lower = [friend.lower() for friend in friends]
print(lower)

#5
friend = input("Enter your friend's name: ")

friend_list = ["Rolf", "Bob", "Charlie", "Tom"]
friends_lower = [friend.lower() for friend in friend_list]

if friend.lower() in friends_lower:
    print(f"{friend.title()} is one of my friends.")




