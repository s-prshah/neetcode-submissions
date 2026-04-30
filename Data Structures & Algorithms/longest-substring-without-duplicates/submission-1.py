class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0
        cur_length = 0

        seen = set()

        while r < len(s) and l < len(s):
            if l > r:
                r = l
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                cur_length += 1
                longest = max(cur_length, longest)
            else:
                cur_length -= 1
                seen.remove(s[l])
                l += 1
            print(seen)
            print(l)
            print(r)

        return longest






            