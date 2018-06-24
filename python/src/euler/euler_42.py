# count triangle words

import euler_util

tgen = euler_util.triangles()
t = [tgen.next() for i in range(1000)]

f = open('words.txt', 'r')
data = f.read()
f.close()

words = [euler_util.word_value(d[1:-1]) for d in data.split(',')]
words = filter(lambda x: euler_util.bsearch(t, x) != -1, words)
# print len(words)
