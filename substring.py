string = "pwwkew"

# lst=[]

# for letter in string:
#     if letter not in lst:
#         lst.append(letter)
#     else:
#         break
     


# print(lst)
# print(len(lst))
class Sol:
 def lengthOfLongestSubstring(self, s):
        maxLen = 1
        if s == '':
            return 0                      # Dealing with one edge case
        for i in range(len(s)):
            substring = s[i]              # Initialising the substring
            for j in range(i+1, len(s)):  # Starting to append characters to substring from i+1
                if s[j] not in substring: # As long as its not repeating. "not in" can be used to check if the character isn't already there in the substring
                    substring = substring + s[j]
                    maxLen = max(maxLen, len(substring)) # Updating maxLen if it is greater than the existing maxLen
                else:
                    break
        return maxLen


solulu =Sol()
res = solulu.lengthOfLongestSubstring(string)
print(res)