name = "racecar"
pal = name [: : -1]

print(pal)

if (name == pal):
    print('palindrome')
else:
    print('not palindrome')


def palindrome_int(n):
    
    no = str(n)
    
    if no == no[::-1]:
        return "number is palindrome"
        
    else:
       return "number is not palindrome"
        
sample=121

result= palindrome_int(sample)

print(result)
        