def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        less = arr[:mid]
        more = arr[mid:]
        mergeSort(less)
        mergeSort(more)
        i = j = k = 0
        while i < len(less) and j < len(more):
            if less[i] <= more[j]:
                arr[k] = less[i]
                i += 1
            else:
                arr[k] = more[j]
                j += 1
            k += 1
        while i < len(less):
            arr[k] = less[i]
            i += 1
            k += 1
        while j < len(more):
            arr[k] = less[j]
            j += 1
            k += 1
    return arr


if __name__ == '__main__':
    arr = []
    count = int(input("How many? "))
    for x in range(count):
        arr.append(input())
    print(*mergeSort(arr))
