# coding=utf-8
import copy
import keyword
# copy 为浅拷贝，只是拷贝了list，list中的对象还是原来的对象，改变了原来的对象，拷贝对象也会随之改变
# deepcopy 则会创建被拷贝对象中的所有对象的拷贝
# keyword 模块记录了所有的关键字

print(keyword.iskeyword('if'))
print(keyword.kwlist)   # 所有关键字列表


class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color


harry = Animal('hippo griff', 6, 'pink')
harries = copy.copy(harry)
print(harry.species)
print(harries.species)
carrie = Animal('chimera', 6, 'pink')
billy = Animal('chimera', 4, 'green polka dots')
my_animals = [harry, carrie, billy]
more_animals = copy.copy(my_animals)
print(more_animals[0].species)
print(more_animals[1].species)
my_animals[0].species = 'ghoul'
print('after change my_animals:', my_animals[0].species)
print('after change more_animals:', more_animals[0].species)
print('-'*50)
sally = Animal('sphinx', 4, 'sand')
my_animals.append(sally)
print('my_animals:', len(my_animals))
print('more_animals:', len(more_animals))
print('-'*50)
more_animals_deep = copy.deepcopy(my_animals)
my_animals[0].species = 'wyim'
print(more_animals_deep[0].species)     # 没变
