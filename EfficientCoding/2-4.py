from random import randint
#如何根据字典中值的大小对字典中的项进行排序
#法1
d = {x: randint(60,100) for x in "adjfdjghrw"}
print(d)
print(sorted(d))
print(iter(d))
print(list(iter(d)))
print(d.keys())
z = zip(d.values(),d.keys())
print(sorted(z))
#法2
print("second:",d.items())
print(sorted(d.items(), key = lambda x : x[1]))
