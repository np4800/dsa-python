class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize variables to store the maximum sum and current sum
        max_sum = float('-inf')
        print("Initial Max Sum:", max_sum)
        current_sum = 0

        # Iterate through the array
        # print("Current Number", "Current Sum","Max Sum")
        # print("------------------------------------------------")
        for num in nums:
            # Add the current number to the current sum
            current_sum += num
            # Update the maximum sum if the current sum is greater
            # print(num, current_sum, max_sum)
            # print("Current Sum Before Update:", current_sum)
            # print("Max Sum Before Update:", max_sum)
            max_sum = max(max_sum, current_sum)
            # print("max_sum:", max_sum)
            # If the current sum becomes negative, reset it to 0
            if current_sum < 0:
                current_sum = 0
            # print("---")
            print(num, current_sum, max_sum)
            # print("Current Sum:", current_sum)
            # print("--------------------")
        return max_sum
# Example usage:
nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
print(solution.maxSubArray(nums))  # Output: 6
# The maximum subarray is [4,-1,2,1] with sum 6
# The expected output is 6
nums = [5,4,-1,7,8]
solution = Solution()
print(solution.maxSubArray(nums))  # Output: 23
# The maximum subarray is [5,4,-1,7,8] with sum 23

