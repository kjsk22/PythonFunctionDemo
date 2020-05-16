def factorial(n):
    result = 1
    while n > 0:
        a = n
        result = result * a
        n -= 1
    return result
    
def cylindervolume(radius, height):
    volume = 3.14 * (radius ** 2) * height
    return volume

z = factorial(10)
print(z)

vol = cylindervolume(2, 3)
print(vol)
