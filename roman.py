def int_roman(num):
    roman_map = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }

    roman = ''
    for value in sorted(roman_map.keys(), reverse=True):
        while num >= value:
            roman += roman_map[value]
            num -= value

    return roman

def roman_int(s):
    
    roman ={
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL':40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM':900,
        'M': 1000
    }
    i = 0
    num = 0
    while i < len(s):
        # Check for two-character Roman numeral first
        if i + 1 < len(s) and s[i:i+2] in roman:
            num += roman[s[i:i+2]]
            i += 2
        else:
            # If not, use one-character Roman numeral
            num += roman[s[i]]
            i += 1
    return num
    

    

# Example usage:


        

number = 58
result = int_roman(number)
print(result)

num = "MCMXCIV"
res = roman_int(num)
print(res)

