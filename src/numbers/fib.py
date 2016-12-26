"""
generate Fibonacci sequence

Enter a number and have the program generate the Fibonacci
sequence to that number or to the Nth number.

usage:
    python fib.py [Nth of fib you want to calculate]
"""
import argparse


def fib_gen():
    """Fibonacci sequence generator, using yield"""
    first, sec = 0, 1
    while True:
        yield sec
        first, sec = sec, first + sec

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('n', metavar='N', type=int,
                        help='an integer for the fib')
    args = parser.parse_args()
    # to Nth number of fib
    to_Nth = args.n
    fib = fib_gen()
    current_fib = next(fib)
    for idx in range(0, to_Nth + 1):
        print('fib {}: {}'.format(idx, current_fib))
        current_fib = next(fib)
