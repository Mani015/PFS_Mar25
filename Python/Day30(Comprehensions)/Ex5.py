

x = [1,2,[3,4,5],6,7,8,[10,11,12,13],'vinay',{11,12,13},('one','two','three')]

# y= [1,2,3,4,5,6,7,8,10,11,12,13,'vinay',11,12,13]


# l1 = []
#
# for i in x:
#     for j in i:
#         l1.append(j)
#
# print(l1)


def Sequence(x):

    new_list = []

    for i in x:

        if isinstance(i,(list,set,tuple)):
            new_list.extend(i)

        else:
            new_list.append(i)


    print(new_list)

Sequence(x)
# [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 'vinay', {11, 12, 13}]
