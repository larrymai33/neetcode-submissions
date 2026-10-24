class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+ 1)]

        counter = Counter(nums)
        

        for i,j in counter.items():
            bucket[j].append(i)
        
        ans = []
        count = k

        for i in range(len(bucket)-1, 0 ,-1):
            if bucket[i]:
                for j in range(len(bucket[i])):
                    if count <= 0:
                        break
                    else:
                        ans.append(bucket[i][j])
                        count -=1

        
        return ans


