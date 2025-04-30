class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            left_temp = s[left]
            right_temp = s[right]
            s[left] = right_temp
            s[right] = left_temp
            # Alternatively, you can use tuple unpacking:
            # s[left], s[right] = s[right], s[left]
            # Or use a temporary variable:
            # temp = s[left]
            # s[left] = s[right]    
            left = left + 1
            right = right - 1
        return s
# Time Complexity: O(n)
# Space Complexity: O(n)
print("Reverse String")
print(Solution().reverseString(["h","e","l","l","o"])) # ["o","l","l","e","h"]