"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by 
using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # identify unique chars in ransomNote
    uniq_chars = set(list(ransomNote))

    # find occurrences of each unique char
    # tally with the respective char count in the magazine
    for char in uniq_chars:
        r_count = ransomNote.count(char)
        m_count = magazine.count(char)
        if m_count >= r_count:
            continue
        else:
            return False
    return True