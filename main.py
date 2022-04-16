from pseudorandom import MiddleSquare


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    print(f"{'#' * 10}MIDDLE SQUARE{'#' * 10}")
    ms = MiddleSquare()
    numbers = ms.random_list(1000)
    fig, ax = plt.subplots()
    ax.plot(numbers)
    plt.show()