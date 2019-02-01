# -*- coding: utf-8 -*-
height = float (input('please enter your height(m):'))
weight = float (input('please enter your weight(kg):'))
bim = weight / height / height
if bim <18.5:
	print('过轻')
elif bim < 25.0:
	print('正常')
elif bim < 28.0:
	print('过重')
elif bim<32.0:
	print('肥胖')
else :
	print('严重肥胖')