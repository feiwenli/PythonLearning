#处理二进制wav文件
#写出来的文件无法播放？？？？？？？？？
import struct
import array
from random import randint

f = open('dahuoji.wav','rb')
info = f.read(44)	#前44个信息部分，后面的为数据部分
print(struct.unpack('h',b'\x01\x02'))	#小端字节序 将二进制转化为short
print(struct.unpack('>h',b'\x01\x02'))	#大端字节序 将二进制转化为short
print(struct.unpack('h',info[34:36]))	#short	音频文件的声道数
print(struct.unpack('i',info[24:28]))	#int
print('-'*50)

f.seek(0,2)		#将指针挪到队尾
print(f.tell())	#报告指针的位置
n = int((f.tell() - 44)/2)	#数组的长度
buf = array.array('h',(0 for _ in range(0,n)))	#创建数组，每个元素都是0
f.seek(44)	#将指针指到数据的位置
f.readinto(buf) 	#把数据读入buf中
print('0:',buf[0])
print('6:',buf[6])
print('20:',buf[20])
f.close()

for i in range(n): buf[i] //= 8		#将采样宽度缩小，即将声音变小
f2 = open('dahuoji02.wav','wb')		#创建一个新的文件
f2.write(info)	#将信息部分写入
buf.tofile(f2)	#将buf中是数据写入文件中去
f2.close()
