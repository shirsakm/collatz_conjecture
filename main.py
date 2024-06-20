import matplotlib.pyplot as plt
import random
import sys

def main():
    try:
        fig, ax = plt.subplots()

        if len(sys.argv) < 2:
            print("Usage: python main.py ...")
            sys.exit(1)

        else:
            try:
                n = [int(x) for x in sys.argv[1:]]
            except:
                print("ERROR: Please enter valid numbers")
                sys.exit(1)

        for i in n:
            collatz_values = get_collatz_values(i)

            print(f"Steps required for {i} were {len(collatz_values)}")

            color = f"C{random.randint(0, 9)}"     
            ax.plot([i for i in range(1, len(collatz_values) + 1)], collatz_values, marker = 'o', color = color, label = f"{i}")

        set_graph(ax)
        plt.show()

    except KeyboardInterrupt:
        print("Exiting program...")
        sys.exit(0)


def set_graph(ax: plt.Axes):
    ax.set_title("Collatz Conjecture")
    ax.set_facecolor('#EBEBEB')
    ax.legend(loc = 'upper right')


def collatz_function(n: int):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def get_collatz_values(n: int):
    collatz_values = [n]
    while n != 1:
        y = collatz_function(n)
        collatz_values.append(y)

        n = y

    return collatz_values


if __name__ == '__main__':
    main()