"""
file that handles dsa tasks
"""

def data_structures():
    my_list = []
    value = 0
    while (value < 40):
        value +=10
        my_list.append(value)
    print(f" My list currently: {my_list}")
    # insert 15 at index 1 or after 10
    my_list.insert(1,15)
    print(f" My list after inserting 15 after 10 or at index 1: {my_list}")
    # extending list with [50, 60, 70].
    extra_list = [50,60,70]
    my_list.extend(extra_list)
    print(f" My list after extending with list [ 50, 60, 70 ]: {my_list}")
    # removing last item in the list.
    my_list.pop()
    print(f" My list after removing last item on the list: {my_list}")
    # sort list in ascending order.
    my_list.sort()
    print(f" My list after sorting list in ascending order: {my_list}")
    # finding index of number 30 in my list.
    index_of_30 = my_list.index(30)
    print(f" Index of 30 in my_list: {index_of_30}")
