# pg1: Elements present in first list but not in second list

def difference_set(list1, list2):
    return set(list1) - set(list2)


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(difference_set(list1, list2))
