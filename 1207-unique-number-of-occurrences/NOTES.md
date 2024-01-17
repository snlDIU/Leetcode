# Intuition
 The problem requires determining whether the number of occurrences of each unique element in an input array is itself unique.

# Approach
A common approach is to use a dictionary to count the occurrences of each element in the array. Then, we check if the counts themselves are unique. 

1. Initialize an empty dictionary (`hashmap`) to store the count of occurrences for each unique element.
2. Iterate through the input array (`arr`).
   - For each element in `arr`, check if it is already present in `hashmap`.
      - If yes, increment the count.
      - If no, add the element to `hashmap` with a count of 1.
3. Create a set (`hashset`) to keep track of unique counts.
4. Iterate through the values in `hashmap`.
   - For each count, check if it is already present in `hashset`.
      - If yes, return False (indicating non-unique counts).
      - If no, add the count to `hashset`.
5. If the loop completes without returning False, return True (indicating unique counts).

# Complexity
- Time complexity: O(n), where n is the length of the input array `arr`. The loop through `arr` takes linear time.
- Space complexity: O(n), where n is the length of the input array `arr`. The space required for `hashmap` and `hashset` is proportional to the number of unique elements in `arr`.
​
