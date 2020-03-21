#1

is_learning = True

while is_learning:
    print("You're learning.")
    user_input = input("Are you learning? ")
    is_learning = user_input == "yes"

#2

user_input = input("Enter your response:(p/q) ")

while user_input != 'q':
    if user_input == 'p':
        print("Hello!")
    user_input = input("Enter your response:(p/q) ")
print("Bye.")

