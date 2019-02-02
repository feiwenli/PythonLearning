#!/usr/bin/python
# coding=utf-8
from tkinter import *
import random
from time import sleep, time


class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Mr. Stick Man Races for the Exit")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=500, height=520, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 520
        self.canvas_width = 500
        self.bg = PhotoImage(file="background.gif")
        w = self.bg.width()
        h = self.bg.height()
        for x in range(0, 5):
            for y in range(0, 6):
                self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')
        self.sprites = []  # 小精灵
        self.running = True

    def mainloop(self):
        while 1:
            if self.running:
                for sprite in self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            sleep(0.01)


class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


def within_x(co1, co2):  # 是否在水平方向上冲突
    if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
            or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
            or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
            or (co2.x2 > co1.x1 and co2.x2 < co1.x1):
        return True
    else:  # 两个坐标对象在水平位置上没有交叉
        return False


def within_y(co1, co2):
    if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
            or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
            or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
            or (co2.y2 > co1.y1 and co2.y2 < co1.y1):
        return True
    else:
        return False


def collided_left(co1, co2):
    if within_y(co1,co2):
        if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
            return True
    return False


def collided_right(co1, co2):
    if within_y(co1, co2):
        if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
            return True
    return False


def collided_top(co1, co2):
    if within_x(co1, co2) and co2.y2 <= co1.y1 <= co2.y1:
        return True
    return False


def collided_bottom(y, co1, co2):
    if within_x(co1, co2):
        y_calc = co1.y2 + y
        if co2.y1 <= y_calc <= co2.y2:
            return True
    return False


class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None

    def move(self):
        pass

    def coords(self):
        return self.coordinates


class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x + width, y + height)  # 他的值是平台图形在屏幕上的真实位置


class DoorSprite(Sprite):
    def __init__(self, game, x, y, width, height):
        Sprite.__init__(self, game)
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.photo_image1 = PhotoImage(file="door2.gif")
        self.photo_image2 = PhotoImage(file="door1.gif")
        self.image = game.canvas.create_image(x, y, image=self.photo_image1, anchor='nw')
        self.endgame = True

    def changeEndImage(self):
        self.game.canvas.itemconfig(self.image, image=self.photo_image2)


class StickFigureSprite(Sprite):
    def __init__(self, game):
        Sprite.__init__(self, game)
        self.image_left = [
            PhotoImage(file="stick-L1.gif"),
            PhotoImage(file="stick-L2.gif"),
            PhotoImage(file="stick-L3.gif")
        ]
        self.image_right = [
            PhotoImage(file="stick-R1.gif"),
            PhotoImage(file="stick-R2.gif"),
            PhotoImage(file="stick-R3.gif")
        ]
        self.image = game.canvas.create_image(200, 470, image=self.image_left[0], anchor='nw')
        # 初始速度
        self.x = 0
        self.y = 0
        self.current_image = 0
        # 图片的变换方向，步长
        self.current_image_add = 1
        self.jump_count = 0
        self.last_time = time()
        self.coordinates = Coords()
        # 与键盘绑定
        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        game.canvas.bind_all('<space>', self.jump)

    def turn_left(self, evt):
        # if self.y == 0:
        self.x = -2

    def turn_right(self, evt):
        # if self.y == 0:
        self.x = 2

    def jump(self, evt):
        # 只有在没有跳跃的状态才能起跳，防止二连跳
        if self.y == 0:
            self.y = -4
            self.jump_count = 0

    def animate(self):
        if self.x != 0 and self.y == 0:
            # 每0.1s更换一下图片，刷新自身图片
            # 不把刷新做在整体的update里面，可以让不同的精灵有不同的刷新频率
            if time() - self.last_time > 0.1:
                self.last_time = time()
                self.current_image += self.current_image_add
                if self.current_image >= 2:
                    self.current_image_add = -1
                if self.current_image <= 0:
                    self.current_image_add = 1
        # 如果速度方向向左
        if self.x < 0:
            # 如果是在起跳的状态下，是固定的起跳图片
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.image_left[2])
            else:
                self.game.canvas.itemconfig(self.image, image=self.image_left[self.current_image])
        elif self.x > 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.image_right[2])
            else:
                self.game.canvas.itemconfig(self.image, image=self.image_right[self.current_image])

    # 预设体积
    def coords(self):
        xy = self.game.canvas.coords(self.image)
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y2 = xy[1] + 30
        return self.coordinates

    def move(self):
        self.animate()
        # 如果小人处于上升状态，那么会不停的计数，等到一定时间之后，小人的速度会向下
        if self.y < 0:
            self.jump_count += 1
            if self.jump_count > 15:
                self.y = 4
        # if self.y > 0:
        #     self.jump_count -= 1
        # 获取自身坐标，为接下来的碰撞检测做准备
        co = self.coords()
        # 为True 表示这个方向没有碰到边界
        left = True
        right = True
        top = True
        bottom = True
        # 是否正在下落
        falling = True
        # 火柴人是否撞到了画布的顶部或底部
        if self.y > 0 and co.y2 >= self.game.canvas_height:
            self.y = 0
            bottom = False
        elif self.y < 0 and co.y1 <= 0:
            self.y = 0
            top = False
        # 是否撞到了画布两旁
        if self.x < 0 and co.x2 >= self.game.canvas_width:
            self.x = 0
            right = False
        elif self.x < 0 and co.x1 <= 0:
            self.x = 0
            left = False
        # 与其他精灵相撞
        for sprite in self.game.sprites:
            if sprite == self:
                continue
            sprite_co = sprite.coords()
            if top and self.y < 0 and collided_top(co, sprite_co):
                self.y = -self.y
                top = False
            # 底部碰撞
            if bottom and self.y > 0 and collided_bottom(self.y, co, sprite_co):
                self.y = sprite_co.y1 - co.y2
                if self.y < 0:
                    self.y = 0
                bottom = False
                top = False
            if bottom and falling and self.y == 0 and co.y2 < self.game.canvas_height \
                    and collided_bottom(1, co, sprite_co):
                falling = False
            # 检查左边右边
            if left and self.x < 0 and collided_left(co, sprite_co):
                self.x = 0
                left = False
                # 这个是判断游戏标志，如果碰触到了endgame为True的，running就会呗设置为False，小人就不能跑了，认为游戏结束。
                # 同时，对应的这个精灵，其实就是门，也需要执行changeEndImage，修改为开门状态。
                if sprite.endgame:
                    self.game.running = False
                    sprite.changeEndImage()
            if right and self.x > 0 and collided_right(co, sprite_co):
                self.x = 0
                right = False
        if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:
            self.y = 4

        self.game.canvas.move(self.image, self.x, self.y)


g = Game()
platform1 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 0, 480, 100, 10)
platform2 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 150, 440, 100, 10)
platform3 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 300, 400, 100, 10)
platform4 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 300, 160, 100, 10)
platform5 = PlatformSprite(g, PhotoImage(file='platform2.gif'), 175, 350, 66, 10)
platform6 = PlatformSprite(g, PhotoImage(file='platform2.gif'), 50, 300, 66, 10)
platform7 = PlatformSprite(g, PhotoImage(file='platform2.gif'), 170, 120, 66, 10)
platform8 = PlatformSprite(g, PhotoImage(file='platform2.gif'), 45, 60, 66, 10)
platform9 = PlatformSprite(g, PhotoImage(file='platform3.gif'), 170, 250, 32, 10)
platform10 = PlatformSprite(g, PhotoImage(file='platform3.gif'), 230, 200, 32, 10)
g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
g.sprites.append(platform4)
g.sprites.append(platform5)
g.sprites.append(platform6)
g.sprites.append(platform7)
g.sprites.append(platform8)
g.sprites.append(platform9)
g.sprites.append(platform10)

stick = StickFigureSprite(g)
g.sprites.append(stick)

door = DoorSprite(g, 45, 30, 40, 35)
g.mainloop()
