# 1.tuple Defination ?
# answer:1.tuple is a ordered collection of the items.
#        2.tuple is a immutable.
#        3.tuple allows duplicate values.
# 2. why we use tuple?
# answer: 1. tuple store multiple items in a single variable.
#        2. Data can easily be acces.
#        3. tuple to work with loops.
# 3.how many methods in tuple?
# answer: there are 2 methods in tuple.
# 1. count() - Returns the number of times a specified value occurs in a tuple
# 2. index() - Searches the tuple for a specified value and returns the position of where it was found

# 1. first create a tuple then using count() method
tuple1=(1,2,3,4,5,6,7,8,9,10)
print(tuple1)  #output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
a=tuple1.count(5)
print(a)  #output: 1

# 2. first create a tuple then using index() method
tuple1=(1,2,3,4,5,6,7,8,9,10)
print(tuple1)  #output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
a=tuple1.index(5)
print(a)  #output: 4