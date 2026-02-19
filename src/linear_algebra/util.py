import numpy


def lin_alg(n, matrix=None):
    arr = []
    if matrix is None:
        for i in range(n):
            row = []
            print(f"Enter elements for row {i+1}:")
            for j in range(n):
                val = float(input(f"Element [{i+1},{j+1}]: "))
                row.append(val)
            arr.append(row)
    else:
        arr = matrix
    arr = numpy.array(arr)
    det = numpy.linalg.det(arr)
    return round(det, 2)
