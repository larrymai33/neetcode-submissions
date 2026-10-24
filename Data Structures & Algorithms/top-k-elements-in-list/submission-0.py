"""

k most frequent = counter and then sort by most common
or use a minheap
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        counter = Counter(nums)

        ans2 = counter.most_common(k)

        for i in ans2:
            ans.append(i[0])
        return ans


