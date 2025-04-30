class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        # print(count)
        for key in count:
            # print(key)
            # print(count[key])
            if count[key] == 1:
                return key
        return None
# Time Complexity: O(n)
# Space Complexity: O(n)
print("Single Number")
print(Solution().singleNumber([2,2,1])) # 1
print(Solution().singleNumber([4,1,2,1,2])) # 4 