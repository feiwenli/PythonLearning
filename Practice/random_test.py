import random
import sys

desserts = ['ice cream', 'pancakes', 'brownies', 'cookies', 'candy']
print(random.choice(desserts))  # 从列表元素中随机选取一个元素
random.shuffle(desserts)    # 给列表元素重新洗牌
print(desserts)
sys.exit()  # 控制shell程序
