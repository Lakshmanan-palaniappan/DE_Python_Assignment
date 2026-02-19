import numpy

def min_max(n, m, matrix=None):
    if matrix is None:
        arr = []
        for i in range(n):
            row = []
            print(f"Enter elements for row {i+1}:")
            for j in range(m):
                val = int(input(f"Element [{i+1},{j+1}]: "))
                row.append(val)
            arr.append(row)
    else:
        arr = matrix

    arr = numpy.array(arr)
    result = numpy.max(numpy.min(arr, axis=1))
    print("Result:", result)
    return result
