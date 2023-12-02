import random
import time
import matplotlib.pyplot as plt
from typing import List
from naive_search import naive_search
from rabin_karp import rabin_karp_search
from kmp import kmp_search, compute_lps_table
from booyer_moore import booyer_moore_search
from booyer_moore_horspool import booyer_moore_horspool_search

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

pattern_sizes = [2, 4, 6, 8, 10, 12, 14, 350]


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
    # times_naive = []
    times_kmp = []
    times_rabin_karp = []
    times_booyer_moore = []
    times_booyer_moore_horspool = []
    num_comparisons_kmp = []
    num_comparisons_rabin_karp = []
    num_comparisons_booyer_moore = []
    num_comparisons_booyer_moore_horspool = []
    pairs_alphabet_pattern = []
    for alphabet in alphabets:
        for size in pattern_sizes:
            print(
                f"-------- Alphabet size: {len(alphabet)} - Pattern Size: {size} --------"
            )
            text = generate_random_text(alphabet, 1000)
            pattern = generate_random_pattern(text, size)

            # pattern_found_naive = naive_search(text, pattern)
            # times_naive.append(pattern_found_naive["execution_time"])
            # print(
            #     f"Naive Pattern found {pattern_found_naive['found']}: {pattern_found_naive['execution_time']}"
            # )

            pattern_found_kmp = kmp_search(text, pattern)
            times_kmp.append(pattern_found_kmp["execution_time"])
            num_comparisons_kmp.append(pattern_found_kmp["comparisons"])
            print(
                f"KMP Pattern found {pattern_found_kmp['found']}: {pattern_found_kmp['execution_time']}"
            )

            pattern_found_rabin_karp = rabin_karp_search(text, pattern, len(alphabet))
            times_rabin_karp.append(pattern_found_rabin_karp["execution_time"])
            num_comparisons_rabin_karp.append(pattern_found_rabin_karp["comparisons"])
            print(
                f"Rabin-Karp Pattern found {pattern_found_rabin_karp['found']}: {pattern_found_rabin_karp['execution_time']}"
            )

            pattern_found_booyer_moore = booyer_moore_search(text, pattern)
            times_booyer_moore.append(pattern_found_booyer_moore["execution_time"])
            num_comparisons_booyer_moore.append(
                pattern_found_booyer_moore["comparisons"]
            )
            print(
                f"Booyer-Moore Pattern found {pattern_found_booyer_moore['found']}: {pattern_found_booyer_moore['execution_time']}"
            )

            pattern_found_booyer_moore_horspool = booyer_moore_horspool_search(
                text, pattern
            )
            times_booyer_moore_horspool.append(
                pattern_found_booyer_moore_horspool["execution_time"]
            )
            num_comparisons_booyer_moore_horspool.append(
                pattern_found_booyer_moore_horspool["comparisons"]
            )
            print(
                f"Booyer-Moore-Horspool Pattern found {pattern_found_booyer_moore_horspool['found']}: {pattern_found_booyer_moore_horspool['execution_time']}"
            )

            pairs_alphabet_pattern.append(f"({len(alphabet)}, {size})")

    # plt.plot(times_naive, label="Naive")
    # --------------- PLOT time execution ---------------
    # plt.plot(times_kmp, label="KMP")
    # plt.plot(times_rabin_karp, label="Rabin-Karp")
    # plt.plot(times_booyer_moore, label="Booyer-Moore")
    # plt.plot(times_booyer_moore_horspool, label="Booyer-Moore-Horspool")
    # plt.xlabel("Pair (Alphabet Size, Pattern Size)")
    # plt.ylabel("Time (s)")
    # plt.xticks(range(len(times_kmp)), pairs_alphabet_pattern)
    # plt.legend(loc="best")
    # plt.show()

    # ---------------- PLOT number of comparisons ---------------
    plt.plot(num_comparisons_kmp, label="KMP")
    plt.plot(num_comparisons_rabin_karp, label="Rabin-Karp")
    plt.plot(num_comparisons_booyer_moore, label="Booyer-Moore")
    plt.plot(num_comparisons_booyer_moore_horspool, label="Booyer-Moore-Horspool")
    plt.xlabel("Pair (Alphabet Size, Pattern Size)")
    plt.ylabel("Number of comparisons")
    plt.xticks(range(len(num_comparisons_kmp)), pairs_alphabet_pattern)
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
