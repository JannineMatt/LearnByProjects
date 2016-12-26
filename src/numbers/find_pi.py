"""
find the PI, using alogrithm
[Leibniz' formula](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80)
"""


def pi_generate():
    result = 0.0
    n = 0
    while True:
        result += 4 * ((-1.0) ** n / (2.0 * n + 1.0))
        yield result
        n += 1

if __name__ == '__main__':
    times = 10000
    pi_gen = pi_generate()
    current_pi = next(pi_gen)

    for idx in range(times):
        print('generation:{} current pi: {}'.format(idx, current_pi))
        current_pi = next(pi_gen)
