# A Python code that accepts the lengths of the two perpendicular sides of a right angled triangle, and calculates the hypotenuse length to 4 decimal places.

import math
b = int(input('Enter the base of the right angled triangle :- '))
h = int(input('Enter the height of the right angled triangle :- '))
Hypotenuse = math.sqrt((b*b)+(h*h))
print('The length of the hypotenuse of the right angled triangle is ','%.4f'%Hypotenuse)
