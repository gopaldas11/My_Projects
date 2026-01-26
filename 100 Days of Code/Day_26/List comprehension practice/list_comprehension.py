# Now i am practicing list comprehension.

# nums = [1,2,4,7,8,23,34,56,78,90]
#
# squer_numbers = [n*n for n in nums]
# print(squer_numbers)


# numbrs = [7, 94, 21, 58, 36, 82, 13, 67, 45, 9,
# 71, 26, 54, 88, 32, 60, 5, 97, 41, 19,
# 76, 24, 63, 11, 90, 38, 49, 84, 16, 69,
# 2, 57, 33, 92, 28, 75, 44, 10, 86, 51,
# 65, 18, 80, 34, 98, 22, 59, 14, 73, 47]
#
# results = [num for num in numbrs if num % 2 == 0]
# print(results)

with open("./file1.txt") as f1:
    file_1 = f1.readlines()
with open("./file2.txt") as f2:
    file_2 = f2.readlines()

result = [int(num) for num in file_1 if num in file_2]
print(result)