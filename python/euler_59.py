import contextlib, operator

def read_cipher(filename):
    data = []
    with contextlib.closing(open(filename, 'r')) as file:
        for line in file:
            data += [int(c) for c in line.split(',')]
    return data

def key_gen(key):
    while True:
        for k in key:
            yield k

def decode(data, key):
    kg = key_gen(key)
    return ''.join([chr(operator.xor(d, kg.next())) for d in data])

def searcher():
    data = read_cipher('cipher.txt')
    for a in range(ord('a'), ord('z') + 1):
        for b in range(ord('a'), ord('z') + 1):
            for c in range(ord('a'), ord('z') + 1):
                decoded = decode(data, [a,b,c])
                if 'the' in decoded and 'and' in decoded:
                    print '***',a,b,c,'***'
                    print decoded
                    print ''

def run():
    data = read_cipher('cipher.txt')
    key = [103,111,100]
    decoded = decode(data, key)
    return sum([ord(d) for d in decoded])

print run()
