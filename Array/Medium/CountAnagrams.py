from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # My sol
        anagrams = dict()
        for w in strs:
            sortedW = str(sorted(list(w)))
            if sortedW in anagrams:
                anagrams[sortedW].append(w)
            else:
                anagrams[sortedW] = [w]
        return list(anagrams.values())