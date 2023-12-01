prime = 101
def rabin_karp_search(text: str, pattern: str) -> bool:
    m = len(pattern)
    n = len(text)
    pattern_hash = create_hash(pattern, m - 1)
    text_hash = create_hash(text, m - 1)

    for i in range(1, n - m + 2):
        if pattern_hash == text_hash:
            if check_equal(text[i-1:i+m-1], pattern[0:]) is True:
                return True;
        if i < n - m + 1:
            text_hash = recalculate_hash(text, i-1, i+m-1, text_hash, m)
    return False;

def check_equal(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False;
    i = 0
    j = 0
    for i, j in zip(str1, str2):
        if i != j:
            return False;
    return True

def create_hash(input: str, end: int) -> int:
    hash = 0
    for i in range(end + 1):
        hash = hash + ord(input[i])*pow(prime, i)
    return hash

def recalculate_hash(input: str, old_index: int, new_index: int, old_hash: int, pattern_len: int) -> int:
    new_hash = old_hash - ord(input[old_index])
    new_hash = new_hash/prime
    new_hash += ord(input[new_index])*pow(prime, pattern_len - 1)
    return new_hash;