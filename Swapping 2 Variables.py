Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Swapping 2 Variables
>>> 
>>> a = 5
>>> b = 6
>>> 
>>> a = b
>>> b = a
>>> 
>>> print(a)
6
>>> print(b)
6
>>> # doesn't work bc nothing is assigned to 5
>>> 
>>> 
>>> a = 5
>>> b = 6
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> a = 5
>>> b = 6
>>> 
>>> temp = a
>>> a = b
>>> b = temp
>>> 
>>> print(a)
6
>>> print(b)
5
>>> # it works using a temporary variable
>>> 
>>> 
>>> a = 5
>>> b = 6
>>> 
>>> a = a + b
>>> b = a - b
>>> a = a - b
>>> 
>>> print(a)
6
>>> print(b)
5
>>> 
>>> 
>>> a = 5
>>> b = 6
>>> 
>>> a = 5    # 101  which is 3 bits
>>> b = 6    # 110 which is also 3 bits
>>> 
>>> a = a + b  # equals 11 (which needs 4 bits)
>>> b = a - b  # equals 5
>>> a = a - b  # equals 6
>>> 
>>> print(a)
6
>>> print(b)
5
>>> # this works without the use of a third variable
>>> 
>>> 
>>> a = 5
>>> b = 6
>>> 
>>> a,b = b,a
>>> 
>>> print(a)
6
>>> print(b)
5
>>> # this swap on a single line is only avalible in Python
>>> # based on the concept "Rot_Two()" which swaps the two top-most stack items