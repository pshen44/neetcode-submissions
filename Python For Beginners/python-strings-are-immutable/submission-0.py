def remove_fourth_character(word: str) -> str:
    i = word[:3]
    s = word[4:]
    return i + s


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
