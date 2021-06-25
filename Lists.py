Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Lists
>>> 
>>> nums = [25,12,36,95,14]
>>> nums
[25, 12, 36, 95, 14]
>>> # Lists are implemented with [] square brackets

>>> nums[0]
25
>>> nums[5]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    nums[5]
IndexError: list index out of range
>>> nums[4]
14
>>> nums[2:]
[36, 95, 14]
  # This is called Slicing, the first number is inclusive and the last number is exclusive

>>> nums[-1]
14
>>> nums[-5]
25
>>> 
>>> names = ['will', 'John', 'Mike']
>>> names
['will', 'John', 'Mike']

>>> values = [9.5, 'will', 25]
>>> values
[9.5, 'will', 25]
>>> # In Python you are able to make lists with different data types

>>> mil = [nums, names]
>>> mil
[[25, 12, 36, 95, 14], ['will', 'John', 'Mike']]
>>> # you can also make a list of lists
>>> # Lists are mutable, which means you can change the values

>>> nums.append(45)
>>> nums
[25, 12, 36, 95, 14, 45]
>>> # appends adds to the end of the list


>>> nums
[25, 12, 36, 95, 14, 45]
>>> nums.insert(2,77)
>>> nums
[25, 12, 77, 36, 95, 14, 45]
>>> # insert, inserts a number at a given index position

>>> nums.remove(14)
>>> nums
[25, 12, 77, 36, 95, 45]
>>> # remove, removes a specified number

>>> nums.pop(1)
12
>>> nums
[25, 77, 36, 95, 45]
>>> # pop removes and prints the value given the index position number

>>> nums.pop()
45
>>> nums
[25, 77, 36, 95]
>>> # pop with out an index value, pops out the last value
>>> # In data structures, there is a concept called "Stack" which is last in fist out, or push and pop
>>> del nums[2:]
>>> nums
[25, 77]
>>> # "del" is a command to delete multiple values specified by [starting point:ending point]
>>> # google python doc commands for a complete list of all commands

>>> nums.extend([29,12,14,36])
>>> nums
[25, 77, 29, 12, 14, 36]
>>> # extend adds numbers to the list
    # there is no list concatination
>>> min(nums)
12
>>> max(nums)
77
>>> sum(nums)
193
>>> nums.sort()
>>> nums
[12, 14, 25, 29, 36, 77]
>>> 
    #
