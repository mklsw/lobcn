## String 字符串 

字符串的表示方法为单引号，双引号和三引号，字符串创建以后是不可更改的. 


    ''
    ""
    '''
    """
    

### 字符串的转义

所谓转义就是指让某个符号不再表示某个含义，而是表示另外一个含义。转义符



转义字符 | 描述 |
:-------|:-------|
 \ (在行尾时)|续行符号|
  \\  |反斜杠符号 |
 \'| 单引号|
 \" | 双引号|
 \a | 响铃 |
 \b | 退格 |
 \e | 转义 |
 \000 | 空 |
  \n | 换行 |
  \v | 纵向制表符 |
  \t | 横向制表符 |
  \r | 回车 |
  \f | 换行 |
  \oyy |   八进制数，yy代表的字符，例如：\012 代表换行 |
  \xyy | 十进制yy代表的字符，例如: \x0a 代表换行 |
  \ other | 其他的字符以普通格式输出 |


### String Method 

字符串可以被索引,第一个字符索引为0，索引也可以是复数，这将导致从右边开始计算

   ![](https://raw.githubusercontent.com/mklsw/python-learning/master/String/string_slices.png)


        print(help(str))
        
1. lower return a copy of the string S converted to lowercase

        S.lower 
        >>> string = "HOW ARE YOU ?"
        >>> print(string.lower())
        how are you ?
      
2. upper Return a copy of S converted to uppercase.

        S.upper
        >>> string = "how are you ?"
        >>> print(string.upper())
        HOW ARE YOU ?
        
        

3. slices 



copy

拼接

查找 find

统计

检测

切片


Reference:
https://docs.python.org/3/library/stdtypes.html#string-methods
https://developers.google.com/edu/python/strings
http://wiki.jikexueyuan.com/project/start-learning-python/106.html 
