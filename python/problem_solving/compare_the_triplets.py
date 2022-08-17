# Complete the compareTriplets function below.
def compareTriplets(a, b):
    points_a = 0
    points_b = 0

    for num_a, num_b in zip(a,b):
        if num_a > num_b:
            points_a += 1
        elif num_b > num_a:
            points_b += 1

    return [points_a, points_b]