def Solution(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target-num], i] # MOST IMPORTANT LINE
        d[num] = i
    return []

target = 9
nums = [2,0,7,15]  # [0,1]
print(Solution(nums, target)) # [0,1]
[2,7,0,11]

# Code Description:
# 1. Create an empty dictionary
# 2. Loop through the list of numbers
# 3. Check if the target minus the number is in the dictionary
# 4. If it is, return the index of the target minus the number and the index of the current number
# 5. If it is not, add the number to the dictionary with its index
