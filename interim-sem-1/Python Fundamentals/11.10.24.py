
def getsum(n):
    sum=0
    for digit in str(n):
        sum+=int(digit)
    return sum

n=int(input("Enter A Number:"))
d=getsum(n)
print(d)