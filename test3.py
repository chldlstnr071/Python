import turtle

wn = turtle.Screen()
wn.title('test3')
wn.setup(500, 500)

t1 = turtle.Turtle()

t1.penup()
t1.goto(0, -100)
t1.pendown()
t1.circle(100)

for i in range(4):
    t1.penup()
    t1.home()
    t1.left(90+30*i)
    t1.forward(100)
    t1.left(150)
    t1.pendown()
    t1.forward(100*(3**(1/2)))
    t1.left(120)
    t1.forward(100*(3**(1/2)))
    t1.left(120)
    t1.forward(100*(3**(1/2)))



wn.mainloop()