#  Day 1: Data Types & Variables
# Basic data types: int, float, str, bool
# Integers: whole numbers, e.g. 1, 2, 3
a = 5
print("a = ",a, type(a))

# Floats: decimal numbers, e.g. 3.14, -0.5
b = 5.68
print("b = ",b, type(b))
# Strings: sequences of characters, e.g. "hello", 'hello'
c = "Tanmay"
print("c = ",c, type(c))

# Booleans: true or false values
print(True if type(c) == str else False)  
  
# Collections: list, tuple, set, dict
# Lists: are ordered, mutable collections that can hold items of different data types., e.g. [1, 2, 3] , e.g. [1,1,2,3,"four",5.5,True]
nums = [10, 20, 30, 40, 50]
# Task 1:
# a. Add 60 to the end
nums.append(60)
print(nums)
# b. Insert 25 at index 2
nums.insert(2,25)
print(nums)
# c. Remove 40
nums.remove(40)
print(nums)
# d. Print the list in reverse order
nums.reverse()
print(nums)

colors = ['red', 'green', 'blue', 'yellow']
# Task 2:
# a. Change 'green' to 'purple'
colors[1] = "purple"
print(colors)
# b. Print the second and third colors
print(colors[1:3])

# Task 3: Write a program to find the sum of all elements in the list
nums = [5, 10, 15, 20]
print("sum of list :",sum(nums))


# Task 4: Count the number of even and odd elements in the list
lst = [10, 21, 4, 45, 66, 93,89]
even = 0
odd = 0
for i in lst:
  if i % 2 == 0:
    even += 1
  else:
    odd+=1
print("Even count : ", even)
print("Odd count : ", odd)

# Task 5: Remove duplicates from the list
nums = [1, 2, 2, 3, 4, 4, 5]
# approch 1
duplicate = []
for i in nums:
  if i in duplicate:
    continue
  duplicate.append(i)
  
print(duplicate) 
# apporach 2
nums = list(set(nums))
print("Unique list : ",nums)
    
    
   