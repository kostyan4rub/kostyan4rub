my_dict = {'Alisa': 2016, 'Anton' : 2019}
print(my_dict['Anton'])
my_dict['Natasha'] = 1989
my_dict.update({'Konstantin' : 1988,
                'Maxim' : 1986})
print(my_dict)
my_dict.pop('Maxim')
print(my_dict)
my_set = {1, 2, 3, 3, 1, 2, 'sun', 'sky', 'sea', 'sky','sea', 'sun'}
print(my_set)
my_set.add(5)
my_set.add(7)
my_set.remove(3)
print(my_set)