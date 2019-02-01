# -*- coding = utf-8 -*-
import turtle
from random import randint
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

