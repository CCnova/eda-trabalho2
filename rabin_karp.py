import time

PRIME = 101


def rabin_karp_search(txt, pat, d):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1

    for i in range(M - 1):
        h = (h * d) % PRIME

    for i in range(M):
        p = (d * p + ord(pat[i])) % PRIME
        t = (d * t + ord(txt[i])) % PRIME

    start = time.time()
    number_of_comparisons = 0
    for i in range(N - M + 1):
        if p == t:
            for j in range(M):
                if txt[i + j] != pat[j]:
                    number_of_comparisons += 1
                    break
                else:
                    j += 1

            if j == M:
                return {
                    "found": True,
                    "execution_time": time.time() - start,
                    "comparisons": number_of_comparisons,
                }

        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % PRIME

            if t < 0:
                t = t + PRIME
    return {
        "found": False,
        "execution_time": time.time() - start,
        "comparisons": number_of_comparisons,
    }
