This hashtag calcualtor was interesting - start with a hashtag, then Pascal Case for the rest of the words that are
split by any number of spaces.

My solution kept track of a capitalization flag, then interated through each character of the input string.
If the next character isn't a space, and the flag is True, capitalize the character. If the flag is false, lowercase
the character. If the character is a space, set the flag to True and continue.