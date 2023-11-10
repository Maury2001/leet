def lengthOfLongestSubstring(self, s):
        char_index_map = {}
        max_len = 0
        start = 0

        for end in range(len(s)):
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                start = char_index_map[s[end]] + 1

            char_index_map[s[end]] = end
            max_len = max(max_len, end - start + 1)

        return max_len