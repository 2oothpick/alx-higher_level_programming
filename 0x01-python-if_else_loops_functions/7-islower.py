#!/usr/bin/python3
def islower(c):
    lowercase =[]
    for i in range(97,123):
        lowercase.append(f"{i:c}")
        i+=1
    if c in lowercase:
        return True
    else:
        return False

