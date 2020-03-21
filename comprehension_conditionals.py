#1

ages = [23,24,25,26,27,22,21]
odds = [age for age in ages if age % 2 == 1]

print(odds)


#2

friends = ["A","B","C","D","E","F"]

guests = ["E", "f", "G", "H", "I"]

friend_lower = set([friend.lower() for friend in friends])
guest_lower = set([guest.lower() for guest in guests])

common = friend_lower.intersection(guest_lower)
print(common)
