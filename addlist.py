list1 =[2,4,3]
list2 =[5,6,4]

print(list1)
list1str = ''.join([str(i) for i in list1])
list2str = ''.join([str(i) for i in list2])

list1int =(int(list1str[::-1]))
list2int =(int(list2str[::-1]))

resultlist=[]

result =(list1int+ list2int)
resultstr= str(result)
reversedresult = resultstr[::-1]
print(reversedresult)

digits = [int(d) for d in str(reversedresult)]
print(digits)

# for i in reversedresult:
#     resultlist.append(i)

# print(resultlist)
