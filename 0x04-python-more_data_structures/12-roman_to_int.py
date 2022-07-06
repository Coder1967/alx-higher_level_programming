#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    s = roman_string.copy()
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
            "D": 500, "M": 1000}
    i = 0
    sum = 0
    while i < len(s):
        sum += my_dict.get(s[i])
        if len(s)-1 != i:
            if s[i] == "I" and (s[i+1] == "V" or s[i + 1] == "X"):
                sum -= 2
            elif s[i] == "X" and (s[i+1] == "C" or s[i+1] == "D" or s[i+1] == "L"
                    or roman_string[i+1] == "M"):
                sum -= 20
            elif s[i] == "C" and (roman_string[i+1] == "D" or s[i+1] == "M"):
                sum -= 200

        i += 1

    return sum
