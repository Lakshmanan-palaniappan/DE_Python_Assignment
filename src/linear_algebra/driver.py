from util import lin_alg


if __name__ == "__main__":
    n = int(input("Enter N: "))
    result = lin_alg(n)
    print("Determinant:", result)
