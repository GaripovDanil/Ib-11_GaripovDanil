def average(values: list) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


print(average([1, 2, 3, 4, 5]))
print(average([-5, 2]))
