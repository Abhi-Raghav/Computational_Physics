"""
Simulate a simple random walk
"""


import random
import matplotlib.pyplot as plt


def random_walk(total_random_steps):
    x_values = []
    y_values = []
    x_initial = 0
    y_initial = 0
    x_values.append(x_initial)
    y_values.append(y_initial)

    for step in range(total_random_steps):
        x_new = x_values[-1] + (random.random()-0.5)*2
        y_new = y_values[-1] + (random.random()-0.5)*2
        x_values.append(x_new)
        y_values.append(y_new)

    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set(xlabel='x', ylabel='y', title='Random walk simulation')
    ax.grid()
    fig.savefig('random_walk.png')
    plt.show()


def main():
    random_walk(total_random_steps=20)


if __name__ == '__main__':
    main()

