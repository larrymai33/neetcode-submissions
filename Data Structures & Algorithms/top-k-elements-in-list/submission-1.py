"""

k most frequent = counter and then sort by most common
or use a minheap
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]

        for i,j in count.items():
            buckets[j].append(i)


        ans = []

        for i in range(len(buckets)-1, 0, -1):
            if buckets[i]:
                for j in range(len(buckets[i])):
                    if k == 0:
                        break
                    ans.append(buckets[i][j])
                    k-=1

        return ans



            







