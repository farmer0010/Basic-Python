import turtle
import random
import sqlite3
import math

con = sqlite3.connect("turtleDB")
cur = con.cursor()

try:
    cur.execute("CREATE TABLE turtleList (선분ID int(6), 색상R float(8), 색상G float(8), 색상B float(5), 순번 INT(6), X좌표 int(6), Y좌표 int(6))")

except:
    cur.execute("DROP TABLE turtleList")
    cur.execute("CREATE TABLE turtleList (선분ID int(6), 색상R float(8), 색상G float(8), 색상B float(5), 순번 INT(6), X좌표 int(6), Y좌표 int(6))")
con.commit()

global r
global g
global b
swidth, sheight, pSize, exitCount = 300, 300, 3, 0
angle, dist, curX, curY = 0, 0, 0, 0

turtle.title("거북이가 맘대로 다니기(DB)")
turtle.shape("turtle")
turtle.pensize(pSize)
turtle.setup(width = swidth + 30, height = sheight + 30)
turtle.screensize(swidth, sheight)

idnum = 1
num = 1

while True:
    global num1
    global num2

    r = round(random.random(), 1)
    g = round(random.random(), 1)
    b = round(random.random(), 1)
    turtle.pencolor((r,g,b))

    angle = random.randrange(0, 360)
    dist = random.randrange(1, 100)
    turtle.left(angle)
    turtle.forward(dist)
    curX = round(turtle.xcor())
    curY = round(turtle.ycor())
    sql = "INSERT INTO turtleList VALUES('" + str(idnum) + "','" + str(r) + "','" + str(g) + "','"  + str(b) + "','" + str(num) + "','" + str(curX) + "','" + str(curY) + "')"
    num += 1;

    if(-swidth/2 <= curX and curX <= swidth/2) and (-sheight/2 <= curY and curY <= sheight/2):
        pass

    else:
        if exitCount < 5:
            num1 = round(turtle.xcor())
            num2 = round(turtle.ycor())
            turtle.penup()
            turtle.goto(0, 0)
            idnum += 1
            num = 1
            turtle.pendown()
            exitCount += 1
            
        if exitCount >= 5:
            break
    
    cur.execute(sql)
    
turtle.clear()

sql = "SELECT * FROM turtleList WHERE 선분ID = 5"
cur.execute(sql)
rows = cur.fetchall()
turtle.penup()
turtle.pencolor(r,g,b)
turtle.goto(num1, num2)
turtle.pendown()
turtle.goto(rows[len(rows)-1][5], rows[len(rows)-1][6])

print("----------------------------------------------------------")

cur.execute("SELECT * FROM turtleList")
while True:
    row = cur.fetchone()

    if row == None:
        break;

    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    data5 = row[4]
    data6 = row[5]
    data7 = row[6]
    print("%6d %5s %5s %5s %5s %5s %5s" % (data1, data2, data3, data4, data5, data6, data7))

for i in range(idnum-1, -1, -1):
    sql = "SELECT * FROM turtleList WHERE 선분ID = ('" + str(i) + "')"
    cur.execute(sql)
    rows = cur.fetchall()
    turtle.penup()
    for g in range(len(rows)-1, -1, -1):
        turtle.goto(rows[g][5], rows[g][6])
        turtle.down()
        turtle.pencolor((rows[g][1], rows[g][2], rows[g][3]))

    turtle.goto(0,
                
