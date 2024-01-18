# Climb Stairs Dynamic Programming Note

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        previous, current = 1, 1
        for i in range(2, n+1):
            temp     = current
            current  = previous + current
            previous = temp
        return current
``` 
This code is designed to help determine the number of ways one can climb a staircase with a given number of steps. The approach used in this code is known as "dynamic programming."

## How It Works:

### Base Case:

If there's only one step (when n is 1), the function returns 1, as there's only one way to climb one step.
Dynamic Programming Loop:

For more than one step, the code uses two variables (previous and current) to keep track of the number of ways to climb the stairs at the previous step and the current step.
It iterates through a loop starting from step 2 up to the total number of steps (n).
In each step, it updates the current variable by adding the previous and current values.
It also updates the previous variable to the old current value.

### Result:

After completing all steps, the function returns the final answer, stored in the current variable. This value represents the total number of ways to climb the given number of steps.

## Summary:

In simple terms, the code is like a smart friend helping you figure out how many different ways you can climb a staircase, and it does it in a way that's efficient and fast!

---

*Note: This Markdown file serves as documentation for the code.*
