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


start = time.time()
naive_search("Hello Worldasdjsadiojaodijajncxlcznlkmadslkamalkmlckzncxsiasmasmlkmclknvlkmafmkks", "Hi")
end = time.time()
print(end-start)

start = time.time()
kmp_search("Hello Worldasdjsadiojaodijajncxlcznlkmadslkamalkmlckzncxsiasmasmlkmclknvlkmafmkks", "Hi")
end = time.time()
print(end-start)

print(generate_random_text(alphabets[3], 1000))