from random import randint
from collections import deque
import pickle
import os

target = randint(0,100)

if os.path.exists('history.txt'):
	#使用load()将数据从文件中序列化读出  
	d = pickle.load(open('history.txt','rb'))
	#print('exit')
else:
	d = deque([],5)
	#print('not exit')

def guess(num):
	if num == target:
		print('well down')
		return 1
	elif num > target:
		print('you are bigger than target')
	else :
		print('you are smaller than target')
	return 0
while True:
	line = input("input:")
	if line.isdigit():
		num = int(line)
		d.append(num)
		if guess(num):
			break
	elif line == "history" or line == "h?":
		print(list(d))
	elif line == 'quit':
		break
#使用dump()将数据序列化到文件中 		
fw = open('history.txt','wb')   
pickle.dump(d, fw)  
fw.close()  
