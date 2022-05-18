This one was pretty easy - sorting the numbers in any order, putting the even
numbers first and then the odd numbers in any order.

Honestly the more intensive part was figuring out how to test this correctly,
since the lists could be in any order. Sorting was simply passing in a key where
the key was x % 2, essentially putting the even numbers first and the odd numbers
second.