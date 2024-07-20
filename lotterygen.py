import random
amount = input ("How many numbers would you like?")
numbers=[]
for i in range (1,100):
  numbers.append(i)
chosen_number=random.choice(numbers)
