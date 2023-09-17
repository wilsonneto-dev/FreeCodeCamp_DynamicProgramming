# FreeCodeCamp_DynamicProgramming

Just practicing DP

Video link:
https://www.youtube.com/watch?v=oFkDldu3C_4

### Introduction

DP is used when you see a problem that can be **broken** down into **smaller subproblems**, and the subproblems are **overlapping**.

### Fibonacci

```python
# naive approach
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)
```

```python
#DP approach / memoisation
class Solution:
    def fib(self, n: int, cache: {} = None) -> int:
        if cache == None: cache = { 0: 0, 1: 1 }

        if n in cache: return cache[n]

        result = self.fib(n-1, cache) + self.fib(n-2, cache)
        cache[n] = result

        return result
```

### Tribonacci

```python
# naive approach
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1: return n
        if n == 2: return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
```

## Exercises

- [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/description/)
- [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)
- [39. Combination Sum](https://leetcode.com/problems/combination-sum/description/)
-
