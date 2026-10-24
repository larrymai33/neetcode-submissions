

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        ans = 0

        left = 0
        right = len(people) -1

        while left <= right:
            if left == right:
                ans+=1
                left+=1
                right-=1
            elif people[left] + people[right] <= limit:
                ans +=1
                left +=1
                right -=1
            elif people[right] <= limit:
                ans+=1
                right-=1
        
        return ans