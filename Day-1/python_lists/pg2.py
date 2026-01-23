# pg2: Find common elements between two lists

def common_elements(list1, list2):
    common = []

    for item in list1:
        if item in list2 and item not in common:
            common.append(item)

    return common


a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

print(common_elements(a, b))
