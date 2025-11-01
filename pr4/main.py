import utilities

my_numbers = [10, 45, 22, 8, 19, 50]

print(f"Список чисел: {my_numbers}")

avg = utilities.calculate_average(my_numbers)
maximum = utilities.find_max(my_numbers)

print(f"Середнє значення: {avg}")
print(f"Максимальне число: {maximum}")
