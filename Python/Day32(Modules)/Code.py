
# def difference of sum(n,m)
#
# 	The function accepts two integers n,m as arguemnts. Find the sum of all numbers in range from 1 to m(both inclusive)
# 	that are not divisible by n.Return difference between sum of integers not divisible by n with sum of numbers divisibe by n.
#
# 	Assumptions :
# 		n > 0 and  m > 0
# 		Sum lies between integral range
#
# 	Case : 1
# 		Example : Input n = 4, m = 20
# 	 	 Output 90
#
# 	Explanation :
# 		. Sum of numbers divisible by 4 are 4 + 8 + 12 + 16 + 20 = 60
# 		. sum of numbers not divisible by 4 are 1 + 2 + 3 + 5 + 6 + 7 + 9 + 11 + 13 + 14 + 15 + 17 + 18 + 19 = 150
# 		. Difference 150 - 60 = 90
#
# 	Case : 2
# 		Sample input : n = 3, m = 10
# 		Output : 19



def differece(n,m):

    divisable = 0

    not_divisable = 0
    l1 = []
    l2 = []
    for i in range(1,m+1):

        if i % n==0:

            divisable += i
            l1.append(i)



        # 3 % 3 == 0
        else:
            not_divisable += i
            l2.append(i)
    print()
    print(not_divisable - divisable)
    print(l1)
    print(l2)

differece(3,10)
