#!/usr/bin/env python3
"""Funniest sick-day excuse entry.

Writes a single sick-day excuse line -- under 200 characters -- to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: no randomness, no network, no input files.

Why this line: the draft ("I woke up with a fever of 39 and my cat
is sick too...") is exactly the worn excuse the judge brief warns
against -- fever plus a pet, no twist, no laugh. The final line turns
on a fresh idea instead: joking about calling in sick, and the body
taking the joke as a formal request. The twist ("professional
courtesy") lands near the end, with the deadpan tail "obviously" after
it so the laugh arrives before the last word, and the whole thing
reads like a real person typing a message to their boss -- half
believable, in the sense that everyone has felt a joke turn real.
"""

import os

LINE = "I joked about calling in sick yesterday and my body took it as a formal request, so now I'm ill out of professional courtesy, obviously."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
