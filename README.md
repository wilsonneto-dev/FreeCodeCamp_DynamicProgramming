# FreeCodeCamp_DynamicProgramming

`(plus: leetcode explorer card)`

### Just practicing DP

## materials

- Video I link: https://www.youtube.com/watch?v=oFkDldu3C_4
- Video II link: https://www.youtube.com/watch?v=oBt53YbR9Kk&t=6s
- Leetcode Explorer Card link: https://leetcode.com/explore/learn/card/dynamic-programming/

### Introduction

DP is used when you see a problem that can be **broken** down into **smaller subproblems**, and the subproblems are **overlapping**.

---

## Exercises

FreeCodeCamp Video I:

- [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/description/)
- [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)
- [39. Combination Sum](https://leetcode.com/problems/combination-sum/description/)
- [322. Coin Change (Min Change)](https://leetcode.com/problems/coin-change/description/)
- [62. Unique Paths](https://leetcode.com/problems/unique-paths/)
- [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)'
- [Max Sum Without Adjacent](https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1)
- [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/description/)
- [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/description/)

---

## Solutions

---

### Fibonacci

```python
# naive approach
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)
```

```python
#DP approach / memoisation / top-down
class Solution:
    def fib(self, n: int, cache: {} = None) -> int:
        if cache == None: cache = { 0: 0, 1: 1 }

        if n in cache: return cache[n]

        result = self.fib(n-1, cache) + self.fib(n-2, cache)
        cache[n] = result

        return result
```

---

### Tribonacci

```python
# naive approach
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1: return n
        if n == 2: return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
```

```python
# DP approach / memoisation / top-down
class Solution:
    def tribonacci(self, n: int, cache: {} = None) -> int:
        if cache == None:
            cache = { 0: 0, 1: 1, 2: 1 }

        if n in cache:
            return cache[n]

        result = self.tribonacci(n-1, cache) + self.tribonacci(n-2, cache) + self.tribonacci(n-3, cache)
        cache[n] = result
        return result
```

---

### Min Change / Coin Change

```python
# DP with memoization / top down
class Solution:
    def coinChange(self, coins: List[int], amount: int, cache: {} = None) -> int:
        if amount < 0: return -1
        if amount == 0: return 0

        if cache == None: cache = {}
        if amount in cache:
            return cache[amount]

        _min = -1
        for coin in coins:
            change = self.coinChange(coins, amount - coin, cache)
            if change != -1:
                if _min == -1: _min = change +1
                else: _min = min(_min, change + 1)

        cache[amount] = _min
        return _min
```

---

### Unique Paths

```python
# DP with memoization / top down
class Solution:
    def uniquePaths(self, m: int, n: int, cache: {} = None) -> int:
        if m == 1 or n == 1: return 1
        if cache == None: cache = {}

        if (m, n) in cache: return cache[(m, n)]

        _count = self.uniquePaths(m -1, n, cache) + \
            self.uniquePaths(m, n -1, cache)

        cache[(m, n)] = _count
        return _count
```

---

### Minimum Path Sum

```python
# DP with memoization / top down
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0]
        def minPathSumInner(x: int, y: int, grid: List[List[int]], cache: {}):
            if x >= len(grid) or y >= len(grid[0]): return sys.maxsize

            if x == len(grid) -1 and y == len(grid[0]) -1: return grid[-1][-1]
            if (x, y) in cache: return cache[(x, y)]

            _min = (
                min(minPathSumInner(x + 1, y, grid, cache), minPathSumInner(x, y + 1, grid, cache))
                + grid[x][y]
            )
            cache[(x, y)] = _min
            return _min

        cache = {}
        minPathSumInner(0, 0, grid, cache)
        return cache[(0,0)]
```

---

### Max Sum Without Adjacent

```python
# DP with memoization / top down
class Solution:

	def findMaxSum(self, arr, n, cache: {} = None, idx = 0):
	    if cache == None:
	        cache = {}

	    if idx >= len(arr):
	        return 0

	    if idx in cache:
	        return cache[idx]

	    _max = max(
	        arr[idx] + self.findMaxSum(arr, n, cache, idx + 2),
	        self.findMaxSum(arr, n, cache, idx + 1),
        )

        cache[idx] = _max
        return _max
```
---

279. Perfect Squares

```python
# DP with memoization / top down
class Solution:
    def numSquares(self, n: int) -> int:
        def numSquares(_n, cache):
            if _n == 1: return 1
            if _n == 0: return 0

            if _n in cache: 
                return cache[_n]                

            _next = 1
            _min = sys.maxsize
            while (_next * _next) <= _n:
                _min = min(_min, numSquares(_n - (_next * _next), cache))
                _next += 1
            
            cache[_n] = _min + 1
            return cache[_n]
                

        return numSquares(n, {})


```

---

### 518. Coin Change II

```python
# DP with memoization / top down
class Solution:
    def change(self, amount: int, coins: List[int], cache: {} = None, idx: int = 0) -> int:
        if cache == None: 
            cache = {}
        
        if amount == 0: 
            return 1
        
        if idx >= len(coins) or amount < 0: 
            return 0
        
        if (amount, idx) in cache:
            return cache[(amount, idx)]

        _combinations = 0
        i = 0
        while coins[idx] * i <= amount:
            _combinations += self.change(amount - (coins[idx] * i), coins, cache, idx+1)
            i += 1
        
        cache[(amount, idx)] = _combinations
        return _combinations

```

