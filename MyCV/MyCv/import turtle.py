import turtle

wn = turtle.Screen
rey = turtle.Turtle

size = int(input("please enter the size: "))
rey.color(input("please enter a color: "))

for i in range(4):
    rey.forward(size)
    rey.left(90)

wn.mainloop()