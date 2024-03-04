#qt 1] print your name in python
name='Mohammad Mushraf Uddin'
print(name)
#qt 2 Calculate the multiplication and sum,division, of two numbers
a=2
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
"""qt 3] Print characters from a string that are present at an even index number
       str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’."""
str="pynative"
str[0:7:2]
print(str[0:7:2])
"""qt 4] Write a program to find how many times substring "Emma" appears in the given string.
     str_x = "Emma is good developer. Emma is a writer" """
str_x="Emma is good developer. Emma is a writer"
print(str_x.count("Emma"))
#qt 5] Create a  list take any example
li=[1,2,3,4,5]
print(li)
#qt 6] ex=[7,5,3,6] reverse list o/p=[6,3,5,7]
ex=[7,5,3,6]
ex[::-1]
print(ex[::-1])

#qt 7] l=[1,2,'a','b',7,9] find length of list 
l2=[1,2,'a','b',7,9]
print(len(l2))

#qt 8] l=[1,2,'a','b',7,9] remove 'a'
l3=[1,2,'a','b',7,9]
l3.remove('a')
print(l3)

#qt 9] l=[1,2,100,300,'abc',90]  add 100

l4=[1,2,100,300,'abc',90]
l4.append(100)
print(l4)

"""qt 10] Reverse words in given string 
                  str="python" 
                 output ="nohtyp" """
str="python"
string1=str[::-1]
print(string1)

"""qt 11] find length of string     
             str="python language" """

str="python language"
print(len(str))

"""qt 12] find size of tuple 
             tp=('a','b','c','d','k')"""

tp=('a','b','c','d','k')
size_of_tuple =len(tp)
print(len(tp))

#qt 13]  d={'name':'john','age':21,'city':'London'} find only keys  and find values of Dictionary 

d={'name':'john','age':21,'city':'London'}

keys_of_d = d.keys()
print("Keys of the dictionary:", keys_of_d)

values_of_d = d.values()
print("Values of the dictionary:", values_of_d)

"""qt 14] d={'name':'john','age':21,'city':'London'} 
            output= 'john' """
d={'name':'john','age':21,'city':'London'}
name='john'
print(name)

"""qt 15] create empty Dictionaries and add two keys with values pairs
             output= {'a':1,'b':3}"""

my_dict = {}


my_dict['a'] = 1
my_dict['b'] = 3

print(my_dict)

"""qt 16] find length of Dictionary 
                ex 
                 thisdict = {
                    "brand": "Ford",
                    "electric": False,
                    "year": 1964,
                    }"""

thisdict={"brand":"Ford","electric":"False","year":"1964"}
print(len(thisdict))

"""qt 17] Removing Items from Dictionary
   ex  
                thisdict = {
                     "brand": "Ford",
                     "model": "Mustang",
                     "year": 1964
                   }"""
thisdict1={"brand":"Ford","model":"Mustang","year":"1964"}
thisdict1.pop("brand")
thisdict1.pop("model")
thisdict1.pop("year")
print("removing items from dictionary:", thisdict1)

"""qt 18] compare two values using Comparison operators,Logical operators,Identity operators ?
            x=80
            y=40"""
x = 80
y = 40

# Comparison operators
print("Comparison operators:")
print("x > y:", x > y)   
print("x < y:", x < y)   
print("x == y:", x == y)  
print("x != y:", x != y)  
print("x >= y:", x >= y)  
print("x <= y:", x <= y)  
# Logical operators
print("\nLogical operators:")
print("x > 50 and y < 50:", x > 50 and y < 50)    
print("x > 50 or y < 50:", x > 50 or y < 50)
print("not(x > 50 and y < 50):", not(x > 50 and y < 50)) 
# Identity operators
z = 80
print("\nIdentity operators:")
print("x is y:", x is y)  
print("x is z:", x is z)  
print("x is not y:", x is not y)  

#qt 19] how to comments work in python use single line comment,Multiline Comments comments

#single line can be commented by using #
#multiple line can be commented by using """ at the start and end of the line.

# Define examples of different types
example_list = [1, 2, 3, 4, 5]
example_numbers = 12345
example_float = 3.14
example_string = "Hello, world!"
example_bool = True
example_none = None
example_dict = {"key": "value"}
example_set = {1, 2, 3, 4, 5}
example_tuple = (1, 2, 3, 4, 5)

# Print the types of each example
print("Type of example_list:", type(example_list))
print("Type of example_numbers:", type(example_numbers))
print("Type of example_float:", type(example_float))
print("Type of example_string:", type(example_string))
print("Type of example_bool:", type(example_bool))
print("Type of example_none:", type(example_none))
print("Type of example_dict:", type(example_dict))
print("Type of example_set:", type(example_set))
print("Type of example_tuple:", type(example_tuple))

"""qt 21] li=[4,5,6,7,8,9,10,11,12,13] use slicing 
                 o/p=[4, 6, 8, 10, 12]"""
li=[4,5,6,7,8,9,10,11,12,13]
li[::2]
print(li[::2])




"""qt 22 ] li=[4,5,6,7,8,9,10,11,12,13] use slicing
                o/p=[5, 7, 9, 11, 13]"""
li1=[4,5,6,7,8,9,10,11,12,13]
li1[1::2]
print(li[1::2])

"""qt 23] str= "Python Tutorial" convert str into list
                o/p=['python','Tutorial']"""
str="Python Tutorial"
result_list = str.split()
print(result_list)




