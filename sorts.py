def bubble_sort(alist):
    length = len(alist)
    if length < 2:
        return alist
    else:
        for index in range(length):
            for iterator in range(length - 1, index, -1):
                if alist[iterator] < alist[iterator - 1]:
                    alist[iterator], alist[iterator - 1] = alist[iterator - 1], alist[iterator]
    
    
def insertion_sort(alist):
    length = len(alist)
    if length < 2:
        return alist
    else:
        for index in range(1, length): # for every unsorted elements
            value = alist[index] # remember the value
            j = index - 1
            while j >= 0: # search postiton in sorted part
                if value < alist[j]:
                    alist[j + 1] = alist[j] # move backward
                    if j == 0: 
                        alist[j] = value # insert in start
                    j -= 1
                else:
                    alist[j + 1] = value
                    break

    
def merge_sort(alist):
    length = len(alist)
    if length < 2:
        return alist
    if length > 1:
        mid = len(alist) // 2
        left = alist[:mid] # 0 - (mid - 1)
        right = alist[mid:] # mid - (n - 1)
        merge_sort(left)
        merge_sort(right)
        
        i, k, j =0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
                k += 1
            else:
                alist[k] = right[j]
                j += 1
                k += 1
        if i == len(left):
            alist[k:] = right[j:]
        else:
            alist[k:] = left[i:]
    
    
def quicksort_(alist):
    """
    simple implementation
    """
    if len(alist) < 2:
        return alist
    pivot = alist[0]
    less = []
    greater = []
    for e in alist[1:]:
        if e <= pivot:
            less.append(e)
        else:
            great.append(e)
    quicksort_(less)
    quicksort_(greater)
    alist[::] = less + [pivot] + greater
    
       
def quicksort(alist):
    _sorting(alist, 0, len(alist) - 1)
    
def _sorting(alist, left, right):      
    if right - left > 10 : 
        pivot = _median_of_three(alist, left, right)
        i, j = left + 1, right - 2 # left and right are already in position
        while True:    
            while alist[i] < pivot:
            # use < rathen than <=. consider worst case that the emtire sequence is all 1, it will do many extra swap operations but the pivot will be placed in a reletively middle position, so the sequence will be divided to half and the time complexity remains O(nlogn)
                i += 1
            while alist[j] > pivot:
                j -= 1
            if j > i: # switch side of pivot
                alist[i], alist[j] = alist[j], alist[i]
                i += 1
                j += 1
            else:
                break
        alist[i], alist[right - 1] = alist[right - 1], alist[i]
        _sorting(alist, left, i - 1)
        _sorting(alist, i + 1, right)
    else:
        insertion_sort(alist) # when scale is small, use simple sorting. 

def _median_of_three(alist, left, right):
    centre = right // 2
    if alist[left] > alist[centre]:
        alist[left], alist[centre] = alist[centre], alist[left]
    if alist[left] > alist[right]:
        alist[left], alist[right] = alist[right], alist[left]
    if alist[centre] > alist[right]:
        alist[centre], alist[right] = alist[right], alist[centre]
    alist[centre], alist[right - 1] = alist[right - 1], alist[centre] 
    return alist[right - 1]
