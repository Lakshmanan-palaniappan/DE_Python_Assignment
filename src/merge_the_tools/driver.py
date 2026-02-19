from util import merge_the_tools
if __name__ == '__main__':
    string = input("Enter names (no spaces): ")
    k = int(input("Enter group size: "))
    parts = merge_the_tools(string, k)
    for p in parts:
        print(p)