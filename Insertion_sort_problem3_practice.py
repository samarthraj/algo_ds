def split_names(name2, name1):
    first_name2, last_name2 = name2.split()
    first_name1, last_name1 = name1.split()

    if last_name2 != last_name1:
        return last_name2 < last_name1
    else:
        return len(first_name2) < len(first_name1)


def sort_names(names_list):

    for index in range(1, len(names_list)):
        value = names_list[index]
        i = index - 1
        while i >= 0 and split_names(value, names_list[i]):
            names_list[i+1] = names_list[i]
            names_list[i] = value
            i = i - 1
    return names_list


names_list = [
    "John Doe",
    "Jane Smith",
    "Alice Johnson",
    "David Brown",
    "Mary Johnson",
    "Mark Smith",
]
res = sort_names(names_list)
print(res)
