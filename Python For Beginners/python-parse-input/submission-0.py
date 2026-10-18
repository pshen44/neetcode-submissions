from typing import List

def read_integers() -> List[int]:
    string_list = input()
    splitter = string_list.split(",")
    sneaky_list = []
    for i in splitter:
        sneaky_list.append(int(i))
    return sneaky_list
    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
