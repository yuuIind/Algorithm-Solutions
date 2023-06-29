def mergeSort(arr):
    if(len(arr) < 2):
        return arr
    mid_point = len(arr) // 2

    arr_left = arr[:mid_point]
    arr_right = arr[mid_point:]

    arr_left = mergeSort(arr_left)
    arr_right = mergeSort(arr_right)
    arr = mergeS(arr_left, arr_right, n=len(arr))
    return arr


def mergeS(left, right, n=0):
    if n == 0:
        n = len(left) + len(right)
    arr = []
    i = 0
    j = 0
    for k in range(n):
        if i >= len(left):
            arr.extend(right[j:])
            return arr
        elif j >= len(right):
            arr.extend(left[i:])
            return arr
        
        if left[i] <= right[j]:
            arr.append(left[i])
            i +=1
        else:
            arr.append(right[j])
            j +=1
    return arr

arr = [1, 8, 5, 3, 5, 9, 2, 14, 6, 3, 7, 4, 0]
arr = mergeSort(arr)
print(arr)
