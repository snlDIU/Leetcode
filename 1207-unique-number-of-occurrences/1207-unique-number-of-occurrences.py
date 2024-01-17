class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Create a dictionary to store the count of occurrences for each element in arr
        hashmap = {}

        # Count the occurrences of each element in arr
        for num in arr:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        # Check if there are any unique occurrences
        hashset = set()

        for count in hashmap.values():
            if count in hashset:
                return False
            else:
                hashset.add(count)
        
        return True
