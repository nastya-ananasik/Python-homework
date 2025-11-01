books_by_year = {
    "Гаррі Поттер і філософський камінь": 1997,
    "Винні зірки": 2012
}
print(f"Старий словник: {books_by_year}")

new_book = {"13 причин чому": 2007}

if "13 причин чому" not in books_by_year:
    books_by_year.update(new_book)

print(f"Оновлений словник: {books_by_year}")
