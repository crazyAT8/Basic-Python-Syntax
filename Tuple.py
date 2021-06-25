Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Tuple
>>> # Tuple is immutable, which means it can not be changed
>>> # Used the way lists are used
>>> tup = (21,36,14,25)
>>> tup
(21, 36, 14, 25)
>>> tup[1]
36
>>> tup[1] = 33
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tup[1] = 33
TypeError: 'tuple' object does not support item assignment
>>> tup.count
<built-in method count of tuple object at 0x0000013624AD54A0>
>>> tup.count()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tup.count()
TypeError: tuple.count() takes exactly one argument (0 given)
>>> # Tuples are defined with round brackets after the equal sign
>>>
    # tuple comprehension

    tuple(x for x in [1,2,3,4,5,6,7,8,9,10])

      output: (1,2,3,4,5,6,7,8,9,10)
