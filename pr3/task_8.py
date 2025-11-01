data = [1, 5, 15]
data.extend([10, 20])
print(f"Список після розширення: {data}")

val_to_delete = 10

found = False
i = 0
while i < len(data):
    if data[i] == val_to_delete:
        data.pop(i)
        found = True
        break
    i += 1

if found:
    print(f"Список після видалення {val_to_delete}: {data}")
else:
    print(f"Елемент {val_to_delete} не знайдено.")
