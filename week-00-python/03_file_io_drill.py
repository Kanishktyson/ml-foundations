"""Drill 3 — file I/O.

TASK: write a word-report tool:
  1. count_words(path) — total words in a text file.
  2. longest_word(text) — longest word, ties go to the first.
  3. write_report(path, text) — write a small summary file.
Run from the repo root (it reads its own sample file).
"""


# ── solutions ─────────────────────────────────────────────

def count_words(text: str) -> int:
    return len(text.split())


def longest_word(text: str) -> str:
    words = text.split()
    best = ""
    for w in words:
        if len(w) > len(best):
            best = w
    return best


def write_report(report_path: str, text: str) -> None:
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"words: {count_words(text)}\n")
        f.write(f"longest: {longest_word(text)}\n")


if __name__ == "__main__":
    sample_path = "sample.txt"
    sample_text = (
        "foundations first. small drills every day, "
        "no rushing, no pretending.\n"
    )
    with open(sample_path, "w", encoding="utf-8") as f:
        f.write(sample_text)

    with open(sample_path, "r", encoding="utf-8") as f:
        read_back = f.read()

    assert read_back == sample_text
    write_report("report.txt", read_back)
    print(open("report.txt").read())
