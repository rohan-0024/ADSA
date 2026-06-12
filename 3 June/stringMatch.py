mainString = "abababc"
subString = "ababc"

def stringMatch(mainString, subString):
    n = len(subString)
    length = len(mainString)
    i = 0
    while n <= length:
        if mainString[i:n] == subString:
            print("Found in index", i)
            return True
        i += 1
        n += 1
    return False


#print(stringMatch(mainString, subString))


def rabinKarp(mainString, subString):
    hash = {'a': 1, 'b': 2, 'c': 3}
    def hashString(String):
        n = len(String) - 1
        hash = {'a': 1, 'b': 2, 'c': 3}
        hashCode = 0
        for i in String:
            hashCode += hash[i] * (10**n)
            n -= 1
        return hashCode
    
    subStringHash = hashString(subString)
    i, j = 0,len(subString) 
    firstMainHash = hashString(mainString[i:j])
    for i in range(len(mainString)-len(subString)+1):
        if subStringHash == firstMainHash:
            return i,True
        firstMainHash -= hash[mainString[i]] * (10 **(len(subString) - 1))
        firstMainHash *= 10
        i += 1
        if j  > len(mainString) - 1:
            break
        firstMainHash += hash[mainString[j]]
        j += 1
        
    return False


print(rabinKarp(mainString, subString))