from typing import List
import time


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


def kmp_search(text: str, pattern: str):
    lps_table = compute_lps_table(pattern)
    start = time.time()
    number_of_comparisons = 0
    effort = 0
    i = 0
    j = 0
    while i < len(text) and j < len(pattern):
        effort += 1
        if text[i] == pattern[j]:
            number_of_comparisons += 1
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps_table[j - 1]
            else:
                i += 1

    if j == len(pattern):
        return {
            "found": True,
            "execution_time": time.time() - start,
            "comparisons": number_of_comparisons,
            "effort": effort / len(text),
        }

    return {
        "found": False,
        "execution_time": time.time() - start,
        "comparisons": number_of_comparisons,
        "effort": effort / len(text),
    }
