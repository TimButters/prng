import math

import numpy as np
import matplotlib.pyplot as plt

from pseudorandom import MiddleSquare, LinConGen


def spectral_test(prng, *, num_points=1000, dim=3):
    numbers = prng.random_list(num_points * dim)
    points = np.array(numbers).reshape(-1, dim)

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], marker="o")
    return points


def to_binary(number, only_decimal=True):
    if isinstance(number, int):
        return format(number, "b")
    if isinstance(number, float):
        a, b = str(number).split(".")
        if only_decimal:
            return format(int(b), "b")
        return "".join([format(int(n), "b") for n in [a, b]])
    return ValueError("input must be an int or a float.")


def monobit_test(number):
    if isinstance(number, int):
        binary = [int(d) for d in list(to_binary(number))]
    elif isinstance(number, list):
        binary = [int(d) for n in number for d in list(to_binary(n))]
    else:
        raise ValueError("Input must be an int or list of ints.")

    bit_length = len(binary)
    total = 2 * sum(binary) - bit_length
    sobs = total / math.sqrt(bit_length)
    return math.erfc(math.fabs(sobs) / math.sqrt(2))


if __name__ == "__main__":
    ms = MiddleSquare().random_list(1000)
    lcg = LinConGen().random_list(1000)

    fig, axs = plt.subplots(2, 1)
    axs[0].plot(ms, label="Middle Square")
    axs[1].plot(lcg, label="Linear Congruential Generator")

    for ax in axs:
        ax.legend(loc=1)
        ax.set_xlabel("Iteration")

    # RANDU
    spectral_test(LinConGen(a=65539, c=0, m=2**31))

    plt.show()
