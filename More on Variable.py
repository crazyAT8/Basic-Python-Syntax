Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # More on Variables
>>> 
>>> num = 5
>>> id(num)
2064006343088
>>> # this shows the address of the variable num
>>> 
>>> name = 'William'
>>> id(name)
2064006667120
>>> # id also works with strings
>>> 
>>> a = 10
>>> b = a
>>> a
10
>>> b
10
>>> id(a)
2064006343248
>>> id(b)
2064006343248
>>> # notice its the same address, thats because in Python if data is the same they will be stored together or in the same address
>>> id(10)
2064006343248
>>> # variables and values are both objects so the address will be the same
>>> k = 10
>>> id(k)
2064006343248
>>> 
>>> a = 9
>>> id(a)
2064006343216
>>> id(b)
2064006343248
>>> 
>>> k = a
>>> id(k)
2064006343216
>>> 
>>> b = 8
>>> 
>>> PI = 3.14
>>> PI
3.14
>>> PI = 3.15
>>> PI
3.15
>>> # In Python variables can't be set in stone
>>> 
>>> type(PI)
<class 'float'>
>>> 