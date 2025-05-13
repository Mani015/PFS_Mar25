

cars = ['innova','maruthi','honda','kia']
# print(id(cars))

bikes = ['hero','bajaj','ktm','honda']
# print(id(bikes))
print()

new = cars

# print(id(new))


cars.append('bmw')

print(cars)
print(new)

# print(new is cars)
print()
new.remove('maruthi')
print('new list :', new)
print('cars list :', cars)


