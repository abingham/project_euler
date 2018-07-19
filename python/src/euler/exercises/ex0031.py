"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

from more_itertools import ilen

COINS = (200, 100, 50, 20, 10, 5, 2, 1)


def sum_to(amount, coins=COINS):
    for index, coin in enumerate(coins):
        if amount - coin == 0:
            yield (coin,)
        elif amount - coin > 0:
            for combo in sum_to(amount - coin, coins[index:]):
                yield (coin,) + combo
        else:
            yield from sum_to(amount, coins[index + 1:])
            break

def main():
    return ilen(sum_to(200))
