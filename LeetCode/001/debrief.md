For this problem, I did it in two ways - a naive way and a quicker, more intelligent way.

The problem asking for, given a number n, find the number of permutations strings with the length of n
that contain only vowels (a, e, i, o, u) and is in lexicographical order.

For instance, if n = 1, the answer is 5, because there are 5 permutations: a, e, i, o, u.
If n = 2, the answer is 15, because there are 15 permutations: aa, ae, ai, ao, au, ea, ee, ei, eo, eu, ia, ie, io, iu, oa, oe, oi, ou, ua, ue, ui, uo, uu.

After writing down the number of answers for the first few values of n, there was a pattern.
Starting at 1 (the number of strings starting with u is always 1), the next vowel (o) increases by the n-1['o'] number of strings.
Repeat this over and over, and we end up with the right answer.

For the intelligent way, we do the same process, but we just update in place and can use some nifty array tricks to handle things.