#perform combination and permutation and no. of subsets

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: return n * factorial(n-1)
    
def combination(n: int, k: int) -> int:
    if k == 0 or k == n:
        return 1
    return combination(n - 1, k - 1) + combination(n - 1, k)

def permutation(n: int, k: int) -> int:
    if k == 0:
        return 1
    return n * permutation(n - 1, k - 1)

def subsets(n: int) -> int:
    if n == 0:
        return 1
    return 2 * subsets(n - 1)

print("Combinations:", combination(7, 3)) 
print("Permutations:", permutation(7, 3))
print("Subsets:", subsets(7))
