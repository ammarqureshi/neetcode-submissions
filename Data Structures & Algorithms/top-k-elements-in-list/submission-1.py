class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countMap = {}
        freq = [[] for i in range(len(nums)+1)]

        # count frequency of each number
        for n in nums: 
            countMap[n] = 1 + countMap.get(n,0)
        # invert key and value pair
        for num, count in countMap.items(): 
            freq[count].append(num)

        # pick top k elements, going from right to left
        res = []
        for i in range(len(freq) -1, 0, -1): 
            #iterate over sublist
            for n in freq[i]: 
                res.append(n)
                if len(res) == k: 
                    return res

    

        