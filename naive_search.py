def naive_search(text: str, pattern: str) -> bool:
    """
    Naive search algorithm O(n*m) where n is the length of text and m is the length of pattern
    :param text: text to search in
    :param pattern: pattern to search for
    :return: True if pattern is in text, False otherwise
    """
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return True
    return False