class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters = dict()
                
        for letter in magazine:
            if letter in magazine_letters.keys():
                magazine_letters[letter] += 1
            else:
                magazine_letters[letter] = 1
                
        for letter in ransomNote:
            if letter in magazine_letters.keys():
                if magazine_letters[letter] == 0:
                    return False
                magazine_letters[letter] -= 1
            else:
                return False
                   
        return True