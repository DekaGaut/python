greeting = "You are cordially invited!!"
greeting = "It\'s your birthday?"

""""
String formatting
"""

age = 34
print(f"Your age is {age}.")

name = input("Enter a friend's name: ")
greeting = "How are you, {}?"
print(greeting.format(name))

name = "Gautam"
greeting = f"Hi {name}, how are you?"
print(greeting)

name = input("Enter a name: ")
greeting = "Hi {}, how are you?"
print(greeting.format(name))


