# british money combinations

def numbers(start=0, stride=1):
    i = start
    while True:
        yield i
        i += stride

coins = [200,100,50,20,10,5,2,1]
sum = 0

def use_count(c,incoming=0):
    global sum

    if len(c) == 0:
        return

    for i in numbers():
        local = i * c[0]
        subtotal = local + incoming

        if subtotal > 200:
            return
        elif subtotal < 200:
            use_count(c[1:], subtotal)
        else:
            sum += 1
            return

use_count(coins)
# print sum
