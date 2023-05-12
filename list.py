list1 = [1,2,3,4,1.2,3.6,'abc','pqr']
print("The list is : ",list1)
print(len(list1))
print(list1[2])
print(list1[2:6])
list1[2]=10
print(list1)
list2=[1,2,3,4,5]
list2.append(9)
list2.append(10)
list2.append(list1)
print(list2)
print(len(list2))
print(list1[-6:-1])
list3=[1,2,3,4,5]
list4=[7,8,9]
list3.extend(list4)
print("The new list is : ", list3)
list5=list3+list4
print(list5)