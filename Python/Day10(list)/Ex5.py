
# clear : removes the all items in given list, it keeps empty list
# sy : list.clear()

num = [1,2,3,4,5,6,7,8,9,10]
# print('before list : ', num)
# before list :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num.clear()
# print('After list :',num)
# After list : []


# copy : returns into a new list

choco = ['diary milk','oreo','kitkat','5star']

frnd = choco.copy()
print(choco) #['diary milk', 'oreo', 'kitkat', '5star']
print(frnd)  # ['diary milk', 'oreo', 'kitkat', '5star']

print(id(frnd))
print(id(choco))
