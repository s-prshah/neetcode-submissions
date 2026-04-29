class Solution:
    def longestPalindrome(self, s: str) -> str:
        return_Index = 0
        return_length = 0

        for i in range(len(s)):
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > return_length:
                    return_Index = left
                    return_length = right - left + 1
                left -= 1
                right += 1
            
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > return_length:
                    return_Index = left
                    return_length = right - left + 1
                left -= 1
                right += 1
            
        return s[return_Index : return_Index + return_length]

        