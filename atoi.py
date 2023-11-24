def atoi(s):
    s= s.lstrip()
    
    if not s :
        return 0
    
    sign =1 
    if s[0] in ['+', '-']:
        sign = -1 if s[0] == '-' else 1
        s= s[1:]
        
    result=0
    for char in s:
        if char.isdigit():
            result = result* 10+ int(char)
        
        else:
            break
        
    result = sign * result
    result = max(min(result, 2**31 -1), -2**31)
    
    return result

s="   -42"
print(atoi(s))
                    
        
        