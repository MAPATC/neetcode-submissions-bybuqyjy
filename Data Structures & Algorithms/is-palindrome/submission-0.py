class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for w in s:
            if w.isalnum():
                newStr += w.lower()
        return newStr == newStr[::-1]