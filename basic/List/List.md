## List 

Python has a great built-in list type named "list".List literals are writen with square brackets[ ].
Lists work similarly to strings--use the len ( ) function and square brackets [ ] to access data,with
the first element at index 0.

    colors = ['red', 'blue', 'green']
    print(colors[0])  ## red
    print(colors[2])  ## green
    print(len(colors))  ## 3
    
![list index](https://raw.githubusercontent.com/mklsw/python-learning/master/Python%20Data%20Type/List/list1.png)
    
### List Methods

1. append   

        list.append(object) ----append object to the end

2. insert   

        list.insert(index.object) --- insert object before index

3. index 

        list.index(vlaue,[start,[stop]]) ---return first index of value.
4. pop   

        list.pop([index]) --- remove and return item at index (default last)
        
5. remove 

        list.remove((value))---remove first occurrence of value
        


Reference：
1. https://docs.python.org/3.7/library/stdtypes.html#list

2. https://developers.google.com/edu/python/lists 

    
    


