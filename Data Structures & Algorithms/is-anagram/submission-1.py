class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        anagram_tracker = {}

        # dictionary tracking all letters in word and their counts
        for i in range(len(s)):
            if s[i] in anagram_tracker:
                anagram_tracker[s[i]] += 1
            else:
                anagram_tracker[s[i]] = 1

        for i in range(len(t)):
            if t[i] in anagram_tracker and anagram_tracker[t[i]] > 0:
                anagram_tracker[t[i]] -= 1
            else:
                return False
        return True
        
        


        