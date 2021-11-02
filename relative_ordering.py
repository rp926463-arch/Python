'''
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. 
Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

'''

arr1 = [2,3,1,3,2,4,6,19,9,2,7]
arr2 = [2,1,4,3,9,6]


#OPt : [2,2,2,1,4,3,3,9,6,7,19]

d = {}
for i in arr1:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

sorted_d = {}
for i in arr2:
    sorted_d[i] = d[i]

sorted_arr1 = []
for key,val in sorted_d.items():
    for i in range(val):
        sorted_arr1.append(key)

remaining_ele = []
for i in arr1:
    if i not in sorted_arr1:
        remaining_ele.append(i)

remaining_ele = sorted(remaining_ele)

sorted_arr1.extend(remaining_ele)

print(sorted_arr1)
