def factorial(n): #calculates the factorial for n
    result = 1
    while n > 0: # repeat this until n becomes 1
        a = n
        result = result * a
        n -= 1
    return result
    
def cylindervolume(radius, height): # take radius and height and calculate volume of cylinder using forumla Pi*(r)^2*h
    volume = 3.14 * (radius ** 2) * height
    return volume

z = factorial(10)
print(z)

vol = cylindervolume(2, 3)
print(vol)
