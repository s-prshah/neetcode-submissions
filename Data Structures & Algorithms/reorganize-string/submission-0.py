class Solution:
    def reorganizeString(self, s: str) -> str:
        frequency = Counter(s)
        
        to_return = ""
        prev = None

        maxHeap = [[-count, char] for char, count in frequency.items()]
        heapq.heapify(maxHeap)

        while prev or maxHeap:
            if prev and not maxHeap:
                return ""
            
            count, char = heapq.heappop(maxHeap)
            count += 1
            to_return += char

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if count != 0:
                prev = [count, char]

        return to_return
            

        
