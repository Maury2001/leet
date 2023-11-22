class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        lst = nums1 + nums2
        s = sorted(lst)
        n = len(lst)

        # mid = len(sort) // 2
        # res = (sort[mid] + sort[~mid]) / 2

        return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None

    

num1 = [1,2]
num2 = [3,4]

sol = Solution()
print( sol.findMedianSortedArrays(num1, num2))