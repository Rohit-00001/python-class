# polymorphism: the word is derived from the Greek words "poly" meaning many and "morph" meaning form. In programming, polymorphism allows objects of different classes to be treated as objects of a common superclass. It is a core concept in object-oriented programming (OOP) that enables methods to do different things based on the object it is acting upon.

# --> method overloading  X
# --> method overriding

# Method Overloading: when a class having two or more methods with same name but different parameters (different type or number of parameters)

# class Python:
#     def Metthod1(self, a, b):
#         print("Method with two parameters:", a, b)

#     def Method1(self, a):
#         print("Method with one parameter:", a)

# ob = Python()
# # ob.Method1(10, 20)  # Calls the method with two parameters
# ob.Method1(10)      # Calls the method with one parameter



# Method Overriding: when two class having is a relationship and the child class has a method with the same name as in the parent class, the child class method overrides the parent class method.

# class Animal:
#     def speak(self,name):
#         print(f"{name}Animal speaks")

# class Cat(Animal):
#     def speak(self,name):
#         print(f"{name} Cat meows")
#         super().speak(name)  # Calls the parent class method


# ob = Cat()
# ob.speak("kitty")  # Calls the overridden method in the Cat class




# ----------------------------------
# Encapsulation: it is a mechanism of wrapping the data (variables) and code acting on the data (methods) together as a single unit. It restricts direct access to some of an object's components, which can prevent the accidental modification of data. Encapsulation is one of the fundamental principles of object-oriented programming (OOP).

# class Encap:
#     _var = 10 # Protected variable
#     __var2 = 20 # Private variable

#     def access(self):
#         print("Accessing protected variable:", self._var)
#         print("Accessing private variable:", self.__var2)

# en = Encap()
# print(en._var)
# print(en.__var2)

class Animal:

    _weight = 10  # Protected variable
    __height = 20  # Private variable

    def __init__(self,name, age):
        self._name = name
        self.__age = age

    def speak(self,sound):
        # print(f"{self._name} says {sound}")
        print(f"{self._name}")
        print(f"{self.__age} years old")
        print(sound)
        print(f"__height: {self.__height}")

class Dog(Animal):
    def speak(self,sound):
        # print(f"{name} Dog barks")
        print(sound)
        super().speak(sound)

    
ob = Dog("Buddy", 5)
ob.speak("woof")
print(ob._weight)
# print(ob.__height)
# print(ob.self.__age)  # This will raise an AttributeError because __age is private

ob2 = Animal("Kitty", 3)
# print(ob2.self.__age)
# print(ob2.__height)  # This will raise an AttributeError because __height is private