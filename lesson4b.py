#Python For LOOP
"""
Syntax of for Loop

for val in sequence
Body of for
"""

for x in [7,33,5] :
	print(x, end="\t")
	
for x in range(0,99):
	print(x,end="\t")
'''	
for x in range(20):
	print(x,end=",")
	
'''	
for x in range(20,41):
	print(x,end=" ")
	
for x in range(0,100,5):
	print(x,end="\t")
print("\n")
cars= ['honda','yamaha','bmw','audi','audi','audi','honda']
for cars in cars:
	print(cars, end="\t")