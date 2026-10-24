

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[]* 1 for i in range(len(nums)+1)]

        counter = Counter(nums)


        for val,count in counter.items():
            bucket[count].append(val)
        
        
        ans = []
        count = k
        for i in range(len(bucket)-1, 0, -1):
            if bucket[i]:
                for j in bucket[i]:
                    if count >0:
                        ans.append(j)
                        count -= 1
                    else:
                        break

        
        return ans

