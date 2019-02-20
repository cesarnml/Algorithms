#!/usr/bin/python

import sys

# runtime O(n) due to needs to loop through n rounds; space O(n) due to recursive stack


def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    outcomes = []
    if n == 0:
        return [[]]

    def helper(play, i):
        # recursive helper that builds each list, play-by-play
        for option in options:
            play = play + [option]
            if i == n:
                outcomes.append(play)
            else:
                helper(play, i + 1)
            # removes last option from current list before next list is created
            play = play[:-1]
    helper([], 1)
    return outcomes


rock_paper_scissors(2)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
