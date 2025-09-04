#1.1
name = "Miranda"
age = 28
height = 5 + 3 / 12
favorite_color = 'green'

#1.2
print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)

print(f'Hello, my name is {name}. I am {age} years old, and I am {height} feet tall.')

import math
a = 4
b = 9
c = math.sqrt(a**2 + b**2)
print(c)
print(f'{c:.2f}')
c_int = (int(c))
print(f' {c_int:050d}')

print(f"""
      name: {name}
      age: {age}
      height: {height}
      favorite color: {favorite_color}
""")

#1.3
r = 5
circle_area = math.pi * r**2
print(f' {circle_area: .1f}')

#2.0
sqrt_age = math.sqrt(age)
print(sqrt_age)

sin_h = math.sin(height)
cos_h = math.cos(height)
print(sin_h, cos_h)

#3.0
sum = age + 5
difference = height - 4
product = age * height
quotient = height / 2
remainder = age // 3
power = age ** 2
print(f"""
    age + 5 = {sum} 
    height - 4 = {difference}
    age * height = {product}
    height / 2 = {quotient}
    age // 3 = {remainder}
    age **2 = {power}
    """)

#4.0
fahrenheit = input('Enter degrees Fahrenheit: ')
fahrenheit_in = fahrenheit
## input fuctions makes whatever the input a string, even if it is a number
celcius = round(((float(fahrenheit) - 32) * 5/9), 1)
celcius_str = str(celcius)
degree = str(chr(176))

print('The input of ' + fahrenheit_in + degree + 'F,  yields ' + celcius_str +degree +'C')


#input practice
#x = input('enter your name:')
#print('hello,' + x)



