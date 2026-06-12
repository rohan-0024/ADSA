arr = [2,5,4,6,1]

def kedanes(arr):
    curr_sum = arr[0]
    max_sum = arr[0]
    
    for num in range(1, len(arr)):
        curr_sum = max(arr[num], curr_sum + arr[num])
        max_sum = max(max_sum,curr_sum )
        
    return max_sum

def equilibrium_sum(arr):
    total_sum = 0
    left_sum = 0
    
    for num in arr:
        total_sum += num
    
    right_sum = total_sum
        
    for i in range(len(arr)):
        right_sum -= arr[i]
        if right_sum == left_sum:
            return i
        left_sum += arr[i]
        
    return -1
        
        

print("Max Subarray Sum :",kedanes(arr))
print("Equilibrium Index:",equilibrium_sum(arr))