# set defination ?
# answer:1.set is a unordered collection of the items.
#        2.set is a mutable.
#        3.set does not allow duplicate values.
# 2. why we use set?
# answer: 1. set store multiple items in a single variable.
#        2. set is used to remove duplicate values.
#        3. set is used to perform mathematical operations.
# 3.how many methods in set?
# answer: there are 15 methods in set.
# 1. add() - Adds an element to the set
# 2. clear() - Removes all the elements from the set
# 3. copy() - Returns a copy of the set
# 4. difference() - Returns a set containing the difference between two or more sets
# 5. discard() - Remove the specified item
# 6. intersection() - Returns a set, that is the intersection of two other sets
# 7. issubset() - Returns whether another set contains this set or not
# 8. pop() - Removes an element from the set
# 9. remove() - Removes the specified element
# 10. union() - Return a set containing the union of sets
# 11. update() - Update the set with the union of this set and others

# 1.first create a set then using add() method
num={1,2,3,4,5}
print(num)  #output: {1, 2, 3, 4, 5}
num.add(6)
print(num)  #output: {1, 2, 3, 4, 5, 6}

#2.first create a set then using clear() method
num={1,2,3,4,5}
print(num)  #output: {1, 2, 3, 4, 5}
num.clear()
print(num)  #output: set()

#3.first create a set then using copy() method
num={1,2,3,4,5}
print(num)  #output: {1, 2, 3, 4, 5}
num_copy=num.copy()
print(num_copy)  #output: {1, 2, 3, 4, 5}

#4.first create a set then using difference() method
num={1,2,3,4,5}
number={2,3,4,2,1}
b=num.difference(number)
print(b)  #output: {5}

#5.first create a set then using discard() method
num={1,2,3,4,5}
print(num)  #output: {1, 2, 3, 4, 5}
num_discard=num.discard(2)
print(num_discard)  #output: None
print(num)  #output: {1, 3, 4, 5}

#6.first create a set then using intersection() method
num={1,2,3,4,5}
number={2,3,4,2,1}
c=num.intersection(number)
print(c)  #output: {1, 2, 3, 4}

#7.first create a set then using issubset() method
num={1,2,3,4,5}
number={2,3,4,2,1}
d=num.issubset(number)
print(d)  #output: False

#8.first create a set then using pop() method
num={1,2,3,4,5}
print(num)  #output: {1, 2, 3, 4, 5}
num_pop=num.pop()
print(num_pop)  #output: 1
print(num)  #output: {2, 3, 4, 5}

#9.first create a set then using remove() method
num={1,2,3,4,5}
print(num)  #output: {1, 2, 3, 4, 5}
num_remove=num.remove(2)
print(num_remove)  #output: None
print(num)  #output: {1, 3, 4, 5}

#10.first create a set then using union() method
num={1,2,3,4,5}
print(num)  #output: {1, 2, 3, 4, 5}
num_union=num.union({2,3})
print(num_union)  #output: {1, 2, 3, 4, 5}

#11.first create a set then using update() method
num={1,2,3,4,5}
print(num)  #output: {1, 2, 3, 4, 5}
num_update=num.update({2,3})
print(num_update)  #output: None
print(num)  #output: {1, 2, 3, 4, 5}

