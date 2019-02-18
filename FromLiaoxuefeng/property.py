# -*- coding=utf-8 -*-

class Student:

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if score>100 or score<0:
            raise ValueError('score must between 0 and 100')
        if not isinstance(score, int):
            raise ValueError('score must be an int')
        self._score = score

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width =width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    # 只读
    @property
    def resolution(self):
        return self._width * self.height


s = Student()
s.score = 10
print(s.score)

s.width = 1000
s.height = 344
print(s.resolution)


