class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # height is always the lesser of the two numbers
        # width is just substracting the indices

        #make a list of all of the areas, and then just apply the max function to it

        max_area = 0
        pointer1 = 0
        pointer2 = len(heights) - 1

        for i in range(len(heights)):
            width = abs(pointer2 - pointer1)
            height = min(heights[pointer1], heights[pointer2])
            if heights[pointer1] < heights[pointer2]:
                pointer1 += 1
            else:
                pointer2 -= 1
            max_area = max(max_area, width * height)
        
        return max_area
