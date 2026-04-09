#1.defination of the class
# ans: class is a blue print of the object which is used to create the object and it is a user defined data type.
# 2.why use the class
# ans: class is used to create the object and it is a user defined data type.and do not repate code again and again we can use class to create object and we can use the object to access the data and function of the class.
#  3. how to create a class
# ans: there is 5 mean point in the class.
#1. class is bluprint of the object that is real data holder.
#2.__init__ is a constructor which is used to initialize the object and it is called when the object is created.and inii run automatically when the object is created.
#3. self is a parameter which is used to refer the current object and it is used to access the data and function of the class.
#4. object is an instance of the class and it is used to access the data and function of the class.
#5. method is a function which is defined inside the class and it is used to perform the action on the data and it is used to access the data and function of the class.

class Student:
    school="yogiraj" # class variable these the comman object that is delcared in the class and it is shared by all the object of the class.
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Roll No:",self.rollno)
s1=Student("parvati",20,101)
s1.display()
print("School:",Student.school)