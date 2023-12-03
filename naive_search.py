import time


def naive_search(text: str, pattern: str) -> bool:
    """
    Naive search algorithm O(n*m) where n is the length of text and m is the length of pattern
    :param text: text to search in
    :param pattern: pattern to search for
    :return: True if pattern is in text, False otherwise
    """
    start = time.time()
    n = len(text)
    m = len(pattern)
    number_of_comparisons = 0
    for i in range(n - m + 1):
        j = 0
        if text[i + j] != pattern[j]:
            number_of_comparisons += 1
            continue

        while j < m and text[i + j] == pattern[j]:
            number_of_comparisons += 1
            j += 1
        if j == m:
            return {
                "found": True,
                "execution_time": time.time() - start,
                "comparisons": number_of_comparisons,
            }
    return {
        "found": False,
        "execution_time": time.time() - start,
        "comparisons": number_of_comparisons,
    }
