import time

NO_OF_CHARS = 256


def bad_char_heuristic(string, size):
    """
    The preprocessing function for
    Boyer Moore's bad character heuristic
    """

    badChar = [-1] * NO_OF_CHARS

    for i in range(size):
        badChar[ord(string[i])] = i

    return badChar


def booyer_moore_search(txt, pat):
    """
    A pattern searching function that uses Bad Character
    Heuristic of Boyer Moore Algorithm
    """
    m = len(pat)
    n = len(txt)

    bad_char = bad_char_heuristic(pat, m)

    start = time.time()
    number_of_comparisons = 0
    effort = 0
    s = 0
    while s <= n - m:
        effort += 1
        j = m - 1

        while j >= 0 and pat[j] == txt[s + j]:
            effort += 1
            number_of_comparisons += 1
            j -= 1

        if j < 0:
            s += m - bad_char[ord(txt[s + m])] if s + m < n else 1
            return {
                "found": True,
                "execution_time": time.time() - start,
                "comparisons": number_of_comparisons,
                "effort": effort / len(txt),
            }
        else:
            s += max(1, j - bad_char[ord(txt[s + j])])
    return {
        "found": False,
        "execution_time": time.time() - start,
        "comparisons": number_of_comparisons,
        "effort": effort / len(txt),
    }
