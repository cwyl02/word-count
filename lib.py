from collections.abc import Iterable

def calculate(input_iter: Iterable) -> int:
    word_count = 0
    for line in input_iter:
        word_count += count_word(line)

    return word_count

def count_word(line: str) -> int:
    words = line.split()
    return len(words)
