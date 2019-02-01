# -*- coding = utf-8 -*-
#如何将文件映射到内存上

import mmap

f = open('demo.bin','wb',buffering = 0)
f.write('你好啊，阿部察察'.encode('utf-8'))

m = mmap.mmap(f.fileno(),0,access=mmap.ACCESS_WRITE)
#PermissionError: [WinError 5] 拒绝访问。
#0 表示映射整个文件

print(type(m))

print(m[0])
print(m[10:20])

m[0] = '\x88'

m[4:8] = '\xff'*4

#跳过四个页，映射八个页
m = mmap.mmap(f.fileno(), mmap.PAGESIZE*8,access=mmap.ACCESS_WRITE,offset=mmap.PAGESIZE*4)
m[:0x1000] = '\xaa' * 0x1000
