import calculator

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
operation = input("Введіть операцію (+, -, *, /): ")

if operation == '+':
    result = calculator.add(num1, num2)
    print(f"Результат: {num1} + {num2} = {result}")
elif operation == '-':
    result = calculator.subtract(num1, num2)
    print(f"Результат: {num1} - {num2} = {result}")
elif operation == '*':
    result = calculator.multiply(num1, num2)
    print(f"Результат: {num1} * {num2} = {result}")
elif operation == '/':
    result = calculator.divide(num1, num2)
        
    if result is None:
        print("Помилка: Ділення на нуль неможливе!")
    else:
        print(f"Результат: {num1} / {num2} = {result}")
else:
    print("Помилка: Невідома операція.")

