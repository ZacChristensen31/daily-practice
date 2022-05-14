This was a pretty simple problem, focusing on translating a Roman Numeral string into an integer.

After handling the cases with subtraction (IV, IX, XL, XC, CD, CM), it was a simple matter of iterating
over the string and counting up each character. Then, we multiply by the appropriate value.

For example, the string "MCMXCIV" would be converted to "1994". We first calculate and remove the 
"CM" for 900, the "XC" for 90, the "IV" for 4. All that is left is the "M", and adding all together we get 1994