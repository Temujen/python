from functools import reduce

result_list = [i for i in range(100, 1001) if i % 2 == 0]
print(result_list)
print(reduce(lambda x, y: x * y, result_list))
