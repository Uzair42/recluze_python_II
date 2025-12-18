def squre(n):
    return n**n
def cube(n):
    return n**3

def summation(low,high,method):
    sum=0
    for i in range(high):
       sum += method(i)
    return sum

print(summation(1,2,squre))
print(summation(1,2,cube))