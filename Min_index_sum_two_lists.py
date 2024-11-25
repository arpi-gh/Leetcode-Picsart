class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        words = {}
        min_sum = len(list1) + len(list2)
        for i in range(len(list1)):
            words[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in words:
                index_sum = words[list2[i]] + i
                if index_sum < min_sum:
                    res = []
                    res.append(list2[i])
                    min_sum = index_sum
                elif index_sum == min_sum:
                    res.append(list2[i])
        return res