class Solution:
    def isValid(self, s: str) -> bool:
        a = {')':'(','}':'{', ']':'['}
        b = []
        for i in s:
            if i in a:
                c = b.pop() if b else '#'
                if a[i] != c:
                    return False
            else:
                b += i
        return not b
     