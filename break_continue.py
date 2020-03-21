#1 Break

cars = ["ok","ok","ok","ok","faulty","ok","ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line.")
        break
    print(f"This car is {status}.")
    

#2 continue

cars = ["ok","ok","ok","ok","faulty","ok","ok"]

for status in cars:
    if status == "faulty":
        print("Found a faulty car...")
        continue
    print(f"This car is {status}.")
    
#3 Exercise

for i in range(16):
    if i % 15 == 0:
        print("Fizzbuzz")
    elif i % 5 == 0:
        print("Fizz")
    elif i % 3 == 0:
        print("Buzz")
    else:
        print(i)

#4 else could be used with for loops

cars = ["ok","ok","ok","ok","faulty","ok","ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production.")
        break
    print(f"This car is {status}.")
else:
    print("All cars are fault-free. Ready for shipping.")


#5 Finding the prime number

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} equals {x}*{n//x}")
            break
    else:
        print(f"{n} is a prime number.")
