num = -1234

print(str(num)[::-1])

def reverse(x):
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    # Handle the sign of the integer
    sign = -1 if x < 0 else 1
    x *= sign

    # Reverse the digits
    reversed_x = int(str(x)[::-1])

    # Apply the sign to the reversed integer
    reversed_x *= sign

    # Check if the result is within the 32-bit signed integer range
    if reversed_x < INT_MIN or reversed_x > INT_MAX:
        return 0

    return reversed_x

print(reverse(-1234))

def reversed(x):
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    # Handle the sign of the integer
    sign = -1 if x < 0 else 1
    x *= sign

    # Reverse the digits
    reversed_x = 0
    while x != 0:
        pop = x % 10
        x //= 10

        # Check for integer overflow before updating the reversed integer
        if reversed_x > (INT_MAX - pop) // 10:
            return 0

        reversed_x = reversed_x * 10 + pop

    # Apply the sign to the reversed integer
    reversed_x *= sign

    return reversed_x