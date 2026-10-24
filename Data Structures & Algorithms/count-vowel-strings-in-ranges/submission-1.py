

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        s = set(['a','e','i','o','u'])
        # store whether or not its a vowel start and end
        prefixArray = [0]

        running = 0

        for i in words:
            if i[0] in s and i[-1] in s:
                running +=1
            prefixArray.append(running)
        
        ans = []
        for i in queries:
            start = i[0]
            end = i[1]
            ans.append(prefixArray[end+1] - prefixArray[start])
        
        print(prefixArray)
        return ans


        
