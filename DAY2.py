#List
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))

#Methods
print(len(my_list))

my_list.append(6)  # is used to add an element to the end of the list
print(my_list)

my_list.insert(0, 0)  # is used to add an element at a specific index
print(my_list)  

my_list.extend([7, 8, 9])  # is used to add multiple elements to the end of the list
print(my_list)

my_list.remove(3)  # is used to remove the first occurrence of a specific element
print(my_list)

my_list.pop()  # is used to remove the last element from the list
print(my_list)

#Properties

#ORDERED and mutable
my_list[7]= 10  # is used to change the value of an element at a specific index
print(my_list)

#dUPLICACY AND HETEROGENEITY
FUN=[1,2,3,4,12,1,2,True,False,"Hello"]
print(FUN)

## Tuple
abc = (1, 2, 3, 4, 5)
print(abc)
print(type(abc))

#Set
my_set = {1, 2, 3, 4, 5}

# dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

# string
my_string = "Hello, World!"