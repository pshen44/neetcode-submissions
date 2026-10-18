def add_two_numbers() -> int:
    line = input()
    list_strings = line.split(",")
    list_integers = []
    for string in list_strings:
        list_integers.append(int(string))
    total = 0
    for integer in list_integers:
        total += integer
    return total


    


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
