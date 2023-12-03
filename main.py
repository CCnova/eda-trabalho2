import random
import time
import matplotlib.pyplot as plt
from typing import List
from naive_search import naive_search
from rabin_karp import rabin_karp_search
from kmp import kmp_search, compute_lps_table
from booyer_moore import booyer_moore_search
from booyer_moore_horspool import booyer_moore_horspool_search

ALPHABETS = [
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

PATTERN_SIZES = [2, 4, 6, 8, 10, 12, 14]

NUMBER_OF_TESTS = 10


def generate_random_pattern(text: str, size: int) -> str:
    """
    Generate a random pattern with the given text and size
    gathering the last `size` chars of `text`.
    """
    return text[len(text) - size :]


def generate_random_text(alphabet: List[str], size: int) -> str:
    """Generate a random text with the given alphabet and size."""
    return "".join(random.choice(alphabet) for i in range(size))


def calculate_average(values: List[float]) -> float:
    """Calculate the average of the given values."""
    return sum(values) / len(values)


def execute_analysis():
    """Execute the analysis of the algorithms."""
    times_naive = []
    times_kmp = []
    times_rabin_karp = []
    times_booyer_moore = []
    times_booyer_moore_horspool = []
    num_comparisons_naive = []
    num_comparisons_kmp = []
    num_comparisons_rabin_karp = []
    num_comparisons_booyer_moore = []
    num_comparisons_booyer_moore_horspool = []
    effort_naive = []
    effort_kmp = []
    effort_rabin_karp = []
    effort_booyer_moore = []
    effort_booyer_moore_horspool = []
    pairs_alphabet_pattern = []
    for alphabet in ALPHABETS:
        for size in PATTERN_SIZES:
            print(
                f"-------- Alphabet size: {len(alphabet)} - Pattern Size: {size} --------"
            )

            text = generate_random_text(alphabet, 1000)
            pattern = generate_random_pattern(text, size)

            tests_times_naive = []
            tests_num_comparisons_naive = []
            tests_effort_naive = []
            for _ in range(NUMBER_OF_TESTS):
                pattern_found_naive = naive_search(text, pattern)
                tests_times_naive.append(pattern_found_naive["execution_time"])
                tests_num_comparisons_naive.append(pattern_found_naive["comparisons"])
                tests_effort_naive.append(pattern_found_naive["effort"])
            times_average_naive = calculate_average(tests_times_naive)
            num_comparisons_average_naive = calculate_average(
                tests_num_comparisons_naive
            )
            effort_average_naive = calculate_average(tests_effort_naive)
            times_naive.append(times_average_naive)
            num_comparisons_naive.append(num_comparisons_average_naive)
            effort_naive.append(effort_average_naive)
            print(
                f"Naive ------- Execution time: {times_average_naive}, Number of comparisons: {num_comparisons_average_naive}, Effort: {effort_average_naive}"
            )

            tests_times_kmp = []
            tests_num_comparisons_kmp = []
            tests_effort_kmp = []
            for _ in range(NUMBER_OF_TESTS):
                pattern_found_kmp = kmp_search(text, pattern)
                tests_times_kmp.append(pattern_found_kmp["execution_time"])
                tests_num_comparisons_kmp.append(pattern_found_kmp["comparisons"])
                tests_effort_kmp.append(pattern_found_kmp["effort"])
            times_average_kmp = calculate_average(tests_times_kmp)
            num_comparisons_average_kmp = calculate_average(tests_num_comparisons_kmp)
            effort_average_kmp = calculate_average(tests_effort_kmp)
            times_kmp.append(times_average_kmp)
            num_comparisons_kmp.append(num_comparisons_average_kmp)
            effort_kmp.append(effort_average_kmp)
            print(
                f"KMP ------- Execution time: {times_average_kmp}, Number of comparisons: {num_comparisons_average_kmp}, Effort: {effort_average_kmp}"
            )

            tests_times_rabin_karp = []
            tests_num_comparisons_rabin_karp = []
            tests_effort_rabin_karp = []
            for _ in range(NUMBER_OF_TESTS):
                pattern_found_rabin_karp = rabin_karp_search(
                    text, pattern, len(alphabet)
                )
                tests_times_rabin_karp.append(
                    pattern_found_rabin_karp["execution_time"]
                )
                tests_num_comparisons_rabin_karp.append(
                    pattern_found_rabin_karp["comparisons"]
                )
                tests_effort_rabin_karp.append(pattern_found_rabin_karp["effort"])
            times_average_rabin_karp = calculate_average(tests_times_rabin_karp)
            num_comparisons_average_rabin_karp = calculate_average(
                tests_num_comparisons_rabin_karp
            )
            effort_average_rabin_karp = calculate_average(tests_effort_rabin_karp)
            times_rabin_karp.append(times_average_rabin_karp)
            num_comparisons_rabin_karp.append(num_comparisons_average_rabin_karp)
            effort_rabin_karp.append(effort_average_rabin_karp)
            print(
                f"Rabin Karp ------- Execution time: {times_average_rabin_karp}, Number of comparisons {num_comparisons_average_rabin_karp}, Effort: {effort_average_rabin_karp}"
            )

            tests_times_booyer_moore = []
            tests_num_comparisons_booyer_moore = []
            tests_effort_booyer_moore = []
            for _ in range(NUMBER_OF_TESTS):
                pattern_found_booyer_moore = booyer_moore_search(text, pattern)
                tests_times_booyer_moore.append(
                    pattern_found_booyer_moore["execution_time"]
                )
                tests_num_comparisons_booyer_moore.append(
                    pattern_found_booyer_moore["comparisons"]
                )
                tests_effort_booyer_moore.append(pattern_found_booyer_moore["effort"])
            times_average_booyer_moore = calculate_average(tests_times_booyer_moore)
            num_comparisons_average_booyer_moore = calculate_average(
                tests_num_comparisons_booyer_moore
            )
            effort_average_booyer_moore = calculate_average(tests_effort_booyer_moore)
            times_booyer_moore.append(times_average_booyer_moore)
            num_comparisons_booyer_moore.append(num_comparisons_average_booyer_moore)
            effort_booyer_moore.append(effort_average_booyer_moore)
            print(
                f"Booyer Moore ------- Execution time: {times_average_booyer_moore}, Number of comparisons: {num_comparisons_average_booyer_moore}, Effort: {effort_average_booyer_moore}"
            )

            tests_times_booyer_moore_horspool = []
            tests_num_comparisons_booyer_moore_horspool = []
            tests_effort_booyer_moore_horspool = []
            for _ in range(NUMBER_OF_TESTS):
                pattern_found_booyer_moore_horspool = booyer_moore_horspool_search(
                    text, pattern
                )
                tests_times_booyer_moore_horspool.append(
                    pattern_found_booyer_moore_horspool["execution_time"]
                )
                tests_num_comparisons_booyer_moore_horspool.append(
                    pattern_found_booyer_moore_horspool["comparisons"]
                )
                tests_effort_booyer_moore_horspool.append(
                    pattern_found_booyer_moore_horspool["effort"]
                )
            times_average_booyer_moore_horspool = calculate_average(
                tests_times_booyer_moore_horspool
            )
            num_comparisons_average_booyer_moore_horspool = calculate_average(
                tests_num_comparisons_booyer_moore_horspool
            )
            effort_average_booyer_moore_horspool = calculate_average(
                tests_effort_booyer_moore_horspool
            )
            times_booyer_moore_horspool.append(times_average_booyer_moore_horspool)
            num_comparisons_booyer_moore_horspool.append(
                num_comparisons_average_booyer_moore_horspool
            )
            effort_booyer_moore_horspool.append(effort_average_booyer_moore_horspool)
            print(
                f"Booyer Moore Horspool ------- Execution time: {times_average_booyer_moore_horspool}, Number of comparisons: {num_comparisons_average_booyer_moore_horspool}, Effort: {effort_average_booyer_moore_horspool}"
            )

            pairs_alphabet_pattern.append(f"({len(alphabet)}, {size})")

    # --------------- PLOT time execution ---------------
    plt.plot(times_naive, label="Naive")
    plt.plot(times_kmp, label="KMP")
    plt.plot(times_rabin_karp, label="Rabin-Karp")
    plt.plot(times_booyer_moore, label="Booyer-Moore")
    plt.plot(times_booyer_moore_horspool, label="Booyer-Moore-Horspool")
    plt.xlabel("Pair (Alphabet Size, Pattern Size)")
    plt.ylabel("Time (s)")
    plt.xticks(range(len(times_kmp)), pairs_alphabet_pattern)
    plt.legend(loc="best")
    plt.show()

    # ---------------- PLOT number of comparisons ---------------
    plt.plot(num_comparisons_naive, label="Naive")
    plt.plot(num_comparisons_kmp, label="KMP")
    plt.plot(num_comparisons_rabin_karp, label="Rabin-Karp")
    plt.plot(num_comparisons_booyer_moore, label="Booyer-Moore")
    plt.plot(num_comparisons_booyer_moore_horspool, label="Booyer-Moore-Horspool")
    plt.xlabel("Pair (Alphabet Size, Pattern Size)")
    plt.ylabel("Number of comparisons")
    plt.xticks(range(len(num_comparisons_kmp)), pairs_alphabet_pattern)
    plt.legend(loc="best")
    plt.show()

    # ---------------- PLOT effort ---------------
    plt.plot(effort_naive, label="Naive")
    plt.plot(effort_kmp, label="KMP")
    plt.plot(effort_rabin_karp, label="Rabin-Karp")
    plt.plot(effort_booyer_moore, label="Booyer-Moore")
    plt.plot(effort_booyer_moore_horspool, label="Booyer-Moore-Horspool")
    plt.xlabel("Pair (Alphabet Size, Pattern Size)")
    plt.ylabel("Effort")
    plt.xticks(range(len(effort_kmp)), pairs_alphabet_pattern)
    plt.legend(loc="best")
    plt.show()


execute_analysis()
