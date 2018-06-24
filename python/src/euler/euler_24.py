import euler_util

iter = euler_util.combinations([0,1,2,3,4,5,6,7,8,9])
for i in range(1000000):
    val = iter.next()
# print ''.join('%d' % i for i in val)
