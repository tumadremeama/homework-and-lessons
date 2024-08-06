my_dict = {'Demyan': 1995, 'Alicia': 2003, 'Christrian': 1997, 'Bogo': 1995}
print(my_dict)
print(my_dict.get('Demyan'))
print(my_dict.get('Vladimir'))
my_dict.update({'Cristian': 1991,'Bogdan': 1996})
del my_dict['Christrian']
print(my_dict)


my_set = {1, 1, 1, 2, 2, 'Pacha', 'Pacha', True, True}
print(set(my_set))
print(my_set.add('Guacamole'))
print(my_set.add('Fresh24'))
print(my_set.discard(True))
print(my_set)
