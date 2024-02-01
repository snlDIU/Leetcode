# Intuition
The problem requires generating a list of strings based on certain conditions for each index `i` in the range from 1 to `n`. The conditions involve checking divisibility by 3, 5, or both.

# Approach
1. Initialize an empty list `new_item` to store the resulting strings.
2. Iterate through the range from 1 to `n`.
3. Check the following conditions:
   - If `i` is divisible by both 3 and 5, append "FizzBuzz" to the list.
   - If `i` is divisible by 3, append "Fizz" to the list.
   - If `i` is divisible by 5, append "Buzz" to the list.
   - If none of the above conditions are true, append the string representation of `i` to the list.
4. Return the list `new_item` containing the generated strings.

# Complexity
- Time complexity: $$O(n)$$ as we iterate through the range from 1 to `n`.
- Space complexity: $$O(n)$$ as we store the resulting strings in the `new_item` list.

# Code
```python

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer
```

​
