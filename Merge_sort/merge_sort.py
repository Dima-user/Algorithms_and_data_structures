from operator import lt

def merge_sort(list, compare_operator = lt):
    list_len = len(list)

    if list_len < 2:
        return list
    
    leftPart = merge_sort(list[:list_len // 2])
    rightPart = merge_sort(list[list_len // 2:])

    return merge_sub_lists(leftPart, rightPart, compare_operator)

def merge_sub_lists(left_sub_list, right_sub_list, compare_operator):
    left_sub_list_index = 0
    right_sub_list_index = 0

    left_sub_list_len = len(left_sub_list)
    right_sub_list_len = len(right_sub_list)

    merged_list = []

    while left_sub_list_index < left_sub_list_len and right_sub_list_index < right_sub_list_len:
        if compare_operator(left_sub_list[left_sub_list_index], right_sub_list[right_sub_list_index]):
            merged_list.append(left_sub_list[left_sub_list_index])
            left_sub_list_index += 1
        else:
            merged_list.append(right_sub_list[right_sub_list_index])
            right_sub_list_index += 1

    while left_sub_list_index < left_sub_list_len:
        merged_list.append(left_sub_list[left_sub_list_index])
        left_sub_list_index += 1

    while right_sub_list_index < right_sub_list_len:
        merged_list.append(right_sub_list[right_sub_list_index])
        right_sub_list_index += 1
    
    return merged_list