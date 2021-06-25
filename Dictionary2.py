Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Dictionary 2
>>> # This is an example of a dictionary inside of a dictionary
>>> 
>>> prog = {'JS:'Atom', 'CS':'VS', 'Python':['Pycharm', 'Sublime'], 'Java':{'JSE':'Netbeans', 'JEE':'Eclipse'}}
	
SyntaxError: invalid syntax
>>> prog = {'JS':'Atom', 'CS':'VS', 'Python':['Pycharm', 'Sublime'], 'Java':{'JSE':'Netbeans', 'JEE':'Eclipse'}}
>>> prog
{'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}
>>> prog['JS']
'Atom'
>>> prog['Python']
['Pycharm', 'Sublime']
>>> prog['Python'][1]
'Sublime'
>>> prog['Java']
{'JSE': 'Netbeans', 'JEE': 'Eclipse'}
>>> prog['Java']['JEE']
'Eclipse'
>>> 
>>> prog['Atom']
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    prog['Atom']
KeyError: 'Atom'
>>> # so you can search only one way, like the way one would look up a name in a phone book and get a number and not look up a number and get a name
>>> # which makes sense, you look up words in a dictionary to get definitions, not the other way around