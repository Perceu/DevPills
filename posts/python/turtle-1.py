"""
Criando sua primeira animação com turtle

"""
from turtle import Screen, Turtle

screen = Screen()
screen.setup(720, 720)
screen.colormode(255)
screen.bgcolor('black')
tl = Turtle()
tl.pencolor('white')
tl.speed(1)
for _ in range(8):
    for _ in range(4):
        tl.fd(150)
        tl.left(90)
    tl.left(45)

screen.mainloop()