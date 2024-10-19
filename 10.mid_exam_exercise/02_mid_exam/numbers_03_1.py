FIRST_COUNT = 5
numbers = [int(x) for x in input().split()]
average_num = sum(numbers) / len(numbers)
filtered_nums = sorted([x for x in numbers if x > average_num])

if not filtered_nums:
    print("No")
else:
    print(*[filtered_nums.pop() for i in range(FIRST_COUNT) if filtered_nums])