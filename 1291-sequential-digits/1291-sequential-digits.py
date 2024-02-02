class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        result = []
        for i in range(1,10):
            num = i
            next_num = i + 1


            while num <= high and next_num <= 9:
                num = num*10 + next_num

                if low <= num <= high:
                    result.append(num)
                next_num = next_num + 1
        
        result.sort()
        return result