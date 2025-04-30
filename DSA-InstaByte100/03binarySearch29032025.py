class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target: # True, then you have to search in the left half
                high = mid - 1
            else: # False, then you have to search in the right half
                low = mid + 1
        return -1
# Test cases
s = Solution()
print(s.search([-1,0,3,5,9,12], 9)) # Output: 4
print(s.search([-1,0,3,5,9,12], 2)) # Output: -1
print(s.search([], 0)) # Output: -1
print(s.search([1], 0)) # Output: -1
print(s.search([1], 1)) # Output: 0
print(s.search([1,2,3,4,5], 3)) # Output: 2
print(s.search([1,2,3,4,5], 6)) # Output: -1
print(s.search([1,2,3,4,5], 1)) # Output: 0
print(s.search([1,2,3,4,5], 5)) # Output: 4
print(s.search([1,2,3,4,5], 2)) # Output: 1
print(s.search([1,2,3,4,5], 4)) # Output: 3
print(s.search([1,2,3,4,5], 0)) # Output: -1
print(s.search([1,2,3,4,5], 7)) # Output: -1