def pairs_sum_to_target(list1, list2, target):
    new_list = []
    for i, enum in enumerate(list1):
        for j, enum2 in enumerate(list2):
            if enum2 + enum == target:
                new_list.append([i, j])
    return new_list
