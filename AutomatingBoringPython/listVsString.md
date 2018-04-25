# Difference between string and list (Python)

1. String are immutable, list is mutable.

2. List assignment is different than variable assignment

3. !!! When you assign a variable of a list to another variable, the variable is actually a reference (pointer) to the original list so when you
   change something from the list with the new assignment variable, you're actually mutating the original list.

Ex:
```python
spam = [1,2,3] #spam is also a pointer/reference to the list
cheese = spam
cheese[1] = 'Hello!'
>>>cheese
[1,'Hello!',3]
>>>spam
[1,'Hello!',3]

#                                 _________________
#spam -------[reference]-------> [ list in memory ]
#cheese -->[spam]--[reference]-> [ list in memory ]
#                                [________________]

```

> Python does this because if we have a very long list (millions and billions),
> it can be costly to copy that list over every time you make assignment/method call/function call
> so as default python provide this cheap, easy to handle list reference

---

* So a solution to when you do need to copy a list over, there is a copy build in module 'import copy' -> 'cheese = copy.deepcopy(spam)'
* Another way is to use slicing b/c slicing will make a new copy of an array/list.
* This is the same for dictionary, only tuples and strings are immutable.
