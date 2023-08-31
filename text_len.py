"""Task

Write a program that detects if a string has an even/odd 
number of characters and prints "even" or "odd" accordingly.
"""

text = input('Enter any words or text: ')

if len(text) % 2 == 0:
    print(f'"{text}"  -->  "even"')
else:
    print(f'"{text}"  -->  "odd"')

print(len(text))