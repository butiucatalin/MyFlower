import turtle

def desen_petala(t, d, u):
    t.speed(100)
    t.rt(u/2)
    for i in range(0, 2):
        t.fd(d)
        t.lt(u)
        t.fd(d)
        t.lt(180-u)
    t.lt(u/2)

def desen(n,deflection):

    assert 360.0/n == int(360.0/n)

    window = turtle.Screen()
    window.bgcolor("blue")

    F = turtle.Turtle()
    F.color("red","yellow")
    F.pensize(2)
    F.shape("circle")
    F.rt(deflection)

    for i in range(0, n):
        desen_petala(F, 100, 45)
        F.lt(360/n)
    F.lt(deflection)

    F.color("orange","yellow")
    F.rt(90)
    F.pu()
    F.fd(10)
    F.pd()
    F.lt(90)
    F.pensize(4)
    F.begin_fill()
    F.circle(10)
    F.end_fill()

    F.rt(90)
    F.color("green")
    F.fd(400)
    F.ht()

    window.exitonclick()

desen(36,45)
    
    
