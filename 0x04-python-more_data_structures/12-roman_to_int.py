#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return None
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
            "D": 500, "M": 1000}
    i = 0
    sum = 0
    while i < len(roman_string):
        sum += my_dict.get(roman_string[i])
        if len(roman_string)-1 != i:
            if roman_string[i] == "I" and (roman_string[i + 1] == "V" 
                    or roman_string[i + 1] == "X"):
                sum -= 2
            elif roman_string[i] == "X" and (roman_string[i+1] == "C"
                    or roman_string[i+1] == "D" or roman_string[i+1] == "L"
                    or roman_string[i+1] == "M"):
                sum -= 20
            elif roman_string[i] == "C" and (roman_string[i+1] == "D" or
                    roman_string[i+1] == "M"):
                sum -= 200

        i += 1

    return sum
