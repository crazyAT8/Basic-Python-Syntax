Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Set
>>> # a set is a collection of unique elements
>>> # sets are defined with {} culy brackets
    # the difference between dictionaries and sets, is that dictionaries use key value pairs
>>> s = {22,25,14,21,5}
>>> s
{5, 21, 22, 25, 14}
>>> # set never fallows a sequence
>>> s = {25,14,98,63,75,98}
>>> s
{98, 25, 75, 14, 63}
>>> # notice that 98 isn't listed twice
>>> # you can not be sure of the set sequence
>>> # sets use a concept called hash, which improves the preformance by going as fast as possible
>>> s[2]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
>>> # what is the difference between sets and lists
>>> # 1. there is no assigned sequence to sets
>>> # 2. there are no duplicate values in sets
    # sets are immutable

    set1 = {1,2,3,4}
    set2 = {3,4,5,6}
    set1.intersection(set2)
    output: {3,4}
    
        .union
    output: {1,2,3,4,5,6}
    
        .difference
    output: {1,2}
