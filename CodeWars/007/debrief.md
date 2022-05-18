For this problem, we take in a list of numbers. We want to return a list where the
odd numbers are sorted, but the even numbers are left in their original order.

This was pretty simple - essentially iterate through the list, copy and sort the
odd numbers. Then iterate through the list again - if you find an odd number,
then pop it from the list and replace the odd number with the new odd number. 