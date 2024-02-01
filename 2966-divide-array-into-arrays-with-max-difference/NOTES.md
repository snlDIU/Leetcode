![image.png](https://assets.leetcode.com/users/images/904ab84d-6846-4208-90ef-e552d73bdbad_1706806020.5348465.png)

# Intuition
The problem requires dividing an integer array into one or more arrays of size 3, such that each element is in exactly one array, and the difference between any two elements in one array is less than or equal to k. Sorting the array is a crucial step to simplify the process of creating valid arrays.

# Approach
1. Sort the array `nums` to make it easier to form arrays that satisfy the conditions.
2. Iterate through the sorted array in steps of 3 to create chunks of size 3.
3. Check if the difference between the third and second element, as well as the third and first element, is less than or equal to k for each chunk.
4. If any chunk violates the conditions, set the `chunks` list to an empty array.
5. Return the resulting list of arrays or an empty array if it's impossible to satisfy the conditions.

# Complexity
- Time complexity: 
   - Sorting the array takes O(n log n) time, and iterating through the sorted array takes O(n). Thus, the overall time complexity is O(n log n).

- Space complexity: 
   - The space complexity is O(n) as we are creating chunks to store the arrays.


# Code
```
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        chunks = []

        for i in range(0, len(nums), 3):
            chunk = nums[i: i+3]
            chunks.append(chunk)
        print(chunks)

        for chunk in chunks:
            if chunk[2]-chunk[1] > k or chunk[2]-chunk[0] > k:
                chunks = []
                break


        return chunks
```
