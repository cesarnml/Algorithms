#!/usr/bin/python

import argparse
import math


def find_max_profit(prices):
    # Iterate through prices[1:], while keeping track of max_profit and min_price seen
    # Initialize min_price to first element; max_profit = 0 (UPDATE)
    # Looks like the testing code forces you to take a loss if no profit possible
    # So now initializing max_profit = prices[1] - prices[0]
    # runtime O(n); space O(1)
    min_price = prices[0]
    max_profit = prices[1] - prices[0]
    for price in prices[1:]:
        max_profit = max(price - min_price, max_profit)
        min_price = min(price, min_price)
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
