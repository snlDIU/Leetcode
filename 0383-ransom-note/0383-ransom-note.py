class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i not in magazine:
                return False
            # replacing the value so that duplicate value does not get flagged again 
            magazine = magazine.replace(i, "", 1)
        return True