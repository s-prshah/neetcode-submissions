class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        longest_str = 0
        cur_str = 0
        cur_chars = set()
        l, r = 0, 0

        while r < len(s):
            print(cur_chars)
            if s[r] not in cur_chars:
                cur_str += 1
                print(longest_str)
                cur_chars.add(s[r])
                r += 1
            else:
                longest_str = max(longest_str, cur_str)
                cur_chars.remove(s[l])
                l += 1
                cur_str -= 1

        return max(longest_str, cur_str)






            