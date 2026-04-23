class Solution:

    def encode(self, strs: List[str]) -> str:
        to_return = ""
        for s in strs:
            to_return = to_return + str(len(s)) + "#" + s
        print(to_return)
        return to_return

    def decode(self, s: str) -> List[str]:
        to_return = []

        cur_str = ""
        i = 0
        while i < len(s):
            j = i
            num = ""
            while s[j] != "#":
                num += s[j]
                j+= 1
            num = int(num)
            i = j + 1
            j = 0
            while j < num:
                cur_str += s[i + j]
                j += 1
            to_return.append(cur_str)
            cur_str = ""
            i = i + j
        return to_return
            
            
