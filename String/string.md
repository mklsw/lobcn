## String 字符串 
Python 内置的类 "Str" 字符串有很多便利的功能，它的表示方法为单引号，双引号和三引号.

    ''
    ""
    '''
    """
    
字符串创建以后是不可更改的. 

### 字符串的转义

1. 遇到特殊字符时，Python 用反斜杠"\" 转义字符 



    >>> 'doesn\'t'
    "doesn't"
    
    >>> "doesn't"
    "doesn't"
    
    >>> '"yes,"they said.'
    '"yes,"they said.'
    
    >>> "\"yes,\"they said."
    '"yes,"they said.'


列表

![string](https://raw.githubusercontent.com/mklsw/lobcn/master/Pictures/string_escape.png)


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


### String Method 

copy

拼接

查找 find

统计

检测

切片

大小写