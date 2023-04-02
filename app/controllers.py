import re

def reverse_integer(number: int) -> int:
    is_negative = number < 0
    reverse_abs = int(str(abs(number))[::-1])

    return -reverse_abs if is_negative else reverse_abs

def average_words_length(phrase: str) -> float:
    words = re.findall(r'\w+', phrase)
    print(words)
    total_letters = sum(len(word) for word in words)
    return total_letters / len(words) if words else 0

def matched_and_mismatched_words(phrase1: str, phrase2: str) -> tuple[list[str], list[str]]:
    set1, set2 = get_word_sets(phrase1, phrase2)
    mismatched_words = get_symmetric_difference(set1, set2)
    matched_words = get_intersection(set1, set2)
    return mismatched_words, matched_words

def get_word_sets(phrase1: str, phrase2: str) -> tuple[set[str], set[str]]:
    set1 = set(phrase1.split())
    set2 = set(phrase2.split())
    return set1, set2

def get_symmetric_difference(set1: set[str], set2: set[str]) -> list[str]:
    return sorted(list(set1.symmetric_difference(set2)))

def get_intersection(set1: set[str], set2: set[str]) -> list[str]:
    return sorted(list(set1.intersection(set2)))

