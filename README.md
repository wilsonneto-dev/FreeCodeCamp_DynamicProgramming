# FreeCodeCamp_DynamicProgramming++

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
