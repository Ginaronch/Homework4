import random
my_list = [random.randrange(10) for element in range(3,10)]
print(my_list)
result = [my_list[0], my_list[2], my_list[-2]]
print(result)