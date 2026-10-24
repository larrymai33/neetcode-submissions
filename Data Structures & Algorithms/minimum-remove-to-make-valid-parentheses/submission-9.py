class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        stack to keep track

        map of open and closing parenthesis 

        traverse through string
        - if open we add to int 
        - if close
        - check counter if greater than 0 decrement and leave alone
        - else if we see close and theres no open, just remove it

        """

        indiciesStack = deque()

        counter = 0

        ans = ""

        for i in range(len(s)):
            if s[i] == "(":
                counter += 1
                indiciesStack.append(i)
            elif s[i] == ")" and counter > 0:
                counter -=1 
                indiciesStack.pop()       
            elif s[i] == ")":
                indiciesStack.append(i)


        for i in range(len(s)):
            if indiciesStack and i == indiciesStack[0]:
                indiciesStack.popleft()
            else:
                ans += s[i]

        return ans

            
        

        
            


