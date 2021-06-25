Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Variables
>>> 2+3
5
>>> x = 2
>>> # a variable is essentially an container with contents on the inside, which are called values
>>> # in this case x is the variable and 2 is the value
>>> # and notice that there was no out put for x = 2, thats because of the equals sign, which makes it an assignment operation
>>> x+3
5
>>> y = 3
>>> x+y
5
>>> # by definition a variable can be changed at any time
>>> x = 9
>>> x + y
12
>>> x
9
>>> abc
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    abc
NameError: name 'abc' is not defined
>>> x + 10
19
>>> _ + y
22
>>> # _ or an underscore, is the output of the previous operation
>>> 
>>> name = 'youtube'
>>> name
'youtube'
>>> name + 'rocks'
'youtuberocks'
>>> # don't forget the space before the word
>>> name + ' rocks'
'youtube rocks'
>>> 
>>> name ' rocks
SyntaxError: EOL while scanning string literal
>>> name 'rocks'
SyntaxError: invalid syntax
>>> # you need a plus sign
>>> 
>>> # This next section will be on how to fetch a letter from a string
>>> 
>>> name
'youtube'
>>> name[0]
'y'
>>> name[6]
'e'
>>> name[8]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    name[8]
IndexError: string index out of range
>>> name[-1]
'e'
>>> # a minus sign or negative numbers will count right to left
>>> name[-2]
'b'
>>> name[-7]
'y'
>>> name[0:2]
'yo'
    # this is called slicing, the first number is inclusive the second number is exclusive
>>> name[1:4]
'out'
>>> # the first number is the starting point and the second is the stopping point
>>> name[1:]
'outube'
>>> name[:4]
'yout'
>>> # is the stopping or starting points aren't specified is will out put everything
>>> name[3:10]
'tube'
>>> # inputing a number that exceeds the number of characters will still print everything from the starting point
>>> name[0:3] = 'my'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    name[0:3] = 'my'
TypeError: 'str' object does not support item assignment
>>> name[0] = 'R'
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    name[0] = 'R'
TypeError: 'str' object does not support item assignment
>>> # Strings in python are immutable, meaning that you can not change the value of it
>>> 
>>> 'my ' + name[3:]
'my tube'
>>> myname = 'William Watson'
>>> len(myname)
14
>>> # 'len' is the length function, which when used, outputs the number of characters in a string
