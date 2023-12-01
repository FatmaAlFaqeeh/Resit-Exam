def is_pangram(input_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    input_string = input_string.lower()

    for char in alphabet:

        if char not in input_string:
            return False
    else:
        return True
