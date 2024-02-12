class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dic = defaultdict(int)
        for c in nums:
            dic[c] += 1
        
        maxV = max(dic.values())
        value = [i for i in dic if dic[i]== maxV]     
        # print(dic)
        # print(value)
        
        return(value[0])