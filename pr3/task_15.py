capital_city_map = {
    "Україна": "Київ",
    "Польща": "Варшава",
    "Німеччина": "Берлін"
}

query_country = "Італія"
print(f"Шукаємо столицю для: {query_country}")

capital = capital_city_map.get(query_country)

if capital:
    print(f"Столиця: {capital}")
else:
    print(f"Інформація про країну '{query_country}' відсутня.")
