
x = [9,7,[2,3,4,5,[-3,4,-5,6,-7,8],[10,11,12,13,14,15],'nani','melody'],[4,5,6,7,8],[9,8,7,6,5]]

print(x)

print(max(x[2][5]))
# 15


# compare of both nested list max values
# [-3,4,-5,6,-7,8],[10,11,12,13,14,15]

print(max(x[2][4]) > max(x[2][5]))
# False

# convert into upper case

print(x[-3][-1][:3].upper())
# MEL


