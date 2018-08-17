### String

Python has a built-in string class named "str" with many handy features.

    >>>help(str)
    
String literals can be enclosed by either double or single quotes,
although single quotes are more commonly used.
Backslash escapes work the usual way within both single and double quoted literals.
A double quoted string literal can contain single quotes without any fuss and likewise single
 quoted string can contain double quotes. A string literal can span multiple lines,but there
 must be a backslash \ at the end of each line to escape the new line.String literals inside 
 triple quotes,""" or ''' ,can span multiple lines to text.
 
 
    ''
    ""
    '''
    """
    >>> print("hello 'Jun'")
    hello 'Jun'
    
    >>> print('hello "Tom"')
    hello "Tom"
    
Python string are "immutable" which means they cannot be changed after they are created.
Since string can't be changed, we construct "new" string as we go to represent computed
values. 

    >>> print("hello" + "world")
     helloworld

Characters in a string can be accessed using the standard [ ] syntax,and  like 
Java and C++,Python uses zero-based indexing,so if is 'hello' s[1] is 'e'.
If the index is out of bounds for the string ,Python raises an error. 

    >>> string = 'hello'
    >>> print(string[1])
     e
     >>> print(string[9])
     Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     IndexError: string index out of range


#### String Method 

copy

拼接

查找

统计

检测

切片

大小写