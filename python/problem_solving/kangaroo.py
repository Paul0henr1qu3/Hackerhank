# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    jumps_v1 = x1 + v1
    jumps_v2 = x2 + v2
    x1 += v1
    x2 += v2

    while x1 <= 19999999 or x2 <= 19999999:
        if jumps_v1 == jumps_v2:
            return 'YES'
        jumps_v1 += v1
        jumps_v2 += v2
        x1 += v1
        x2 += v2


    return 'NO'