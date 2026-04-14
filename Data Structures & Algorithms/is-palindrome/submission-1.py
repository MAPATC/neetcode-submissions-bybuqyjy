class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for w in s:
            if w.isalnum(): # Проверяет не спец символ ли это(только буквы и цифры)
                newStr += w.lower()
        return newStr == newStr[::-1]