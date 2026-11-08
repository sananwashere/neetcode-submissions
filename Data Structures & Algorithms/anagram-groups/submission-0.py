class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}
        for anagram in strs:
            key = "".join(sorted(anagram))
            if key not in sorted_dict:
                sorted_dict[key] = []
            sorted_dict[key].append(anagram)
        
        return list(sorted_dict.values())