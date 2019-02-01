# coding=utf-8
# 使用list 构建堆栈
class Stack(object):
	__sorts__ = ('items')

	# 初始化为空列表
	def __init__(self):
		self.items = []

	# 判断栈是否为空，返回布尔值
	def is_empty(self):
		return self.items == []

	# 返回栈顶元素
	def peek(self):
		return self.items[len(self.items)]

	# 返回栈的大小
	def size(self):
		return len(self.items)

	# 把新的元素堆进栈里
	def push(self, item):
		self.items.append(item)

	# 把栈顶元素丢出去
	def pop(self):
		return self.items.pop(self.size()-1)
