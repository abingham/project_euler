import euler_util as eu

def run():
    count = 0
    for p in range(1,22):
        for x in eu.numbers(1):
            l = eu.length(pow(x,p))
            if l > p:
                break
            if l == p:
                count += 1
    return count

print run()
