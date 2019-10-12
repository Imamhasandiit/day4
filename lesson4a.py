#Introducing Lists

motorcycles = ['honda','Yamaha','bajaj']

print(motorcycles)

#Accessing Elements in a List
print(motorcycles[0])

#Updating Elements in a List
motorcycles[0] ='hero'
print(motorcycles)

fruits = []
#print(dir(fruits))
fruits.append ('orange')
#print(fruits)
fruits.append ('mango')
fruits.append ('banana')
print(fruits)

fruits.insert (1, 'apple')
print(fruits)

#print(help(fruits.sort))
fruits.sort()
print(fruits)
print ('After Reverse Sort:')
fruits.sort( reverse = True )
print(fruits)
print ('After Remove :')

fruits.remove('orange')
print(fruits)

print ('After Delete :')
del fruits[0]
print(fruits)
#print(help(fruits.count))

print ('Count numberer occurance:')
#del fruits[0]
print(fruits.count("mango"))



cars= ['honda','yamaha','bmw','audi','audi','audi','honda']

print(cars.count("audi"))
print(cars.index('yamaha'))

print("\n HERE IS THE SORTED LIST:")
print(sorted(cars))
print("\n HERE IS THE main LIST:")
print(cars)
print("\n Total Number of Cars:", end="")
print (len(cars))

print(cars[0:3])

print(cars[2:5])
print(cars[-1])



print(30*'=')
