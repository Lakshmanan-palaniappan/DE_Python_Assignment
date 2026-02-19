from util import mutate_string

if __name__ == '__main__':
    s = input("Enter a string: ")
    position = int(input("Enter position: "))
    character = input("Enter new character: ")
    s_new = mutate_string(s, position, character)
    print("Result:", s_new)
