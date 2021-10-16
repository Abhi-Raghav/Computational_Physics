"""
This is a simple python program to generate pseudo random numbers between 0 and 1 using Linear Congruent method
"""


import numpy as np
import matplotlib.pyplot as plt


def rand_no_gen(seed, a, c, m, no_of_randnos):
    """
    This function generates a numpy array of random numbers (positive integers) using Linear congruent method

    If r_i is initial random number, the next random number in the sequence is given by
    r_i+1 = (a*r_i + c) % m
    The random numbers generated will start repeating after m numbers
    Parameters
    ----------
    seed : int
        The starting 'seed' for the random no. generator
    a : int
        The multiplying parameter for the random no. generator
    c : int
        The adding parameter for the random no. generator
    m : int
        m determines how many number of random nos can be generated. Repetition starts after m entries
    no_of_randnos : int
        Total no of random numbers (including seed) required

    Returns
    -------
    randno_array : ndarray
        A numpy array of the random nos generated

    """
    randno_array = np.zeros(no_of_randnos)
    randno_array[0] = seed
    for i in range(no_of_randnos - 1):
        randno_array[i + 1] = (a * randno_array[i] + c) % m
    return randno_array


def random_generator_test(array_of_random_numbers):
    if len(array_of_random_numbers) % 2 != 0:
        mod_array = array_of_random_numbers[0:-1]
    else:
        mod_array = array_of_random_numbers
    x_values = []
    y_values = []

    for i in range(len(mod_array)):
        if i % 2 == 0:
            x_values.append(mod_array[i])
        else:
            y_values.append(mod_array[i])

    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Correlations of random nos')
    ax.grid(True)
    plt.show()


def main():
    print('## A simple python script to generate random numbers ##')
    no_of_randnos = int(input('Enter the number of random numbers that you want: '))
    seed = int(input('Enter seed value: '))
    a = int(input("Enter 'a' parameter for the generator: "))
    c = int(input("Enter 'c' parameter for the generator: "))
    m = int(input("Enter 'm' parameter for the generator: "))
    rand_array = rand_no_gen(seed, a, c, m, no_of_randnos)
    print(f'The generated random numbers are {rand_array}')
    random_generator_test(rand_array)


if __name__ == '__main__':
    main()
