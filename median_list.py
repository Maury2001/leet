import statistics

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        lst = nums1 + nums2
        sort = sorted(lst)

        median = statistics.median(sort)

        return median
    
num1 = [1,3]
num2 = [2]

sol = Solution()
print( sol.findMedianSortedArrays(num1, num2))
