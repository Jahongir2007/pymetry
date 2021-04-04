'''
    Author: Jahongir Sobirov
    License: MIT
    Version: 1.0.0
    All rights reserved 2021 (c)
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
