# Variable
# Defination of variable
# ans:Variable is name that refers to the address of the memory location where store the value.
# 2.why use the variable 
# ans:Variables are used because where the data is stored in the memory,the value of the variable is taken.
# 3. How is a variable stored in memory?
#ans:Values ​​are stored in memory as objects.

x=10   # x is variable and 10 is value
print(x)
#output: 10

num=20
print(num)
#output: 20
# in memory how to store the value
#Memory:
#[10]  ← object
#x ----> 10  is int type 

num=30  #same variable me different value store karenge toh pehle wala value override ho jayega
print(num)
#output: 30

name="parvati"  # ye variale me string value store kiya gaya hai
print(id(name))
#output: (parvati) 1970972398656  ye id hai memory me jaha par value store kiya gaya hai




##  DATA TYPES ##
#Defination of data types
# ans :data types is defined which kind of value is stored in the memory .

num=10     # dono ka variable name same hai but value different memory location par store hua hai 
print(id(num))  # mean ki number inmutable hai sab variable hone par bhi diffrenet memory use karega 
# output: 140733796087192

num=20      # dono ka variable name same hai but value different memory location par store hua hai 
print(id(num))  # mean ki number inmutable hai same variable hone par bhi diffrenet memory use karega ..
# output: 140733796087512

a="parvati"  # dono ka value same hai different variable hai toh memory location same hoga
print(id(a))  # different variable hai memory ka  address same rahega a variable bhi use value 
              # ko memory se le kar aayega aur b variable bhi wahi memory se value le kar aayega .
#output:2357269107776


b="parvati"  # dono ka value same hai different variable hai toh memory location same hoga.
print(id(b))  # different variable hai memory ka  address same rahega a variable bhi use value 
              # ko memory se le kar aayega aur b variable bhi wahi memory se value le kar aayega .
#output:2357269107776
# varible diffrent hone par memory location diffrent nhi ager value same hai to same address rahega .


a = 10        # int
b = 10.5      # float
c = 2 + 3j    # complex
print(type(a))
print(type(b))
print(type(c))
#output: <class 'int'>   interger value store kiya hai memory me 

name="parvati"
print(type(name))
#output: <class 'str'>   string value store kiya hai memory me 

# there are the two types of data types:
# 1.Mutable  ->  jo value change ho sake 
# 2.Immutable  ->  jo value change nahi ho sake 
# In mutable data type list
# dict
# set are mutable


# In immutable data type int
# float,
# bool
# str
# tuple are immutable
