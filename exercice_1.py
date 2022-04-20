


def get_indexes(my_list, value_to_get):
    index2 = []
    for index, value in enumerate(my_list):
        if value == value_to_get:
            index2.append(index)
    return index2


my_list = [1,5,3,6,8,1]
value_to_get = 10

print(get_indexes(my_list, value_to_get))


