class Solution(object):
    def addTwoNumbers(self, l1, l2):

       list1str = ''.join([str(i) for i in l1])
       list2str = ''.join([str(i) for i in l2])

       list1int =(int(list1str[::-1]))
       list2int =(int(list2str[::-1]))

       resultlist=[]

       result =(list1int+ list2int)
       resultstr= str(result)
       reversedresult = resultstr[::-1]
       print(reversedresult)

       digits = [int(d) for d in str(reversedresult)]
       return digits
    

list1 =[2,4,3]
list2 =[5,6,4]
solution = Solution()
result = solution.addTwoNumbers(list1,list2)
print(result)
