class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        reversed_sarray = [char.lower() for char in s if char.isalnum()]
        return reversed_sarray == reversed_sarray[::-1]
    

# Time Complexity: O(n)
# Space Complexity: O(n)
print("Valid Palindrome")
print(Solution().isPalindrome("dad")) # True
print(Solution().isPalindrome("A man, a plan, a canal: Panama")) # True
print(Solution().isPalindrome("race a car")) # False
print(Solution().isPalindrome(" ")) # True