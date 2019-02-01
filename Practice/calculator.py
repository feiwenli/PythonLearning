#-*- coding = utf-8 -*-
#好吧.....抄了一个......不适合的代码

import re 
import sys

def remove_space(data_list):
	'''去除列表中的空元素'''
	for x in data_list:
		if type(x) is not int:
			if len(x.strip()) == 0:
				data_list.remove(x)
	return data_list

def fetch_data_from_bracket(data_list, first_right_bracket_pos):
	'''用递归的形式取出每一对括号里的数据并进行计算且得出结果'''
	print('data_list:',data_list)
	left_bracket_pos, right_bracket_pos = data_list.index('('),data_list.index(')') + 1
	print('\033[31;1mleft bracket pos:%s right_bracket_pos:%s\033[0m'%(left_bracket_pos, first_right_bracket_pos))
	data_after_strip = data_list[left_bracket_pos:right_bracket_pos]
	if data_after_strip.count("(") > 1:
		print('fetch_data_from_bracket:%s \033[31;1m%s\033[0m left pos:%s' %(data_after_strip,data_after_strip[1:], left_bracket_pos))
		return fetch_data_from_bracket(data_after_strip[1:],first_right_bracket_pos)
	else: 
		print('last:',len(data_after_strip),data_after_strip)
		bracket_start_pos = first_right_bracket_pos - len(data_after_strip) + 1	#( takes two position 
		calc_res = parse_operator(data_after_strip)
		return calc_res, bracket_start_pos, first_right_bracket_pos + 1 #') takes one position'

def parse_bracket(formula):	#解析括号中的格式	formula：公式	parse:解析
	'''解析括号中的公式，并运算出结果'''
	pattern = r"\(.+\)"		#图案，样品		一个正则表达式，表示匹配（大于一个字符）
	m = re.search(pattern, formula)	#匹配出所有的括号 ‘3 / 1      - 2 * ( (60-30 * (4-2)) - 4*3/ (6-3*2) )’ 匹配完之后是'( (60-30 * (4-2)) - 4*3/ (6-3*2) )'
	if m:
		data_with_brackets = m.group()
		#print(list(data_with_brackets))
		data_with_brackets = remove_space(list(data_with_brackets))
		#print(data_with_brackets)
		calc_res = fetch_data_from_bracket(data_with_brackets, data_with_brackets.index(')'))
		print('\033[32;1mResult:\033[0m',calc_res)
		print(calc_res[1],calc_res[2])
		print(data_with_brackets[calc_res[1]:calc_res[2]])
		del data_with_brackets[calc_res[1]:calc_res[2]]
		data_with_brackets.insert(calc_res[1],str(calc_res[0]))	#replace string formula string with calculation result 4
		return parse_bracket(''.join(data_with_brackets))	#继续处理其它括号
	else:
		print('\033[42;1mCalculation result:\033[0m',formula)

def caculate_1(formula):# for multiplicatuion and division
	result = int(formula[0])	# e.g ['4', '/', '2', '*', '5'], loop start from '/'
	last_opperator = None
	formula = list(formula)
	nagative_mark = False
	for index,i in enumerate(formula[1:]):
		#if str(i).isdigit():
			if nagative_mark:
				i = int('-'+i)
				nagative_mark = False
			else:
				i = int(i)
			if last_opperator == '*':
				result *= index
			elif last_opperator == '/':
				try:
					result /= index
				except( ZeroDivisionError,e):
					print("\033[31;1mError:%s\033[0m" % e)
					sys.exit()
		#elif i == '-':
		#	nagative_mark = True
		#else:
		#	last_opperator = index
	print('乘除运算结果：', result)
	return result
def calculate_2(data_list, operator_list):
	'''eg. data_list:['4', 3, 1372, '1']  operator_list:['-', '+', '-']'''
	data_list = remove_space(data_list)
	print('caculator_2:',data_list,operator_list)
	result = int(data_list[0])
	for i in data_list[1:]:
		if operator_list[0] == '+':
			result += int(i)
		elif operator_list[0] == '-':
			result -= int(i)
		del operator_list[0]

	print('caculator_2 result:',result)
	return result
def parse_operator(formula):
	print('开始运算公式：',formula)
	formula = formula[1:-1]	#remove bracket
	low_priorities = re.findall('[+,-]',''.join(formula))
	data_after_remove_low_priorities = re.split('[+,-]',''.join(formula))
	print('去掉加减后的公式列表，先算乘除：',data_after_remove_low_priorities)
	for index,i in enumerate(data_after_remove_low_priorities):
		if i.endswith("*") or i.endswith("/"):
			data_after_remove_low_priorities[index] += '-' + data_after_remove_low_priorities
			del data_after_remove_low_priorities[index+1]
	print('--------------------->handle nagative num:',data_after_remove_low_priorities)
	#计算乘除运算
	nagative_mark = False
	for index,i in enumerate(data_after_remove_low_priorities):
		if not i.isdigit():
			if len(i.strip()) == 0:
				nagative_mark = True
			else:#remove space
				string_to_list = []
				if nagative_mark:
					prior_l = '-' +i[0]
					nagative_mark = False
				else:
					prior_l = i[0]
				for l in i[1:]:
					if l.isdigit():
						if prior_l.isdigit() or len(prior_l) >1:	#two letter should be combine
							prior_l += 1
						else:
							prior_l = 1
					else:#an operator * or /
						string_to_list.append(prior_l)
						string_to_list.append(1)
						prior_l = 1 	#reset  prior_l
				else:
					string_to_list.append(prior_l)
				print('------------------>::',string_to_list)
				calc_res = caculate_1(string_to_list)	#乘除运算结果
				data_after_remove_low_priorities[index] = calc_res
		else:
			if nagative_mark:
				data_after_remove_low_priorities[index] = '-' + i
	print ('去掉 * 和 / 后开始运算加减：',data_after_remove_low_priorities,low_priorities)
	#计算加减运算
	return calculate_2(data_after_remove_low_priorities,low_priorities)
def main():
	while True:
		user_input = input(">>>:").strip()
		if len(user_input) == 0 :continue
		user_input = '('+user_input +')'
		parse_bracket(user_input)

		print('\033[43;qmpython计算器运算结果：\033[0m',eval(user_input))
if __name__ == '__main__':
	main()
