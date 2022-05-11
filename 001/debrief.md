Basically, pretty simple stuff. O(n) time and O(n) space

Loop through the string, and keep track of open braces.
Pop off if you see a non-open brace, and make sure that it matches the last open brace.

If not, return false. If we get through the string and have unclosed braces, return false.