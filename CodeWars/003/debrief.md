We get two inputs, a number N, and a starting power P. Splitting N in to individual
digits, we take each digit and raise it to the power of P, increasing the power by 1 each digit.

After this, we check to see if the output is divisible by N. If it is, return the number that
N multiplies to get the output - otherwise return -1.

This was accomplished through a quick list comprehension, then checking the division.