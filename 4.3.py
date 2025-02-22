import random
my_list = [random.randrange(10) for element in range(random.randint(3, 10))] #для каждого элемента в случайном дипазоне от 3 до 10(включительно) выдать случайное значение от 0 до 10(не включительно)
print(my_list)
result = [my_list[0], my_list[2], my_list[-2]]
print(result)