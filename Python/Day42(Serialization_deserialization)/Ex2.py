# 1.We can perform serialization and deserialization of an object with the respect file by using pickle module
# 2.It is python inbuilt module

# Serialization :
import pickle
Info = [1,2,3,4,5,6]

# sy : pickle.dump(object, file)
# Convert python dict to json formate

# with open('stu.pk','wb') as file:
#     pickle.dump(Info,file)
#
# print('Converted in Bytes')


# Deserialization :
# sy : pickle.load(file)

with open('stu.pk','rb') as file:
    read_bin = pickle.load(file)
    print(read_bin)

print('Succefully read binary files')
# [1, 2, 3, 4, 5, 6]
# Succefully read binary files
