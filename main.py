import random
import time
import matplotlib.pyplot as plt
from typing import List
from naive_search import naive_search
from kmp import kmp_search
from rabin_karp import rabin_karp_search

alphabets = [
    ["a", "b"],  # sigma_2
    ["a", "b", "c", "d"],  # sigma_4
    [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
    ],  # sigma_16
    [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ],  # sigma_32
]

pattern_sizes = [2, 4, 6, 8, 10, 12, 14]


def generate_random_pattern(text: str, size: int) -> str:
    """
    Generate a random pattern with the given text and size
    gathering the last `size` chars of `text`.
    """
    return text[len(text) - size :]


def generate_random_text(alphabet: List[str], size: int) -> str:
    """Generate a random text with the given alphabet and size."""
    return "".join(random.choice(alphabet) for i in range(size))


def execute_analysis():
    """Execute the analysis of the algorithms."""
    times_naive = []
    times_kmp = []
    times_rabin_karp = []
    pairs_alphabet_pattern = []
    for alphabet in alphabets:
        for size in pattern_sizes:
            print(
                f"-------- Alphabet size: {len(alphabet)} - Pattern Size: {size} --------"
            )
            text = generate_random_text(alphabet, 1000)
            pattern = generate_random_pattern(text, size)

            start = time.time()
            pattern_found_naive = naive_search(text, pattern)
            end = time.time()
            time_naive = end - start
            times_naive.append(time_naive)
            print(f"Naive Pattern found {pattern_found_naive}: {time_naive}")

            start = time.time()
            pattern_found_kmp = kmp_search(text, pattern)
            end = time.time()
            time_kmp = end - start
            times_kmp.append(time_kmp)
            print(f"KMP Pattern found {pattern_found_kmp}: {time_kmp}")

            start = time.time()
            pattern_found_rabin_karp = rabin_karp_search(text, pattern)
            end = time.time()
            time_rabin_karp = end - start
            times_rabin_karp.append(time_rabin_karp)
            print(
                f"Rabin-Karp Pattern found {pattern_found_rabin_karp}: {time_rabin_karp}"
            )

            pairs_alphabet_pattern.append(f"({len(alphabet)}, {size})")

    plt.plot(times_naive, label="Naive")
    plt.plot(times_kmp, label="KMP")
    plt.plot(times_rabin_karp, label="Rabin-Karp")
    plt.xlabel("Pair (Alphabet Size, Pattern Size)")
    plt.ylabel("Time (s)")
    plt.xticks(range(len(times_naive)), pairs_alphabet_pattern)
    plt.legend(loc="best")
    plt.show()


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
