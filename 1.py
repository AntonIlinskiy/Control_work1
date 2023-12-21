def replace_none_with_zero(lst):
    new_lst = []
    for sublist in lst:
        new_sublist = []
        for item in sublist:
            if item is None:
                new_sublist.append(0)
            else:
                new_sublist.append(item)
        new_lst.append(new_sublist)
    return new_lst


test_lst = [
    [1, 2, 3],
    [4, 5, 6],
    [None, 8, 9],
    [10, 11, 12],
    [13, None, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, None],
]
result = replace_none_with_zero(test_lst)
print(result)
