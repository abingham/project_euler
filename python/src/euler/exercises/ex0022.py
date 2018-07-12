ord_base = ord('A') - 1

def letter_sum(name):
    return sum([ord(letter) - ord_base for letter in name])

names = []
f = open('names.txt', 'r')
for l in f:
    names += [filter(lambda x: x != '"', i) for i in l.split(',')]
names.sort()

score_sum = 0
for i in range(len(names)):
    score_sum += ((i + 1) * letter_sum(names[i]))
# print score_sum
