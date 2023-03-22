def insertionsort1(n, arr):
    for i in range(1, n):
        h = arr[i]
        j = i
        while j > 0 and arr[j - 1] > h:
            arr[j] = arr[j - 1]
            print(*arr)
            j -= 1
        arr[j] = h
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionsort1(n, arr)
