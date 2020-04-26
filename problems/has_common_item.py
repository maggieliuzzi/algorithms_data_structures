"""
Check if there are any common items between two arrays
"""

list1 = ['a', 'x', 1, 'g', [], True, 2.5]
list2 = ['b', 'l', 'm', 'v', None, 2.5]

def has_common_item(list1, list2):
    if type(list1) is not list or type(list2) is not list:
        return -1

    list1_set = set()
    for i in list1:  # could be its own function
        if type(i) is not int and type(i) is not str:
            i = str(i)
        if i not in list1_set:
            list1_set.add(i)
    for j in list2:
        if type(j) is not int and type(j) is not str:
            j = str(j)
        if j in list1_set:
            return True

    return False

print(has_common_item(list1, list2))
# print(has_common_item(list1))  # can we assume two params?
print(has_common_item(list1, 0))
