'''
125. Valid Palindrome
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleared = ""
        for content in s:
            if content.isalnum():
                cleared += content
        
        cleared = cleared.lower()
        
        return cleared == cleared[::-1]

solution = Solution()
ans1 = solution.isPalindrome("A man, a plan, a canal : Panama")
print(ans1)
ans2 = solution.isPalindrome("race a car")
print(ans2)