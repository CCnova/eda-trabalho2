from typing import List

def compute_lps_table(pattern: str) -> List[int]:
    lps_table = [0] * len(pattern)
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            lps_table[i] = j + 1
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps_table[j - 1]
            else:
                i += 1

    return lps_table

def kmp_search(text: str, pattern: str) -> bool:
    lps_table = compute_lps_table(pattern)
    i = 0
    j = 0
    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps_table[j - 1]
            else:
                i += 1

    if j == len(pattern):
        return True

    return False