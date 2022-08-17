# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    numero_de_linhas = len(arr)
    soma_outra_diagonal = 0
    soma_diagonal_principal = 0
    ultimo_elemento = numero_de_linhas - 1

    for linha in range(0, numero_de_linhas):
        valores = arr[linha]
        soma_diagonal_principal += valores[linha]
        soma_outra_diagonal += valores[ultimo_elemento - linha]


    return abs(soma_diagonal_principal - soma_outra_diagonal)