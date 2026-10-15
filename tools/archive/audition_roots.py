#!/usr/bin/env python3
"""Step 3 -- audition candidate BARE ROOTS (non-semantic, beauty-first).

Reads the packed base list produced by
    python3 tools/enumerate_roots.py --pack --config current --emit /tmp/lomissifil-roots-current.txt
samples N bases, and writes the FOUR area-rule forms of each, per R1 (author's
ruling 2026-10-14):  base+f | base+w | base+h | base
(/v/ is SPELLED `w`; the letter `v` is the vibrato mark.)  The author listens and
picks what sounds beautiful; the picks become the first coined roots. Meanings are
assigned later -- nothing here is a word yet.

Citation forms carry **no stress mark**: P4 says the dictionary form is unstressed
(stress is a performance choice), so these are plain lowercase.

Output: /tmp/lomissifil-audition/roots-NN.wav + a printed index.
"""

import argparse
import os
import random
import subprocess

OUT = "/tmp/lomissifil-audition"
ESPEAK = "espeak-ng"


def say(fname, text):
    path = os.path.join(OUT, fname)
    subprocess.run([ESPEAK, "-v", "fi", "-s", "130", "-w", path, text], check=True)
    return path


def main():
    global OUT
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="data/generated/roots-bases-current.txt",
                    help="packed base list, one base per line ('#' lines are skipped)")
    ap.add_argument("--bases", type=int, default=48, help="how many bases to audition")
    ap.add_argument("--per-file", type=int, default=8, help="bases per WAV")
    ap.add_argument("--seed", type=int, default=20261014)
    ap.add_argument("--out", default=OUT, help="directory for the WAVs (default: %s)" % OUT)
    a = ap.parse_args()

    OUT = a.out
    os.makedirs(OUT, exist_ok=True)
    with open(a.src, encoding="utf-8") as fh:
        all_bases = [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]
    bases = random.Random(a.seed).sample(all_bases, min(a.bases, len(all_bases)))
    print("auditioning %d bases from %d (%s) -> %s"
          % (len(bases), len(all_bases), a.src, OUT))

    idx = 0
    for fi in range(0, len(bases), a.per_file):
        chunk = bases[fi:fi + a.per_file]
        words, lines = [], []
        for b in chunk:
            tagged = []
            for form in (b + "f", b + "w", b + "h", b):
                idx += 1
                words.append(form)
                tagged.append("%3d %-10s" % (idx, form))
            lines.append("  %-10s %s" % (b, " | ".join(tagged)))
        fn = "roots-%02d.wav" % (fi // a.per_file + 1)
        say(fn, " , ".join(words))
        print("  " + fn)
        for ln in lines:
            print(ln)

    print()
    print("  each group of 4 = one base: +f | +w(/v/) | +h | bare (no final)")
    print("  exactly TWO of the four may be coined (one from {f,w}, one from {h,bare}).")
    print("  pick by number; ~4-6 favourites per file is plenty to start.")


if __name__ == "__main__":
    main()
