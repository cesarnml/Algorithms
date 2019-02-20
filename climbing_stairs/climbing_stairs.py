#!/usr/bin/python

import sys

# climbing_stairs(n) = climbing_stairs(n-3) + climbing_stairs(n-2) + climbing_stairs(n-1)
# Analogues solution to recursive Fibonacci sequence with memoization implementation
# runtime O(?) definitely better than O(2^n) ... probably O(n)
# space O(n) [due to memoization hash] + stack-size ... ?


def climbing_stairs(n, cache={}):
    if n <= 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n >= 3:
        if n in cache:
            return cache[n]
        else:
            value = climbing_stairs(
                n-3, cache) + climbing_stairs(n-2, cache) + climbing_stairs(n-1, cache)
            cache[n] = value
            return value


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
