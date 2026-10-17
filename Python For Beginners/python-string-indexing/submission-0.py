def print_first_char(word: str) -> None:
    pass
    print(word[0])

def print_second_char(word: str) -> None:
    pass
    print(word[1])

def print_last_char(word: str) -> None:
    pass
    if len(word) == 3:
        print(word[2])
    if len(word) > 3:
        print(word[4])


# do not modify below this line
print_first_char("hello")
print_second_char("hello")
print_last_char("hello")

print_first_char("yay")
print_second_char("yay")
print_last_char("yay")
