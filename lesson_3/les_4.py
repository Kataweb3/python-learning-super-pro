a = 'jaybe'
a += ' or... jaybe not'
print(a)
# symbol = symbol * 20
symbol = '+'
symbol *= 20
print (symbol)
print ('GLORIOUS EVOLUTION')
print (symbol)

text = 'Im feeling fantastic'
print('Feeling' in text)

c = 123
print (id(c))
d = 123
print(id(d))

#user_ship = input('What is your ship? ')
#print(user_ship, '? wow, congrats, geek')

#user_input = input('enter something, pls ')
#print(type(user_input))


#СПИСОК LIST - в квадратных скобках

my_list = [123, 256, 'LALAL', 'трэш', 2.333333333]
print(my_list[3])
print(my_list[-1]) #первый элемент с конца
#отсчет идет с 0 !!!!!!!!!!!!!!!!! (копец)

my_list[2] = 'TEATIME'
print(my_list)

my_list2 = []
my_list2.append('BOOM SHAKALAKA YEAAS GAWD')
my_list2.append('what the hell, sure')
#append типа апп и енд - добавляет что-то в конец, выполняет по очереди
print(len(my_list2)) #позволяет узнать количество элементов в списке
print(my_list2)

poped = my_list2.pop(0) #удаляет элемент из списка
print(my_list2)
print(poped)

print('text' in my_list2)


#КОРТЕЖИ TUPLE - в фигурных скобках
#в кортежи нельзя добавлять новые элемент

my_tuple = (1, 259, 'TOLD YA', 'пупупу', 1)
print(my_tuple)
print(my_tuple.count(1)) #считает сколько раз элемент встречается в кортеже
print(my_tuple.index(1)) #найдет индекс элемента

llist = [56]
print(llist)
ttuple = (56,) #если в кортеже 1 элемент, то надо ставить запятую в конце, иначе не будет восприниматься как класс кортеж, а будет как просто число в скобках и вывдет кортеж без скобок
print(ttuple)

#Множества SET - фигурные скобки
# в множестве хранятся только уникальные элементы
#

my_set ={1, 3.7777, 'lalala', False, 1}
my_set.add(42)
my_set.add('text')
my_set.add('lalala') #если элемент уже есть в множестве, то добавление игнорируется
print(my_set)

#создание списка с уникальным элементом - преобразовать в сет и обратно в лист
list2 = [1, 5555, 2, 3, 5555, 1, 7, 8, 7, 3]
list2 = set(list2)
list2 = list(list2)
print(list2)

#можно проще
list3 = list(set([1, 777, 2, 3, 777, 1, 99, 8, 99, 3]))
print(list3)


my_set = {} #это слвоарь
my_set = set() #пустой сет можно создать только так

# Словарь dictionary
# коллекии произвольных объектов с доступом к ним по ключу

my_dict = {'one': 'value', 'two': 'value2'} #ключ:значение
print(my_dict['one'])
my_dict['one'] = 'value1'
my_dict['three'] = 'value3'
my_dict['five'] = [1, 2, 3]
my_dict['four'] = {1, 33, 78}
print(my_dict)

# ключом может быть только неизменяемый тип данных
# не могут список, сет и словарь

