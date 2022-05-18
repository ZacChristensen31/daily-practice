This one was interesting. We need to have a function for each number (one(), two(), etc.), as well as one
function for each method (plus(), minus(), etc.). Then, we want to make sure that things work correctly when
we combine the methods together (for example, seven(times(five())) would produce 35).

Each test case is in the form of number(operation(number())).

To keep things clean, I extracted the main logic that each number utilized. For this base function, it 
takes in two parameters - the number itself (0, 1, 2, etc.) and the operation (plus(), minus(), etc.).

If the operation is None, then we just return the number. Otherwise, we return the operation(number).

The operations are lambdas, which take in a number and return the result of the operation.

For example, let's look at seven(plus(five())). The function five() resolves to 5. This means that the function
plus(5) now resolves to a lambda that takes in a number and returns the result of adding 5 to that number - 
literally lambda x: x + 5. When we call seven(plus(five())), we call base(7, lambda x: x + 5).

Because the function is not None, then we rturn lambda x: x + 5 where x == 7, thus we return 12.