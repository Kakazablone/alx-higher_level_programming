#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_numerals = {'M': 1000, 'D': 500, 'C': 100,
                      'L': 50, 'X': 10, 'V': 5, 'I': 1}
    roman_total = 0
    prev_roman_val = 0
    for numeral in reversed(roman_string):
        roman_val = roman_numerals[numeral]
        if roman_val < prev_roman_val:
            roman_total -= roman_val
        else:
            roman_total += roman_val
        prev_roman_val = roman_val
    return roman_total
