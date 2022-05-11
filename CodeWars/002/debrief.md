Fairly easy problem here, double checking that squaring each number in list A equals list B.

For example, if you have A = [1, 2, 3] and B = [1, 4, 9], then we expect the response to be True.
If you have A = [1, 2, 3] and B = [1, 2, 3], then we expect the response to be False.

My solution was simply comparing arrays, as Python automatically compares arrays this way. We
square each number in A and compare it to the corresponding number in B.

In pseudocode, there are a few steps. First, sort both arrays. Square each number in A and compare against
the corresponding index with B. If we ever get a mismatch, we can return False.

We can also take a few shortcuts by checking lengths at the start, along with presence of empty lists.