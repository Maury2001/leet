# char =[]

# for ch in "tutorialspoint":
#     if ch not in 'aeiou':
#         char.append(ch)


# print(char)

# squares = [x*x for x in range(1,11)]

# result = []
# result.append(squares)
# print(squares)

# list1=[1,2,3]
# list2=[4,5,6]
# CombLst=[(x+y) for x in list1 for y in list2]
# print (CombLst)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy_head = ListNode()
        current = dummy_head

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry

            carry = total // 10
            current.next = ListNode(total % 10)
            
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next

list1 =[2,4,3]
list2 =[5,6,4]
solution = Solution()
result = solution.addTwoNumbers(list1,list2)
print(result)
