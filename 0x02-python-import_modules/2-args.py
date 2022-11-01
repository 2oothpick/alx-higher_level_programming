#!/usr/bin/python3
if __name__ == "__main__":
    import sys 

if sys.argv == 1:
    print(f"{len(sys.argv)} argument:")
if sys.argv == 0:
    print(f"{len(sys.argv)} argument.")
else:
    print(f"{len(sys.argv)} arguments:")

for i in range(len(sys.argv)):
    print(f"1: {sys.argv[i]}")
