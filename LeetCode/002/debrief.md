Without repeating numbers, we want to find the list of all unique sublists with length K that add up to N.

I brute forced this and cheated a little bit using the combinations function from itertools. This allows us to 
find all combinations of length K, and simply sum each of them to find which ones add to N.

Will most likely circle back to this and find a more algorithmic way to handle this.