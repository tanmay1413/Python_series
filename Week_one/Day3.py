""" 
Today we learn Extraction of Digits . 

"""
"""
#--- Count of DIGITS 

n = 5873

# step 1 do not chage original value for best practice
num = n

# step 2 write your logic
count = 0

while num > 0:
  count += 1
  num = num // 10

print("The count is :", count)


"""
#--- Number palindrome or not
 
number = 12321

num = number
result = 0

while num > 0:
  last_digit = num % 10 
  result = (result *10) + last_digit
  num //= 10
  

print("number is palindrome" if number == result else "not palindrome") 



