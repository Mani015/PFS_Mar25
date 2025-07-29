
ob1 = map(lambda x : x*2, [1,2,3,4,5,6,7,8,9,10])



while True:

    try:
        var = next(ob1)
        print(var)
    except StopIteration:
        print('Iteration Stop')
        break




