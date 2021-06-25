Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Number System Conversion
>>> 
>>> bin(25)
'0b11001'
>>> # bin converts decimal to binary system
>>> # This is how you convert
>>> # Divide 25 by 2 = 12 with 1 remanying
>>> # Divide 12 by 2 = 6 with  0 remaining
>>> # Divide 6 by 2 = 3 with 0 remaining
>>> # Divide 3 by 2 = 1 with 1 remaining
>>> 
>>> # the 0b is how you represent a binary format bc you might read 11001 as a decimal but placing the "0b" at the beginning, tells the reader its binary
>>> 
>>> 0b0101
5
>>> 
>>> 
>>> # Octsl System (only uses 8 numbers 0,1,2,3,4,5,7)
>>> oct(25)
'0o31'
>>> # the "0o" deliniates that is octal format
>>> 
>>> 
>>> # Hexadecimal System (base 16 system 0-9 then a-f)
>>> hex(25)
'0x19'
>>> # "0x" deliniates a hexadecimal number
>>> hew(10)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    hew(10)
NameError: name 'hew' is not defined
>>> hex(10)
'0xa'
>>> 0xf
15
>>> 2**0
1
>>> 