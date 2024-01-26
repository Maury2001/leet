def atoi(s):
    s = s.lstrip()

    if not s:
        return 0

    sign = 1
    if s[0] in ['+', '-']:
        sign = -1 if s[0] == '-' else 1
        s = s[1:]

    result = 0
    for char in s:
        digit = ord(char) - ord('0')
        if 0 <= digit <= 9:
            result = result * 10 + digit
        else:
            break

    result = sign * result
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    result = max(min(result, INT_MAX), INT_MIN)

    return result


s="   -42"
print(atoi(s))
print(type(atoi(s)))
                    
        
        