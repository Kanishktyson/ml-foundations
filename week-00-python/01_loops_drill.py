"""Drill 1 — loops.

TASK: before reading the solutions, write these yourself:
  1. fizzbuzz(15) — classic. 3→Fizz, 5→Buzz, both→FizzBuzz.
  2. running_sum(nums) — accumulate a total with a loop (no sum()).
  3. star_triangle(n) — print n rows of increasing stars.
Then compare. The solution below the line is how I solved it.
"""


# ── solutions ─────────────────────────────────────────────

def fizzbuzz(n: int) -> list[str]:
    out = []
    for i in range(1, n + 1):
        label = ""
        if i % 3 == 0:
            label += "Fizz"
        if i % 5 == 0:
            label += "Buzz"
        out.append(label or str(i))
    return out


def running_sum(nums: list[int]) -> int:
    total = 0
    for n in nums:
        total += n
    return total


def star_triangle(n: int) -> str:
    rows = []
    for i in range(1, n + 1):
        rows.append("*" * i)
    return "\n".join(rows)


if __name__ == "__main__":
    print(fizzbuzz(15))
    print(running_sum([3, 7, 2, 8]))   # expect 20
    print(star_triangle(4))
