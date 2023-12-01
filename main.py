from naive_search import naive_search
from kmp import kmp_search
import random
import time
from typing import List

alphabets = [
  ["a", "b"], # sigma_2
  ["a", "b", "c", "d"], # sigma_4
  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"], # sigma_16
  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x" "y", "z", "A", "B", "C", "D", "E", "F",] # sigma_32
]

pattern_sizes = [2, 4, 6, 8, 10, 12, 14]

def generate_random_pattern(text: str, size: int) -> str:
    return text[len(text) - size:]

def generate_random_text(alphabet: List[str], size: int) -> str:
    return ''.join(random.choice(alphabet) for i in range(size))

def execute_analysis():
    for alphabet in alphabets:
        for size in pattern_sizes:
            print(f"-------- Alphabet size: {len(alphabet)} - Pattern Size: {size} --------")
            text = generate_random_text(alphabet, 1000)
            pattern = generate_random_pattern(text, size)

            start = time.time()
            pattern_found_naive = naive_search(text, pattern)
            end = time.time()
            print(f"Naive Pattern found {pattern_found_naive}: {end-start}")

            start = time.time()
            pattern_found_kmp = kmp_search(text, pattern)
            end = time.time()
            print(f"KMP Pattern found {pattern_found_kmp}: {end-start}")

# start = time.time()
# naive_search("Hello Worldasdjsadiojaodijajncxlcznlkmadslkamalkmlckzncxsiasmasmlkmclknvlkmafmkks", "Hi")
# end = time.time()
# print(end-start)

# start = time.time()
# kmp_search("Hello Worldasdjsadiojaodijajncxlcznlkmadslkamalkmlckzncxsiasmasmlkmclknvlkmafmkks", "Hi")
# end = time.time()
# print(end-start)

# print(generate_random_text(alphabets[3], 1000))
execute_analysis()