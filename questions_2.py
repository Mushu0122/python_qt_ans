"""1]. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']"""

list=['Red','Green','White','Black','Pink','Yellow']
list[1:4:]
print(list[1:4:])

"""2]. Check if a list contains an element
 ex li = [1,2,3,'a','b','c']
 check 'a'"""

li=[1,2,3,'a','b','c']
print("'a'is present in the li")


"""3] Difference between append and extend?
ex num1=[1,2,3]
   num2=[4,5,6]"""

num1=[1,2,3]
num1.append(4)
print(num1)

num2=[4,5,6]
num2.extend([7,8,9])
print(num2)

#4] Difference between del and clear?
"""del function  is used to remove the specific element from the structure and clear function is used to 
remove all the elements from the structure"""

#5] Difference between remove and pop?
#The remove() method removes the first occurrence of a specified value from the list.
#The pop() method removes and returns the element at the specified index from the list

#6] how to insert an item at given position ?
"""To insert an item at a given position in a list in Python, you can use the insert() method. 
The insert() method takes two parameters
: the index where you want to insert the item and the value you want to insert."""

#7] how to access elements of the list?
"""Indexing: You can access individual elements of a list by specifying the index of the element 
within square brackets []. Indexing in Python starts from 0 for the first element, 1 for the second 
element, and so on.
Slicing: You can access a range of elements from a list using slicing. Slicing allows you to specify 
a start index, an end index (exclusive), and an optional step size within square brackets """

#8] how to modify elements of the list ?
"""To modify elements of a list in Python, you can directly assign new values to the elements using indexing or slicing. Lists in Python are mutable,
 which means you can change their elements after they have been created."""

"""Here are a few ways to modify elements of a list:
using Indexing: You can modify a
 single element of the list by specifying its index and assigning a new value to it.
 Using Slicing: You can modify a range of elements using slicing and assignment.
  Using Methods: Some list methods can be used to modify elements. For example, the append(), 
  extend(), insert(), and remove() methods can add, remove, or modify elements of a list."""

 """9] how to concatenate of the list ?"""

"""To concatenate lists in Python, you can use the + operator or the extend() method. 
Both methods allow you to combine the elements of two or more lists into a single list.

Here's how you can concatenate lists using both methods:

Using the + Operator:
You can use the + operator to concatenate lists.
 It creates a new list containing elements from both lists.
 Using the extend() Method:
The extend() method is used to add elements
 from one list to the end of another list. It modifies the original list in place."""

 #10] how to convert python list to another data structures like set ,tuple,dictionary ?
 """Here's how you can convert
  a Python list to different data structures:

To Set:
Use the set() constructor to convert a list to a set.
 Sets contain unique elements, so duplicates in the list will be removed.

 To Tuple:
Use the tuple() constructor to convert a list to a tuple

To Dictionary:
Lists can be converted to dictionaries if the list contains nested lists with key-value pairs.
 Each nested list should have two elements: the key and the value."""


# 11] how to remove dublicate elements in list
"""To remove duplicate elements from a list in Python, you can use several approaches,
 including converting the list to a set, using a loop, or using list comprehension"""