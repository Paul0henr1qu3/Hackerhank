# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr = map(int, arr)
    arr = sorted(arr)

    minu = 0
    maxi = 0

    for num in range(0, len(arr) - 1):
        minu += arr[num]

    for num in range(1, len(arr)):
        maxi += arr[num]

    print(minu + '-' + maxi)