#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 计算器: 我觉得正则表达式才是王道！！！
#这个程序写的太精妙了
#其实整个程序相当于eval()函数。。。。。把输入的字符串转化为数字和运算符，并返回表达式的结果

import re

def main():
    #a=input("请输入需要计算的公式：")
    a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    #a = '1+2+(3 - 4) *5/5 +1'
    b = "".join(a.split())  #将字符串中多余的空格去掉并合成一个新的字符串
    while True:
        if "("in b:
            c = re.search(r"\([^()]+\)",b)  #匹配一对括号，且括号中没有其它括号。[]中第一个字符为^则表示取反
            if c is not None:
                e=c.group()
                d=cal(e)
                b=re.sub(r"\([^()]+\)",str(d),b,1)
        else:
            c=cal(b)
            print(c)
            break

#addition  and subtraction
def add_sub(b):
    if "--" in b:
        b=b.replace("--","+")
    add_list = re.findall(r"-?\d+\.?\d*", b)    #匹配 b 中的所有数字，包括小数，负数
    list=[]
    for i in add_list:
        list.append(float(i))   #将字符串列表转化为数字列表
    t=sum(list)     #加法和减法的本质是一样的，减去x 相当于加上 -x,所以这里用的都是sum()
    print('add_sub:',t)
    return t

#multiplication
def mul(b):
    mul_ch=re.search(r"\d+\.?\d*(\*-?\d+\.?\d*)",b)
    if mul_ch is not None:
        mul_ch=mul_ch.group()
        mul_list=re.findall(r"-?\d+\.?\d*",mul_ch)  #搜索string，以列表形式返回全部能匹配的子串
        list=[]
        for i in mul_list:
            list.append(float(i))   #将字符串列表转化为数字列表
        multip=list[0]*list[1]
        b=re.sub(r"\d+\.?\d*(\*-?\d+\.?\d*)",str(multip),b,1)
        print('mul:',multip)
        return b

#division
def div(b):
    div_ch=re.search(r"\d+\.?\d*(\/-?\d+\.?\d*)",b)
    if div_ch is not None:
        div_ch=div_ch.group()
        div_list=re.findall(r"-?\d+\.?\d*",div_ch)
        list=[]
        for i in div_list:
            list.append(float(i))
        division=list[0]/list[1]
        b=re.sub(r"\d+\.?\d*(\/-?\d+\.?\d*)",str(division),b,1)
        print('div:',division)
        return b
#calculation
def cal(c):
    while True:
        if "*"in c:
            s=c.split("*")
            if "/"in s[0]:
                c=div(c)
            else:
                c=mul(c)
        elif "/"in c:
            c=div(c)
        elif "+"or "-" in c:
            c=add_sub(c)
            return c
        else:
            return c

main()
