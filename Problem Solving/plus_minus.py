# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0

    total_elements = len(arr)

    for element in arr:
        if element > 0:
            positive += 1
        elif element < 0:
            negative += 1
        else:
            zero += 1

    print("{:.6f}\n{:.6f}\n{:.6f}\n".format(positive / total_elements, negative / total_elements, zero / total_elements))
