class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Count = 0
        d = {}
        for number in nums:
            if number not in d:
                d[number] = Count
            else:
                d[number] += 1
        for v in d.values():
            if v > 0:
                return True
        return False
        




        