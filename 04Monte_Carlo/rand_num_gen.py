"""
This is a simple python program to generate pseudo random numbers between 0 and 1 using Linear Congruent method
"""

import numpy as np


def rand_no_gen(seed, a, c, m, no_of_randnos):
    randno_array = np.zeros(no_of_randnos)
    randno_array[0] = seed
    for i in range(no_of_randnos - 1):
        randno_array[i + 1] = (a * randno_array[i] + c) % m
    return randno_array

def main():
    print(f'## A simple python script to generate random numbers ##')
    no_of_randnos = int(input('Enter the number of random numbers that you want: '))
    seed = int(input('Enter seed value: '))
    a = int(input("Enter 'a' parameter for the generator: "))
    c = int(input("Enter 'c' parameter for the generator: "))
    m = int(input("Enter 'm' parameter for the generator: "))
    print(f'The generated random numbers are {rand_no_gen(seed, a, c, m, no_of_randnos)}')


if __name__ == '__main__':
    main()
