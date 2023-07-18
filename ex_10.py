import copy

lst = [1, 4, 2, [1, 3, [78, 45, 89]]]

lst2 = copy.copy(lst)

lst3 = copy.deepcopy(lst)

lst[3][2][1] = 10

print(lst2)
print(lst3)