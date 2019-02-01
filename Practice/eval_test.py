
# 计算机 eval()
your_calculation = input("Enter your calculation:")
print(eval(your_calculation))
# exec()    可以用来运行python程序从文件中读入的小程序
my_small_program = '''print("han")
print('sandwich') '''
exec(my_small_program)
