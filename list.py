# 1.list Defination ?
# answer:1.list is a ordered collection of the items.
#        2.list is a mutable.
#        3.list allows duplicate values.
# 2. why we use list?
# answer: 1. list store multiple items in a single variable.
#        2. Data can easily be acces and modified.
#        3. list to work with loops.
# 3. where we use list?
# answer:list are used in data processing,automation and report generating.

# 4. how many methods in list?
# answer: there are 10 methods in list.
# 1. append() - Adds an element at the end of the list
# 2. clear() - Removes all the elements from the list
# 3. copy() - Returns a copy of the list
# 4. count() - Returns the number of elements with the specified value
# 5. extend() - Add the elements of a list (or any iterable), to the end of the current list
# 6. index() - Returns the index of the first element with the specified value
# 7. insert() - Adds an element at the specified position
# 8. pop() - Removes the element at the specified position
# 9. remove() - Removes the first item with the specified value
# 10. reverse() - Reverses the order of the list
# 11. sort() - Sorts the list

# 1. first create a list then using append() method
num=[1,2,3,5,1,2]
print(num)  #output: [1, 2, 3, 5, 1, 2]
num.append(4)
print(num)  #output: [1, 2, 3, 5, 1, 2, 4]
 
# 2. first create a list then using clear() method
name=["parvati","shivam"]
print(name)  #output: ['parvati', 'shivam']
name.clear()
print(name)  #output: []

# 3. first create a list then using copy() method
name=["parvati","shivam"]
print(name)  #output: ['parvati', 'shivam']
name1=name.copy()
print(name1)  #output: ['parvati', 'shivam']

# 4. first create a list then using count() method
num=[1,2,2,3,4,4,4,4,2,2,23,3]
print(num)  #output: [1, 2, 2, 3, 4, 4, 4, 4, 2, 2, 23, 3]
b=num.count(4)
print(b)  #output: 4

# 5. first create a list then using extend() method
num=[1,2,3,4]
number=[4,5,6,7]
num.extend(number)
print(num)  #output: [1, 2, 3, 4, 4, 5, 6, 7]

# 6. first create a list then using index() method
num=[1,2,3,4]
a=num.index(3)
print(a)  #output: 2

# 7. first create a list then using insert() method
num=[1,2,3,4]
num.insert(2,5)
print(num)  #output: [1, 2, 5, 3, 4]

# 8. first create a list then using pop() method
num=[1,2,3,4]
num.pop(2)
print(num)  #output: [1, 2, 4]

# 9. first create a list then using remove() method
num=[1,2,3,4]
num.remove(2)
print(num)  #output: [1, 3, 4]

# 10. first create a list then using reverse() method
num=[1,2,3,4]
num.reverse()
print(num)  #output: [4, 3, 2, 1]

# 11. first create a list then using sort() method
num=[1,2,3,4]
num.sort()
print(num)  #output: [1, 2, 3, 4]