#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    outcomes = []
    if n == 0:
        return [[]]

    def helper(play, i):
        for option in options:
            play = play + [option]
            if i == n:
                outcomes.append(play)
            else:
                helper(play, i + 1)
            play = play[:-1]
    helper([], 1)
    return outcomes


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
