# Some problems on list 

# Section 1 
# Store a apples stock price of 5 days and answer 
stock = [298,305,320,301,292]

#1 ) What was the price on Day 1?
print(stock[0])

#2 ) What wast the price on Day 3?
print(stock[2])

#3 ) On what day price was 301 ?

for i in range(len(stock)):
  if stock[i] == 301:
    print(i)
    
#4 ) print all prices
for i in stock:
  print(i)
  print("---")
  
#5) Insert new price 284 at index 1
stock.insert(1,284)
print(stock)

#6) Delete all element at index 1
stock.pop(1)
stock.remove(1)
print(stock)