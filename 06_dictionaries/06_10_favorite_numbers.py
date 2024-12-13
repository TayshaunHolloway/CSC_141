favorite_numbers = {
    'Alice': [7, 127],
    'Bell': [47, 99, 25],
    'Carson': [47, 28],
    }
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"  {number}")