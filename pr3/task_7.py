start_range = 2
end_range = 30

for num in range(start_range, end_range + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)
