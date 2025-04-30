class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        total = (n * (n + 1)) // 2
        sum_nums = sum(nums)
        if sum_nums == total:
            return 0
        elif total - sum_nums < 0:
            return 0
        return total - sum_nums
# Time Complexity: O(n)
# Space Complexity: O(1)
print("Missing Number")
print(Solution().missingNumber([3,0,1])) # 2
print(Solution().missingNumber([0,1])) # 2
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1])) # 7
print(Solution().missingNumber([0])) # 1
print(Solution().missingNumber([1])) # 0
print(Solution().missingNumber([2])) # 0
print(Solution().missingNumber([2,3])) # 0
print(Solution().missingNumber([2,3,4])) # 0
print(Solution().missingNumber([2,3,4,5])) # 0
print(Solution().missingNumber([2,3,4,5,6])) # 0
print(Solution().missingNumber([2,3,4,5,6,7])) # 0
print(Solution().missingNumber([2,3,4,5,6,7,8])) # 0
print(Solution().missingNumber([2,3,4,5,6,7,8,9])) # 0
print(Solution().missingNumber([2,3,4,5,6,7,8,9,10])) # 0
print(Solution().missingNumber([2,3,4,5,6,7,8,9,10,11])) # 0
print(Solution().missingNumber([2,3,4,5,6,7,8,9,10,11,12])) # 0
print(Solution().missingNumber([2,3,4,5,6,7,8,9,10,11,12,13])) # 0
print(Solution().missingNumber([2,3,4,5,6,7,8,9,10,11,12,13,14])) # 0