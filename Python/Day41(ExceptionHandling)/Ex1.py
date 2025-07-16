
# Add two numbers

# Num1  = int(input('Enter the 1st number : '))
l1 = ['Yogi','sai charan','simha','suresh','ujwala','sonia','madhuri','pasand']

try:
    # Num2 = int(input('Entet the 2nd number : '))
    # Sum = Num1 / Num2
    # print(Sum)
    print(l1[10])

except BaseException:
    print('I am Parent class of all exceptions')

except ZeroDivisionError as Zero:
    print(Zero, 'Occured')



except IndexError:
    print('Index error occured')

except ValueError as Value:
    print(Value,'occured')


except:
    print('Default Except Must be include in your program')


else:
    print("Successfully execute")

finally:
    print('Everytime will execute for the understandable ')