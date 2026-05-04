Summary of my scores:

1. Modules and packages (67%)
2. Exceptions (36%)
3. Strings (72%)
4. OOP (88%)
5. Misc - list comprehensions, lambdas, closures, IO ops (50%)


1. Which of the platform module functions should be used to determine the underlying platform name?

A. platform.processor
B. platform.platform()
C. platform.uname()
D. platform.python_version()

Answer: C

2. A Python module named pymod.py contains a function named pyfun(). Which of the following snippets will let you invoke this function? (Select two answers):

A. import pyfun from pymod
pyfun()
B. from pymod import pyfun 
pyfun()
C. import pymod
pymod.pyfun()
D. from pymod import *
pymod.pyfun()

Answer: B, C


3. What is true about Python packages? (Select two answers):

A. A package is a single file whose name ends with the extension pa.
B. The pyc extension is used to mark semi-compiled Python packages.
C. A package is a group of related modules.
D. The __name__ variable always contains the name of the package.

Answer: B, C


4. With regards to the strucutre below, select the proper forms to import module_a (two answers):


pypack (dir)
- module_a.py (file)
- upper(dir) - module_b.py (file) - lower(dir) - module_c.py (file)


A. import pypack.module_a
B. from pypack import module_a
C. import module_a
D. import module_a from pypack

Answer: A, B


5. What is the expected output of the following code?

import sys
b1 = type(dir(sys)) is str
b2 = type(sys.path[-1]) is str
print(b1 and b2)

A. None
B. True
C. 0
D. False

Answer: B

6. Assuming the code has been executed successfuly, which of the following expressions will always evaluate to True? (Two answers)

import random
random.seed(1)
v1 = random.random()
random.seed(1)
v2 = random.random()

A. len(random.sample([1, 2, 3], 2)) > 2
B. v1 == v2
C. v1 >= 1
D. random.choice([1, 2, 3]) >= 1

Answers: B, D

7. Which is true about the following snippet? (Two answers)

Class E(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return "it's nice to see you"

try:
    print('I feel fine')
    raise E('what a pity')
except E as e:
    print(e)
else:
    print('the show must go on')

A. The code will output the following string: it's nice to see you
B. the code will raise an unhandled exception
C. the code will output the following string: I feel fine.
D. the code will output the following string: what a pity

Answer: D

Pominąłem chyba, że powinno być dwie i jeszcze I feel fine...

8. What is the expected behavior of the following code?

s = '2A'
try:
    n = int(s)
except:
    n = 3
except ValueError:
    n = 2
except ArithmeticError:
    n = 1
print(n)

A. It outputs 1.
B. It outputs 2.
C. The code is erroneous and it will not execute.
D. It outputs 3.

Answer: C

9. Which of the following snippets will execute with raising any unhandled exceptions (two answers)?

A. 
try:
    x = y + 1
except(NameError, SystemError):
    x = y + 1
else:
    y = x

B.
try:
    print(-1, 1)
except:
    print(0/1)
else:
    print(1/1)


C.
try:
    x = 1/0
except NameError:
    x = 1 / 1
else:
    x = x + 1

D.
try:
    x = 1
except:
    x = x + 1
else:
    x = x + 2


Answers:
A, D


10. What is the expected behavior of the following code?

m = 0

def foo(n):
    global m
    assert m != 0
    try:
        return 1/n
    except ArithmeticError:
        raise ValueError
    
try:
    foo(0)
except ArithmeticError:
    m += 2
except:
    m += 1
print(m)

A. It outputs 3.
B. It outputs 1.
C. The code is erroneous and it will not exceute.
D. It outputs 2.

Answer: C

11. What is the expected behavior of the following code?

d = {'1': '1', '2': '2'}
try:
    d['1'] = d['3']
except BaseException as error:
    print(type(error))

A. It outputs class KeyError.
B. The code is erroneous and it will not execute
C. It outputs class Exception.
D. It outputs class BaseException.

Answer: D

12. What is the expected behavior of the following code?

string = str(1/3)
dummy = ''
for character in string:
    dummy = dummy + character
print(dummy[-1])

A. It raises an exception.
B. It outputs 0.
C. It outputs 3.
D. It outputs None.

Answer: C

13. Assuming that the snippet below has been executed successfully, which of the following expressions will evaluate to True? (Two answers)

string = 'REPTILE'[:3:]
string = string[-1] + string[-2::-1]

A. string[0] < string[-1]
B. string[0] == 'E'
C. string is None
D. len(string) == 3

Answer: B, A

14. Which of the following expressions evaluate to True? (Two answers)

A. len("""""") == 0
B. len ('\'') == 1
C. ord('Z') - ord('z') == ord('0')
D. chr(ord('A') + 1) == 'B'

Answer: A, D

15. Which of the following statements are true? (Two answers)

A. II in ASCII stands for Information Interchange
B. \e is an escape sequence used to mark the end of lines
C. ASCII is the synonymous with UTF-8
D. A code point is a number assigned to a given character.

Answer: A, D

16. Which of the following expressions evaluate to True? (Two answers)

A. '1' + '2' * 2 != '12'
B. 'abc'.upper() < 'abc'
C. 3 * 'a' < 'a' * 2
D. 11 = '011'

Answer: A, B

17. Which of the following expressions evaluate to True? (Two answers)

A. 'phd' in 'alpha'
B. str(1-1) in '0123456789'[:2]
C. 'True' not in 'False'
D. 'dcb' not in 'abcde'[::-1]

Answer: B, C

18. Which of the following invocations are valid? (Two answers)

A. 'python'.find('')
B. 'python'.rindex('th')
C. sort('python')
D. 'python'.sorted()

Answer: A, C

19. What is the expected behavior of the following code?

the_string = ',,'.join(('alpha', 'omega'))
the_list = the_string.split(',')
print(',' in the_list)

A. Exception
B. Nothing
C. True
D. False

Answer: C

20. Assuming that the code below has been placed inside a file named code.py and executed successfully, which of the following expressions evaluate to True? (Two answers)

class ClassA:
    var = 1

    def __init__(self, prop):
        prop1 = prop2 = prop
    

class ClassB(ClassA):
    def __init__(self, prop):
        prop3 = prop ** 2
        super().__init__(prop)
    
Object = ClassB(2)

A. __name__ = '__main__'
B. ClassA.__module__ = 'ClassA'
C. str(Object) == 'Object'
D. len(ClassB.__bases__) == 1

Answer: A, D

21. Assuming that the snippet below has been executed successfully, which of the following expressions will evaluate to True? (Two answers)

class Class:
    var = data = 1

    def __init__(self, value):
        self.prop = value

Object = Class(2)

A. 'data' in Class.__dict__
B. len(Class.__dict__) == 1
C. 'data' in Object.__dict__
D. 'var' in Class.__dict__


Answer: A, D

22. What is the expected behavior of the following code?

class Class:
    Var = 0

    def __foo(self):
        Class.Var += 1
        return Class.Var

o = Class()
o.__Class_foo()
print(o.__Class_foo())

A. It outputs 1.
B. It raises an exception.
C. It outputs 3.
D. It outputs 6.

Answer: B

23. What is the expected behavior of the following code?

class Class:
    Var = 0

    def __init__(self, var):
        self.var = var
        Class.Var += 1

object_1 = Class(1)
object_2 = Class(2)
print(Class.Var + object_1.var + object_2.var)

A. It raises an exception
B. It outputs 5.
C. It outputs 2.
D. It outputs 3.

Answer: B

24. Assuming that the snippet below has been executed successfully, which of the following expressions will evaluate to True? (Two answers)

class A:
    __VarA = 1

    def get(self):
        return self.__VarA

class B(A):
    __VarA = 2

    def get(self):
        return self.__VarA

class C(B):
    __VarA = 3

obj_a = A()
obj_b = B()
obj_c = C()

A. hasattr(B, 'get')
B. obj_c.get() == 2
C. isinstance(obj_b, C)
D. C._C__VarA == 2

Answer: A, C


25. What is the expected output of the following snippet?

class Upper:
    def __init__(self):
        self.property = 'upper'

class Lower(Upper):
    def __init__(self):
        super().__init__()

Object = Lower()
print(isinstance(Object, Lower), end = ' ')
print(Object.property)


A. False lower
B. True lower
C. False upper
D. True upper

Answer: D

26. What is true about Object-Oriented Programming in Python?\

A. Each object of the same class can have a different set of properies.
B. Encapsulation allows you to hide a whole class inside a package.
C. The arrows on a class diagram are always directed from a superclass towards its subclass.
D. A class is a recipe for an object

Answer: A, D

27. Assuming that the following inheritance set is in force, which of the following classes are declared properly? (Two answers)

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass


A. class Class_4(D, A): pass
B. class Class_2(B, D): pass
C. class Class_1(C, D): pass
D. class Class_3(A, C): pass

Answer: A, C

28. What is the expected behavior of the following code?

class Super:
    def make(self):
        return 0
    
    def doit(self):
        return self.make()
    

class Sub_A(Super):
    def make(self):
        return 1

class Sub_B(Super):
    def make(self):
        return 2

a = Sub_A()
b = Sub_B()
print(a.doit() + b.doit())

A. Exception.
B. 3
C. 2
D. 1

Answer: B

29. What is the name of the attribute that stores information about a given class's super classes?

A. __bases__
B. __upper__
C. __super__
D. __ancestors__

Answer: C

30. What is true about Python class constructors? (Two answers)

A. The constructor is a method named __init__.
B. The constructor must return a value other than None.
C. The constructor must have at least one parameter
D. There can be more than one constructor in a Python class

Answer: A, C

31. Which of the following lines of code will work flawlessly when put independently inside the inc() method in order to make the snippet's output equal to 3? (Two answers)

class MyClass:
    Var = 0

    def __init__(self):
        MyClass.Var += 1
        self.prop = MyClass.Var

    def get(self):
        return self.prop
    
    def put(self, val):
        self.prop = val
    
    def inc(self, val):
    #insert the line of code here

Object = MyClass()
Object.inc(2)
print(Object.get())

A. self.put(self.prop + val)
B. self.put(get() + val)
C. put(self.prop + val)
D. self.put(self.get() + val)

Answer: A, D 

32. What is the expected behavior of the following code?

x = 8 ** (1 / 3)
y = 2. if x < 2.3 else 3.
print(y)

A. The code is erroneous and it will not execute.
B. 2.0
C. 2.5
D. 3.0

Answer: A

33. What is the expected output of the following code if the file named non_zero_length_existing_text_file is a non-zero length file located inside the working directory?

try:
    f = open('non_zero_length_existing_text_file', 'rt')
    spam = f.read(1)
    print(len(spam))
    f.close()
except IOError:
    print(-1)

A. An errno value corresponding to file not found
B. -1
C. 1
D. 0

Answer: C

34. What is true about lambda functions? (Two answers)

A. They are called anonymous functions.
B. They cannot return the None value as a result.
C. They can be defined without parameters.
D. They must contain the return keyword.

Answer: A, B 

35. Which of the followings statements are true? (Two answers)

A. The second open() argument describes the open mode and defaults to 'w'.
B. If open()'s second argument is 'r', the file must exist or open will fail.
C. Closing an opened file is performed by closefile() function.
D. If open()'s second argument is 'w' and the invocation succeeds, the previous file's contents are lost

Answer: A, B

36. What is the expected output of the following code?

def foo(x, y, z):
    return x(y) - x(z)

print(foo(lambda x: x % 2, 2, 1))

A. -1
B. 0
C. An exception is raised.
D. 1

Answer: C


37. Assuming that the snippet below has been executed successfully, which of the following expressions will evaluate to True? (Two answers)

def f(x):
    def get(x):
        return x * x
    
    return g


a = f(2)
b = f(3)

A. a == b
B. b(1) == 4
C. a is not None
D. a(2) == 4

Answer: A, D

38. What is the expected output of the following code?

myli = range(-2, 2)
m = list(filter(lambda x: True if abs(x) < 1 else False, myli))
print(len(m))

A. 4
B. 1
C. 16
D. An exception is raised

Answer: B

39. What is the expected behavior of the following code?

my_list = [i for i in range(5)]
m = [my_list[i] for i in range(4, 0, -1) if my_list[i] % 2 != 0]
print(m)

A. It outputs [4, 2, 0]
B. It outputs [1, 3]
C. The code is erroneous and it will not execute.
D. It outputs [3, 1]

Answer: B

40. What is the expected output of the following code if existing_file is the name of a file located inside the working directory?

try:
    f = open('existing_file', 'w')
    print(1, end = ' ')
except IOError as error:
    print(error.errno, end = ' ')
    print(2, end = ' ')
else:
    f.close()
    print(3, end = ' ')


A. 1 2 3
B. 2 3
C. 1 3
D. 1 2

Answer: C




