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


if __name__ == "__main__":
    ms = MiddleSquare().random_list(1000)
    lcg = LinConGen().random_list(1000)

    fig, axs = plt.subplots(2, 1)
    axs[0].plot(ms, label="Middle Square")
    axs[1].plot(lcg, label="Linear Congruential Generator")

    for ax in axs:
        ax.legend(loc=1)
        ax.set_xlabel("Iteration")
    plt.show()
