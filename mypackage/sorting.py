def bubble_sort(items):
    output = items.copy()
    for i in range(len(output)):
        for j in range(len(output) - 1 - i):
            if output[j] > output[j + 1]:
                output[j], output[j + i] = output[j + i], output[j]
    return output
    '''Return array of items, sorted in ascending order'''

def merge_sort(items):
    len_i = len(items)
    if len_i == 1:
        return items

    mid_point = int(len_i / 2)
    A = merge_sort(items[:mid_point])
    B = merge_sort(items[mid_point:])

    new_list = []
    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            new_list.append(A[0])
            A.pop(0)
        else:
            new_list.append(B[0])
            B.pop(0)

    if len(A) == 0:
        new_list = new_list + B
    if len(B) == 0:
        new_list = new_list + A

    return new_list

    '''Return array of items, sorted in ascending order'''

def quick_sort(items):
    len_i = len(items)

    if len_i <= 1:
        return items

    end = items[-1]
    small = []
    large = []
    dup = []
    for i in items:
        if i < end:
            small.append(i)
        elif i > end:
            large.append(i)
        elif i == end:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large

    '''Return array of items, sorted in ascending order'''