# NOTES — Week 0

**Status:** scaffolded 24 Nov 2026, reworking by hand through the week.
Some of this drill set was AI-assisted as a starting point — the rule is:
I type every solution myself against the task first, then compare.

## What broke / what I learned

- `fizzbuzz`: first version checked `i % 3` and `i % 5` in separate `elif`s —
  15 never printed "FizzBuzz". Order of the checks matters.
- `running_sum`: reached for `sum()` out of habit. The point of the drill is
  the accumulator pattern — that's what pandas groupby-apply will feel like.
- `is_prime`: the `while d * d <= n` bound is the difference between a
  prime check that scales and one that doesn't.
- file I/O: forgot `encoding="utf-8"` on Windows once. Never again.

## Carrying into Week 1

- No `elif` chains when two independent conditions can both be true
- Accumulator pattern until it's boring
- Always open files with an explicit encoding
