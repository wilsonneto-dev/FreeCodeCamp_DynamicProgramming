# Given a target number and a group of numbers, return true 
# if it's possible to sum a combination of numbers from the group to get the target

class Solution:
  def isSumPossible(self, target: int, nums: list[int], cache: {} = None) -> bool:
    if target < 0: return False
    if cache == None: cache = { 0: True }
    if target in cache: return cache[target]

    for num in nums:
        isPossible = self.isSumPossible(target - num, nums, cache)
        cache[target - num] = isPossible
        print(cache)
        if isPossible: 
            return True

    return False
  
def test_isSumPossible():
    sol = Solution()

    test_cases = [
        {"target": 15, "nums": [4, 6, 10], "expected": False, "name": "15 from 4,6,10"},
        {"target": 15, "nums": [10, 1], "expected": True, "name": "15 from 4,6,10,1"}
    ]

    for test in test_cases:
        result = sol.isSumPossible(test["target"], test["nums"])
        assert result == test["expected"], f"Test '{test['name']}' failed: expected {test['expected']} but got {result}"

test_isSumPossible()