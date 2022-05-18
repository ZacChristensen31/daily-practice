This problem was fairly simple - because Python has a count function, we simply loop through the characters
and find the first one that has a count of 1. I may return to this and find a more efficient solution, 
as I believe this has to loop more times than necessary to count the number of times the character appears.

Possibly can use some sort of dictionary? Or some tuple system to keep track of order, but also the count of the letters.
At most this would be O(n) I believe... no guarantee of that though