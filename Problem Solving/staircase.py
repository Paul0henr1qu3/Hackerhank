# Complete the staircase function below.
def staircase(n):
    for cerquilhas in range(1, n + 1):
        espacos = n - cerquilhas
        print(" " * espacos + "#" * cerquilhas)