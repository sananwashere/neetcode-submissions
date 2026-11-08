class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        result = []
        for number in nums:
            if number not in nums_dict:
                nums_dict[number] = []
            nums_dict[number].append(number)

        number_array = sorted(nums_dict.values(), key=len , reverse=True)

        for i in range(k):
            result.append(number_array[i][0])

        return result