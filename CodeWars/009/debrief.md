This question really just revolves around prime decomposition and printing out the correct string

I did have to look up the algorithm for prime decomposition, which makes 100% sense after seeing it.

We simply slowly iterate up through the numbers, and check if the number is divisible. If it is,
we divide by that number, add the prime to the list (or dictionary), and continue to check. If it is not 
divisible, we simply increment the number we are checking against and continue.

Once we've kept track of how many times we iterate through numbers, then we just have to organize the 
output correctly.
