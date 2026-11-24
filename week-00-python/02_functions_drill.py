"""Drill 2 — functions.

TASK: write these before reading:
  1. is_prime(n) — handle n < 2, check divisors up to sqrt(n).
  2. word_freq(text) — dict of word → count, case-insensitive.
  3. apply_twice(fn, x) — higher-order functions hurt now, they won't later.
"""


# ── solutions ─────────────────────────────────────────────

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def word_freq(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def apply_twice(fn, x):
    return fn(fn(x))


if __name__ == "__main__":
    assert [n for n in range(20) if is_prime(n)] == [2, 3, 5, 7, 11, 13, 17, 19]
    freq = word_freq("the cat the dog the bird")
    assert freq == {"the": 3, "cat": 1, "dog": 1, "bird": 1}
    assert apply_twice(lambda v: v * 2, 5) == 20
    print("all function drills pass ✔")
