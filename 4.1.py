numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
my_list = numbers
more_than_zero = []
for element in my_list:
    if element != 0:
        more_than_zero.append(element)
zero = my_list.count(0)
result = more_than_zero + (zero * [0])
print(result)