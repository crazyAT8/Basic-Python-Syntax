Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Operators
>>> 
>>> #Arithmetic Operator
>>> x = 2
>>> y = 3
>>> x + y
5
>>> x - y
-1
>>> x * y
6
>>> x / y
0.6666666666666666
>>> 
>>> 
>>> # Assignment Operator
>>> x = x + 2
>>> x
4
>>> x += 2
>>> x
6
>>> x *= 3
>>> x
18
>>> 
>>> a,b = 5,6
>>> a
5
>>> b
6
>>> # assigning type variables two different values in one line
>>> 
>>> 
>>> # Unity Operator
>>> # means one
>>> n = 7
>>> n
7
>>> -n
-7
>>> n
7
>>> n = -n
>>> n
-7
>>> 
>>> # Relational Operators
>>> # comparing two variables
>>> 
>>> a < b
True
>>> a > b
False
>>> a == b
False
>>> a = 6
>>> a == b
True
>>> a <= b
True
>>> a >= b
True
>>> a != b
False
>>> 
>>> b = 7
>>> a != b
True
>>> 
>>> 
>>> # Logical Operators
>>> # bases on And, Or, & Not
>>> 
>>> a = 5
>>> b = 5
>>> a < 8 and b < 5
False
>>> 
>>> a = 5
>>> b = 4
>>> a < 8 and b < 5
True
>>> a < 8 and b < 2
False
>>> # Truth Table
>>> # X--Y--C   (C is the output)
>>> # 0--0--0
>>> # 0--1--0
>>> # 1--0--0
>>> # 1--1--1
>>> 
>>> # 1 = True
>>> # 0 = False
>>> 
>>> a < 8 or b < 2
True
>>> # Or Table
>>> # X--Y--C
>>> # 0--0--0
>>> # 0--1--1
>>> # 1--0--1
>>> # 1--1--1
>>> 
>>> x = True
>>> not x
False
>>> x = not x
>>> x
False
>>> # not negates the value



    # Membership Operators
        # object is a member of a collection: in
        # object is not a member of a collection: not in
        # returns a boolean True or False



    # Identity Operators
        # Two variables point to the same object: is
        # Two variables do not point to the same object: is not
