#
# Complete the timeConversion function below.
#
def timeConversion(s):
    n = int(s[:2])
    pm = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    am = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    if s[8:] == 'PM' and n not in pm:
        n = pm[n]
        s = str(n) + s[2:8]
    elif s[8:] == 'AM' and n not in am:
        n = am[n - 1]
        s = '0' + str(n) + s[2:8]
    else:
        s = s[:8]

    return s
