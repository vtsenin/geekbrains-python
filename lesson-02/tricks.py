# 1
nums = [
    [1, 2, 3],
    [4, 5, 6],
]
joined = sum(nums, [])

print(joined)

# 2 Удаление дубликатов в списках
unique = [1, 2, 3, 4, 3]
print(unique)
unique = list(set(unique))
print(unique)

# 3
a, b = 10, 20
# a = 10
# b = 20

a, b = b, a

# 4
total = [1, 2, 2, 2, 3, 4, 3]
print(
    max(
        set(total),
        key=total.count
    )
)

# 5
print(*total, end='', sep='-')