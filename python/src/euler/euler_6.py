def sum_of_squares(count):
    return reduce(lambda x,y: x + y**2, range(1, count + 1))

def square_of_sum(count):
    return sum(range(1, count + 1)) ** 2

# print square_of_sum(100) - sum_of_squares(100)
