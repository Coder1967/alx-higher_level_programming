#!/usr/bin/python3

def remove_char_at(str, n):
    st = ""
    i = 0
    l = len(str) - 1

    while i < l:
        if i == n:
            continue
        else:
            st += str[i]
        i += 1
    return (st)


print(remove_char_at("Best School", 3)) 
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0)) 
print(remove_char_at("School", 10)) 
print(remove_char_at("Python", -2))
