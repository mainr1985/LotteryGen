import random
amount = int(input ("Quantos números você deseja?"))
numbers=[]
number=[]
for i in range (1,100):
  numbers.append(i)
for _ in range (1, amount+1):
  chosen_number=random.choice(numbers)  
  number.append(chosen_number)
print (*number, sep="-") #imprime tudo de chosen_number em uma mesma linha, separando por "-"