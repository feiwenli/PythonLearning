# coding=utf-8 
# 数据导入和内存管理

import sys
import os
from numpy import *
import re
import cPickle as pickle

# 配置一个utf-8输出环境
reload(sys)
sys.setdefaultencoding('utf-8')


# 数据文件转换矩阵
# path：数据文件路径
# delimiter：行内字段分隔符
def file2matrix(path, delimiter):
    recordlist = []
    fp = open(path, 'rb')
    content = fp.read()
    fp.close()
    rowlist = content.splitlines()  # 按行转换位一维表
    # 逐行遍历，结果按分隔符分隔为行向量
    for row in rowlist:
        recordlist.append([x for x in re.split(delimiter, row)])
    return mat(recordlist)


root = 'E:\\data'  # 文件所在路径
pathlist = os.listdir(root)
for path in pathlist:
    recordmat = file2matrix(root + '/' + path, r'[\t\0\n]')
    print shape(recordmat)
    # 将刚才转换为矩阵的数据持久化为对象的文件
    file_obj = open(root+'/recordmat.dat','wb')
    pickle.dump(recordmat[0],file_obj)
    file_obj.close()
    # 读取序列化后的文件
    read_obj = open(root+'/recordmat.dat','rb')
    readmat = pickle.load(read_obj)
    print 'shape:',shape(readmat)



