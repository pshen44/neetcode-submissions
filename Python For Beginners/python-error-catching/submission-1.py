def divide_numbers(a: str, b: str) -> None:
    try:
        list_strings = (a, b)
        list_integers = []
        for string in list_strings:
            list_integers.append(int(string))

        result = list_integers[0] / list_integers[1]
        print(result)
    except Exception as error:
        print("An error occurred:", error)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
