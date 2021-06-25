Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Dictionaries
>>> data = {1:'William',2:'John',4:'Mike'}
>>> data
{1: 'William', 2: 'John', 4: 'Mike'}
>>> data[4]
'Mike'
>>> data[1]
'William'
>>> data[3]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data[3]
KeyError: 3

>>> data.get(1)
'William'
>>> data.get(3)
>>> # notice that there is no error message
>>> print(data.get(3))
None
>>> data.get(1,'Not Found')
'William'
>>> data.get(3,'Not Found')
'Not Found'
>>> 
>>> 
>>> # Dictionary with the help of lists
>>> 
>>> keys = ['will', 'john', 'mike']
>>> values = ['Python', 'Java', 'JS']
>>> data = dict(zip(keys,values))
>>> data
{'will': 'Python', 'john': 'Java', 'mike': 'JS'}
>>> # Merging two lists into a dictionary
>>> data['clare']
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    data['clare']
KeyError: 'clare'
>>> data['clare'] = 'CS'
>>> data
{'will': 'Python', 'john': 'Java', 'mike': 'JS', 'clare': 'CS'}
>>> # adding to a dictionary
>>> 
>>> del data['mike']
>>> data
{'will': 'Python', 'john': 'Java', 'clare': 'CS'}
>>> # deleting items from a dictionary
>>> 
>>> 
