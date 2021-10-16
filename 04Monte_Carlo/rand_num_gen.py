"""
This is a simple python program to generate pseudo random numbers between 0 and 1 using Linear Congruent method
"""

import numpy as np


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
    randno_array : numpy.array(int)
        A numpy array of the random nos generated

    """
    randno_array = np.zeros(no_of_randnos)
    randno_array[0] = seed
    for i in range(no_of_randnos - 1):
        randno_array[i + 1] = (a * randno_array[i] + c) % m
    return randno_array


def main():
    print('## A simple python script to generate random numbers ##')
    no_of_randnos = int(input('Enter the number of random numbers that you want: '))
    seed = int(input('Enter seed value: '))
    a = int(input("Enter 'a' parameter for the generator: "))
    c = int(input("Enter 'c' parameter for the generator: "))
    m = int(input("Enter 'm' parameter for the generator: "))
    print(f'The generated random numbers are {rand_no_gen(seed, a, c, m, no_of_randnos)}')


if __name__ == '__main__':
    main()
