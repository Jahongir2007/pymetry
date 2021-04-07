'''
    Author: Jahongir Sobirov
    Pymetry python library
    License: MIT
    Version: 1.1.0
'''
import turtle
pymetry = turtle.Turtle()
def square(distance, color, bold):
    pymetry.color(color)
    pymetry.pensize(bold)
    pymetry.forward(distance)
    pymetry.right(90)
    pymetry.forward(distance)
    pymetry.right(90)
    pymetry.forward(distance)
    pymetry.right(90)
    pymetry.forward(distance)
    pymetry.right(90)
def rect(distancer, color, bold):
    pymetry.color(color)
    pymetry.pensize(bold)
    pymetry.right(90)
    pymetry.forward(distancer)
    pymetry.left(90)
    pymetry.forward(distancer)
def circle(distance, color, bold):
    pymetry.color(color)
    pymetry.pensize(bold)
    pymetry.circle(distance)
def corner(angle, distance, color, bold):
    pymetry.color(color)
    pymetry.pensize(bold)
    pymetry.right(angle)
    pymetry.forward(distance)
    pymetry.left(angle)
    pymetry.forward(distance)
def triangle(a, b, distance, color, bold):
    pymetry.color(color)
    pymetry.pensize(bold)
    pymetry.forward(distance) 
    pymetry.left(a)
    pymetry.forward(distance)
    pymetry.left(b)
    pymetry.forward(142)
def trsize(a, b, c):
    pymetry.shapesize(a, b, c)
def pentagon(distance, color, bold):
    pymetry.color(color)
    pymetry.pensize(bold)
    for i in range(5):
        pymetry.forward(distance)
        pymetry.right(72)
def hexagon(distance, color, bold):
    pymetry.color(color)
    pymetry.pensize(bold)
    for i in range(6):
        pymetry.forward(distance)
        pymetry.right(60)
def heptagon(distance, color, bold):
    pymetry.color(color)
    pymetry.pensize(bold)
    for i in range(7):
        pymetry.forward(distance)
        pymetry.right(51.42)
def octagon(distance, color, bold):
    pymetry.color(color)
    pymetry.pensize(bold)
    for i in range(8):
        pymetry.forward(distance)
        pymetry.right(45)
def polygon(color, bold):
    pymetry.color(color)
    pymetry.pensize(bold)
    n = int(input("Enter the no of the sides of the polygon : "))
    l = int(input("Enter the length of the sides of the polygon : "))
    for i in range(n):
        pymetry.forward(l)
        pymetry.right(360 / n)
def adjaccor(first_cor, second_cor):
    if first_cor == "unknown":
        value = 180 - second_cor
        print(value)
    elif second_cor == "unknown":
        value = 180 - first_cor
        print(value)
    else:
        print("Not unknowns!")
def valtri(a, b, c):
    if a == 'unknown':
        value = 180 - b - c
        print(value)
    elif b == 'unknown':
        value = 180 - a - c
    elif c == 'unknown':
        value = 180 - a - b
    else:
        print("Not unknowns!")
def perm(a, b):
    value = a + a + b + b
    print(value)
def sqside(a, b, per):
    if a == "unknown":
        value = (per - 2 * b) / 2
        print(value)
    elif b == "unknown":
        value = (per - 2 * a) / 2
        print(value)
    else:
        print("Not unknowns!")
def pert(a, b, c):
    value = a + b + c
    print(value)
def trside(a, b, c, per):
    if a == "unknown":
        value = per - c - b
        print(value)
    elif b == "unknown":
        value = per - a - c
        print(value)
    elif c == "unknown":
        value = per - a - b
    elif per == "unknown":
        print("Error!")
    else:
        print("Not unknowns!")
def aboutme():
    print("Pymetry python library. Author: Jahongir Sobirov.License: MIT. Version: 1.1.0")
