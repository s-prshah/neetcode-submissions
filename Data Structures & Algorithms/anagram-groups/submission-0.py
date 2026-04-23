class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagrams = []
        anagram_tracker = {}
        def find_anagram_frequency(s : str):
            char_freq = [0] * 26
            for i in range(len(s)):
                char_freq[ord(s[i]) - ord('a')] += 1
            return char_freq

        for i in range(len(strs)):
            char_freq = tuple(find_anagram_frequency(strs[i]))
            if char_freq in anagram_tracker:
                anagram_tracker[char_freq].append(strs[i])
            else:
                anagram_tracker[char_freq] = [strs[i]]
        
        for grouping in anagram_tracker:
            groupAnagrams.append(anagram_tracker[grouping])
        
        return groupAnagrams

            

        