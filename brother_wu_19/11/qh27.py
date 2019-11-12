#import os  #导入，操作系统
import turtle  #画图，奥运五环
#os.system("mspaint")
#os.system("task kill /f /im mspaint.exe")
#os.system("ipconfig")

# turtle.color("blue")#蓝色
# turtle.circle(100)#半径100
# turtle.done()    #程序继续进行

#
# turtle.penup()
# turtle.goto(-200,0)
# turtle.pendown()
# turtle.color("red")#蓝色
# turtle.circle(100)#半径100
#
# turtle.done()    #程序继续进行
import turtle as t

t.showturtle() # 打开turtle绘图窗口
t.pensize(7)
# 画中心的黑色圆圈
t.color("black")
t.circle(50)
t.penup()
t.goto(120, 0)
t.pendown()
# 画红色圆圈
t.color("red")
t.circle(50)
t.penup()
t.goto(-120, 0)
t.pendown()
# 画蓝色圆圈
t.color("blue")
t.circle(50)
t.penup()
t.goto(-60, -50)
t.pendown()
# 画橙色圆圈
t.color("orange")
t.circle(50)
t.penup()
t.goto(60, -50)
t.pendown()
# 画绿色圆圈
t.color("green")
t.circle(50)
t.done()