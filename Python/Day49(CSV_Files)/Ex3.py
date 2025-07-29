# Read CSV file

import csv

# with open('emp1.csv','r') as file:
#
#     new_read = csv.reader(file)
    # print(type(new_read))
    #<class '_csv.reader'>

    # print(new_read)<_csv.reader object at 0x000001D45606BC40>

    # for read in new_read:
    #     for data in read:
    #         print(data)
    #     print('//////////////////////')


# drop csv file
import os
print(os.remove('emp1.csv'))

