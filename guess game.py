import random 
import pygame
number = random.randint(1,50)

print('guess the number(1,50)')
print('you have 5 chances')

for i in range(5):
   guess = int(input('enter your guess:'))

   if guess == number:
     print('your win!')
     break
   
   elif guess > number:
       print('too high')
   
   else:
       print('too low')

else:
    print('you lost')
    print('number was:',number)