numbers = [0, 1, 7, 2, 4, 8]
my_list = numbers
if len(numbers) == 0:
    result = 0
else:
    first_action = numbers[::2]
    second_action = numbers[-1]
    result = sum(first_action) * second_action
print(result)
