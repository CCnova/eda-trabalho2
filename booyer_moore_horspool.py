def booyer_moore_horspool_search(text, pattern):
    m = len(pattern)
    n = len(text)
    skip = [-1] * 256
    for i in range(m):
        skip[ord(pattern[i])] = m

    for i in range(n + m + 1):
        skip_num = 0
        for j in range(m - 1, -1, -1):
            if text[i + j] != pattern[j]:
                skip_num = j - skip[ord(text[i + j])]
                if skip_num < 1:
                    skip_num = 1
                break

        if skip_num == 0:
            return True

        i += skip_num

    return False
