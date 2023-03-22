import bisect


def runningMedian(arr):
    l = len(arr)
    if l % 2 == 0:
        x = int(l / 2)
        return (arr[x] + arr[x - 1]) / 2
    else:
        x = int(l / 2)
        return arr[x]

if __name__ == '__main__':
    n = int(input().strip())
    a = []
    for i in range(n):
        a_item = int(input().strip())
        bisect.insort(a, a_item)    
        print(float(runningMedian(a)))
