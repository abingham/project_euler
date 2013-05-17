import euler_util

products = set()
for i_size in range(0,9):
    for j_size in range(0,9):
        if (i_size + 1) + (j_size + 1) + (i_size + j_size + 1) == 9:
            for i in range(10**i_size, 10**(i_size + 1)):
                for j in range(10**j_size, 10**(j_size + 1)):
                    if euler_util.pandigital([i,j,i*j]):
                        products.add(i*j)
print sum(products)
