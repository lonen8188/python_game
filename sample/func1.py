def  calc(x, y, z):
    print(x, y, z)
    return  x + y + z

print(calc(10, 20, 30))
print(calc(x=10, y=20, z=30))
print(calc(y=20, x=10, z=30))
result = calc(10, y=20, z=30)
print(result)
