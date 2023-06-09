class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = ""
        for letter in letters :
            if letter > target and (letter < ans or ans  == "" ) :
            
                ans = letter
        return  letters[0] if  ans == "" else ans