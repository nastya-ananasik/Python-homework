dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
car = dict_test.get('car')
where = dict_test.get('where')
print(f"car: {car}, where: {where}")

print(dict_test.keys())
print(dict_test.values())

for key, value in dict_test.items():
    print(f"{key} -> {value}")
