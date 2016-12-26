"""
find the PI, using alogrithm
[Leibniz' formula](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80)
contiue previous question, but calulate precisce to particular digits
"""

from math import pi


def pi_generate():
    result = 0.0
    n = 0
    while True:
        result += 4 * ((-1.0) ** n / (2.0 * n + 1.0))
        yield result
        n += 1

if __name__ == '__main__':
    to_N_digits = 6
    elisp = 0.1 ** to_N_digits
    pi_gen = pi_generate()
    cureent_pi = next(pi_gen)
    generation = 1
    while True:
        if abs(cureent_pi - pi) <= elisp:
            break
        print('generation:{} cal PI:{}'.format(generation, cureent_pi))
        cureent_pi = next(pi_gen)
        generation += 1
