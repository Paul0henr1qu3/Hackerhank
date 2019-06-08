# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    aux = 0
    tmp_ar = []

    for num in ar:
        aux = ar.count(num)

        if aux == 2 and num not in tmp_ar:
            pairs += 1
            aux = 0
            tmp_ar.append(num)

        elif aux > 2 and num not in tmp_ar:
            pairs += aux // 2
            tmp_ar.append(num)

    return pairs