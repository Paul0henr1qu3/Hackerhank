# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    count_d = 0
    sea_level = 0

    for step in s:

        if step == 'D':
            count_d += 1
            sea_level -= 1

            if sea_level < 0 and count_d == 1:
                valleys += 1
        else:
            count_d -= 1
            sea_level += 1

    return valleys