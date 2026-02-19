import numpy

def mean_var_std(n, m, matrix=None):
    arr = []
    if matrix is None:
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
    print("Mean (axis=1):", numpy.mean(arr, axis=1))
    print("Variance (axis=0):", numpy.var(arr, axis=0))
    print("Std Dev:", round(numpy.std(arr), 11))
    return numpy.mean(arr, axis=1), numpy.var(arr, axis=0), round(numpy.std(arr), 11)
