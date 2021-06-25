Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Data Types
>>> 	# None
	
>>> 	# Numeric
	
>>> 	# List
	
>>> 	# Tuple
	
>>> 	# Set
	
>>> 	# String
	
>>> 	# Range
	
>>> 	# Maps/Dictionary
	
>>> # None
>>> 	# When a variable doesn't have an assigned value
	
>>> # Numeric
>>> # four types
>>> # 1. int
>>> # 2. float
>>> # 3. complex
>>> # 4. bool
>>> 
>>> num = 2.5
>>> type(num)
<class 'float'>
>>> 
>>> num = 5
>>> type(num)
<class 'int'>
>>> 
>>> num = 6+9j
>>> type(num)
<class 'complex'>
>>> 
>>> a = 5.6
>>> b = int(a)
>>> type(b)
<class 'int'>
>>> b
5
>>> k = float(b)
>>> k
5.0
>>> 
>>> k = 6
>>> c = complex(b,k)
>>> c
(5+6j)
>>> 
>>> b<k
True
>>> bool = b < k
>>> bool
True
>>> type(bool)
<class 'bool'>
>>> b > k
False
>>> # in Python True = 1 and False = 0
>>> int(True)
1
>>> int(False)
0
>>> 
>>> 
>>> # Lists
>>> lst = [25,36,45,12]
>>> type(lst)
<class 'list'>
>>> 
>>> s = {2,3,4,5,6}
>>> type(s)
<class 'set'>
>>> 
>>> t = (4,5,6,7,6)
>>> type(t)
<class 'tuple'>
>>> 
>>> str = "william"
>>> type(str)
<class 'str'>
>>> 
>>> st = 's'
>>> type(st)
<class 'str'>
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> # this converts the range into a list, this is also a "for loop"
>>> 
>>> list(rang(2,10,2))
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    list(rang(2,10,2))
NameError: name 'rang' is not defined
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> type(range(10))
<class 'range'>
>>> 
>>> # Lists, Tuples, Sets, Strings, and Ranges are all a sequence type of data
>>> 
>>> #Dictionarys
>>> # for every value we'll assign a key
>>> d = {'will':'samsung','mike':'iphone','john':'android'}
>>> d
{'will': 'samsung', 'mike': 'iphone', 'john': 'android'}
>>> d.keys()
dict_keys(['will', 'mike', 'john'])
>>> d.values()
dict_values(['samsung', 'iphone', 'android'])
>>> d['mike']
'iphone'
>>> d.get('john')
'android'
>>> 