
# from Python to Json
import pickle

s1 = {'Name' : 'jithendra','age' : 20}

ser = pickle.dumps(s1)
# print(ser)
# b'\x80\x04\x95 \x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04Name\x94\x8c\tjithendra\x94\x8c\x03age\x94K\x14u.'


# Json to python

des = pickle.loads(ser)
print(des)
# {'Name': 'jithendra', 'age': 20}
