import turtle
import random
t = turtle.Turtle()

t.up()
t.goto(-100, 100)
t.down()
t.speed(0)
for i in range(15):
    t.write(i)
    t.rt(90)
    t.fd(120)
    t.bk(120)
    t.lt(90)
    t.fd(20)
    

t1 = turtle.Turtle()
t1.shape('turtle')
t1.color('gold')
t1.up()
t1.goto(-120, 80)

t2 = turtle.Turtle()
t2.shape('turtle')
t2.color('red')
t2.up()
t2.goto(-120, 50)

t3 = turtle.Turtle()
t3.shape('turtle')
t3.color('blue')
t3.up()
t3.goto(-120, 20)

#Болельщики
t4 = turtle.Turtle()
t4.shape('turtle')
t4.up()
t4.goto(-90, -40)
t4.speed(0)
r = random.randint(1, 10)
for i in range(r):
    t4.lt(90)
    t4.stamp()
    t4.rt(90)
    t4.fd(20)
t4.goto(10000, 10000)





x1 = 0
x2 = 0
x3 = 0
win = input("Какая черепаха победит:")
text = turtle.Turtle()
text.up()
text.goto(-120,120)
text.write("Ты считаешь, что победит " + win)
while True:
    if x1 == 305:
        break
    if x2 == 305:
        break
    if x3 == 305:
        break
    
    step1 = random.randint(1, 5)
    t1.fd(step1)
    x1 = x1 + step1

    step2 = random.randint(1, 5)
    t2.fd(step2)
    x2 = x2 + step2

    step3 = random.randint(1, 5)
    t3.fd(step3)
    x3 = x3 + step3

