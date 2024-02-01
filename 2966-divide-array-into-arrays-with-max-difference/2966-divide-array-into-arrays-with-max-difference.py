class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        chunks = []
        
        if len(nums) % 3 != 0:
            return []
        
        for i in range(0, len(nums), 3):
            chunk = nums[i: i + 3]
            chunks.append(chunk)
        print(chunks)

        for chunk in chunks:
            if chunk[2]-chunk[1] > k or chunk[2]-chunk[0] > k:
                chunks = []
                break


        return chunks