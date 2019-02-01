from tkinter import *
from time import sleep
import random

def hello():
    print('hello there')


def person(width, height):  # 具名参数
    print('I am %s feet wide,%s feet height'%(width, height))

tk = Tk()
# btn = Button(tk, text="click me", command=hello)
# btn.pack()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

canvas.create_line(0, 0, 500, 500)
canvas.create_rectangle(10, 10, 50, 50)     #座标


def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2, fill = fill_color)

for x in range(1,4):
    random_rectangle(300, 300, '#ffd800')

# 圆弧
canvas.create_arc(10, 10, 200, 100, extent = 180, style = ARC)
canvas.create_arc(50, 50, 500, 200, extent = 270, style = ARC)
canvas.create_arc(100, 100, 30, 30, extent = 300, style = ARC)

# 画多边形
canvas.create_polygon(200, 190, 300, 100, 400, 460, fill ='', outline = 'black')

# 显示文字
canvas.create_text(300, 300, text='on a goose', font = ('Courier', 30))

# 显示.gif图片 ... 就是不动的
my_image = PhotoImage(file = r'E:\core\python\pycharmpro\0001.gif')
canvas.create_image(0, 0, anchor = NW, image = my_image)    # NW == northwest 西北方作为画画的起始点

# 创建基本的动画
my_triangle = canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.itemconfig(my_triangle, fill = 'yellow', outline = 'orange')

for x in range(0, 60):
    canvas.move(my_triangle, 5, 2)   # 12为 canvas创建图形的id，横向移动5个像素，纵向移动2个像素
    tk.update()
    sleep(0.05)

# 让对象对操作有反应
def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(my_triangle, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(my_triangle, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(my_triangle, -3, 0)
    elif event.keysym == 'Right':
        canvas.move(my_triangle, 3, 0)

canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)

tk.mainloop()

print('%02x '% 15)   # 将十进制数转化为十六进制，数字至少有两位

