def square(num): return num**2
#square = lambda num : num**2
numbers=[1,2,3,4,5]
result = list(map(square,numbers))
#result = list(map(lambda,numbers))
print(result)