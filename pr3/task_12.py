t1 = (10, 20)
t2 = (30, 40)

temp_list = []
for item in t1:
    temp_list.append(item)
for item in t2:
    temp_list.append(item)

new_tuple = tuple(temp_list)

print(f"Об'єднаний: {new_tuple}")
