import matplotlib.pyplot as plt

from pseudorandom import MiddleSquare, LinConGen


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