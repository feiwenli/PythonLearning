# -*- coding = utf-8 -*-
import turtle
from time import sleep
from random import randint
turtle.setup(width=500, height=500)
t = turtle.Pen()    # 新建一个空白画布

for x in range(4):
    t.forward(50)
    t.left(90)
t.reset()   # 擦除画布，把海龟放到开始的位置
# t.clear()   # 清除屏幕，海龟仍在原位
t.up()  # 将笔从纸上抬起来
t.down()    # 将笔放下，即开始作画
t.backward(100)     # 向后画
t.reset()

# 对角线
t.up()
t.goto(-250, 250)
t.down()
t.goto(500, -500)

# 三角形
for x in range(3):
    t.forward(100)
    t.left(120)
t.reset()
# 没有角的方格
for x in range(4):
    t.forward(80)
    t.up()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.down()
# 八角星
t.reset()
for x in range(1, 9):
    t.forward(100)
    t.left(225)
# 螺旋星
t.reset()
for x in range(1, 38):
    t.forward(100)
    t.left(175)
t.reset()
for x in range(1, 20):
    t.forward(100)
    t.left(95)
# 星星
t.reset()
for x in range(1, 19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)

# 八边形
t.reset()
for x in range(1, 9):
    t.forward(100)
    t.left(45)


def mycircle(red, green, blue):    # 用来画填色图形的函数
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

t.reset()
mycircle(0, 1, 0)
t.reset()
mycircle(0.5, 0.8, 0.4)


def mysquare(size, filled):
    if filled:
        t.begin_fill()
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
    if filled:
        t.end_fill()
t.reset()
mysquare(50, True)
mysquare(150, False)
sleep(3)


# 画汽车
t.reset()
t.color(1, 0, 0)
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()
# 轮子
t.color(0, 0, 0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()
# 另一个轮子
t.setheading(0)     # 让海龟指向指定的方向
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.circle(10)
t.end_fill()

