#1. Greeting and Age Check
name = input("Enter your name: ")
age = int(input("Enter your age: "))

def greeting():
    if age >= 18:
        print(f"Hello {name.title()}! You can enter!")
    else:
        print(f"Sorry {name.title()}, you are too young to enter.")

greeting()

# 3. Sum of User Inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

numbers = [num1, num2, num3]
total = sum(numbers)

print(f"The total is {total}")

if total % 2 == 0:
    print(f"Your sum is even!")
else:
    print(f"Your sum is odd!")

print(numbers)

# 4. Fruit Basket
fruits = {"apple": 10, "banana": 5, "kiwi": 7, "strawberry": 3}
enter_fruit = input("Enter fruit name: ")
if enter_fruit in fruits:
    print(f"We have {fruits[enter_fruit]} {enter_fruit}(s) available")
    for letter in enter_fruit:
        print(letter)
else:
    print("Sorry, we don't have that fruit.")

# 5. Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))
farentheid = (celsius * 9/5) + 32
print(f"This is your temperature in Farentheid: {farentheid}")
if farentheid > 80:
    print(f"It's hot!")
else:
    print(f"It's not too hot.")
temperatures = [celsius, farentheid]
print(temperatures)

# 6. Menu Selection
menu = {"coffee": 30, "tea":20, "juice":25, "smoothie":15}
order = input("Enter what you want to order: ")
if order in menu:
    print(f"{order} costs {menu[order]}.")
else:
    print(f"Item not found.")

for key, value in menu.items():
    print(key,value)