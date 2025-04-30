class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        print(count)
        for key in count:
            if count[key] > len(nums)//2:
                return key
        return None
# Time Complexity: O(n)
# Space Complexity: O(n)
print("Majority Element")
print(Solution().majorityElement([3,2,3])) # 3
print(Solution().majorityElement([2,2,1,1,1,2,2])) # 2
print(Solution().majorityElement([1,2,3,4,5,6,7,8,9,10])) # None    