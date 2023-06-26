def roman_to_int(roman_string):
    sum = 0
    if "IV" in roman_string:
        roman_string = roman_string.replace("IV", "")
        sum = sum + 4
    if "IX" in roman_string:
        roman_string = roman_string.replace("IX", "")
        sum = sum + 9
    if "XL" in roman_string:
         roman_string = roman_string.replace("XL", "")
         sum = sum + 40
    if "XC" in roman_string:
         roman_string = roman_string.replace("XC", "")
         sum = sum + 90
    if "CD" in roman_string:
         roman_string = roman_string.replace("CD", "")
         sum = sum + 400
    if "CM" in roman_string:
         roman_string = roman_string.replace("CM", "")
         sum = sum + 900
    dict_romans = {}
    dict_romans['I'] = 1
    dict_romans['V'] = 5
    dict_romans['X'] = 10
    dict_romans['L'] = 50
    dict_romans['C'] = 100
    dict_romans['D'] = 500
    dict_romans['M'] = 1000
    splitted_roman = [char for char in roman_string]
    for i in splitted_roman:
        sum = sum + dict_romans[i]
    return sum

    
