from euler.lib.sequences import collatz

from more_itertools import ilen


def main():
    max_number = int(1e6)
    chains = ((n, ilen(collatz(n)))
              for n in range(1, max_number + 1))
    return max(chains, key=lambda x: x[1])[0]
