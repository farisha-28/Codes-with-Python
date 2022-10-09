import itertools
list_1 = [1,3,[4,3,6],[8,5,9]]
list_2 = [1,3,[4,3,6],[8,5,9],[0,5,3]]
print(list(itertools.chain(*list_1)))
print(list(itertools.chain(*list_2)))