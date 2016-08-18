import random


def merge(sorted1, sorted2):
    sorted_list = []
    i = j = 0
    # merge into final sorted list
    while (i < len(sorted1)) or (j < len(sorted2)):
        # fill with only one list once the other is exhausted
        if i >= len(sorted1):
            sorted_list.append(sorted2[j])
            j += 1
        elif j >= len(sorted2):
            sorted_list.append(sorted1[i])
            i += 1
        # choose the smaller of two elements and increment index
        elif (sorted1[i] < sorted2[j]):
            sorted_list.append(sorted1[i])
            i += 1
        else:
            sorted_list.append(sorted2[j])
            j += 1
    return sorted_list

def merge_sort(unsorted):
    length = len(unsorted)
    # ensure recursion stops by specifying base case
    if length < 2:
        return unsorted
    else:
        l1 = unsorted[ :int(length/2)]
        l2 = unsorted[int(length/2): ]
    # apply function recursively
    sorted1 = merge_sort(l1)
    sorted2 = merge_sort(l2)
    return merge(sorted1, sorted2)

if __name__ == '__main__':

    list1 = list(range(100))
    random.shuffle(list1)
    print(list1)
    print(merge_sort(list1))
