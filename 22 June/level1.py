# calculate move count for tower of hanoi, a^b and GCD(a,b)

def toh(n: int) -> int:
    if n <= 0:
        return 0
    else:
        return (2 * toh(n-1)) + 1
    
def power(a: int, b: int) -> int:
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

def GCD(a: int , b:int) -> int:
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

print("Hanoi:", toh(8))
print("Power:", power(3, 6))
print("GCD:", GCD(3,6))