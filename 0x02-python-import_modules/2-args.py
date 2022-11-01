#!/usr/bin/python3
if __name__ == "__main__":
    import sys 
    number = len(sys.argv) - 1

    if number == 1:
        print(f"{number} argument:")
    if number == 0:
        print(f"{number} argument.")
    else:
        print(f"{number} arguments:")

    for i in range(number):
        print(f"{i+1}: {sys.argv[i+1]}")
        