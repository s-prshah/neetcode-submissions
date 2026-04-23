class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = "".join(char for char in s if char.isalnum())
        print(s)

        start = 0
        end = len(s) - 1
        print(len(s))

        while start <= end:
            print(start)
            print(end)
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
        