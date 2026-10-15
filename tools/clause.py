#!/usr/bin/env python3
"""Clause checker: a clause -> its cases, its chords, and the advisory class warnings.

This is the tool `03-open-questions.md` section 0 item 31 asked for. Until now every clause in
`docs/draft/01-first-lines.md` was assembled BY HAND and verified word by word; this tool reads a
written clause and reports what the locked rules say about it.

What it implements (the 2026-10-15 rulings plus the locked rules they sit on):

  S4 / M5c / M5d  the agentivity reading of the clause
                    `V1` (`r` + tonic) = "there IS an instigator"   -> participant in NOM (AG)
                    `V2` (`n` + tonic) = "there is NO instigator"   -> participant in ACC (PT)
                    `V0` (bare root)   = the verb itself claims nothing; the reading comes from the
                                         PARTICIPANT'S CASE (RULED 2026-10-15): NOM present =
                                         implicit `V1`, ACC alone = implicit `V2`
  class           advisory, read from the class section of the lexicon (RULED 2026-10-15):
                    `I`   agentive   -> a patientive use is WARNED
                    `II`  patientive -> an agentive use is WARNED
                    `D`   both framings are natural (a causative/anticausative pair) -> never warned
                    `II*` no verb sense recorded -> the NOUN DEFAULT "be / become N" -> never warned
  H2              every word's chord: NOM / V0 / V1 / V2 = I · ACC / GEN = V · oblique / MOD = IV
  H3 / H4 / M4a   the suffix vowels (via `tools/grades.py`, so a root's last syllable nucleus decides)
  H9              a modifier word is a HEAD-COLOURED island (its suffixes take the head's colour)
  M3a             the seam, so `forah` + `-na` is read as `forahna`, never `forana` (via `tools/seam.py`)
  P4c / N1        the stressed form is counted from the ROOT, so a suffix never steals the stress
  R5 / A1 / R6    every content word must come from `reference/example.md` (the only word source)

Severity: **OK** = a locked rule holds · **NOTE** = allowed, but you should know · **WARN** = an
advisory class or structure mismatch. A WARN is the author's call, never a hard failure -- the class
is advisory by construction.

LIMITS (honest): no tense/aspect/mood (M5a, open), no pronouns (M6, open), no number (M4b, open), no
negation scope and no scrambling limits (open) -- those layers do not exist yet, so this tool cannot
check them. It also cannot tell WHICH reading you meant for a clause-final bare word (M5d's known
zero-suffix ambiguity); it prints both readings.

USAGE
    python3 tools/clause.py "orgi sefmehna thyma"       one clause
    python3 tools/clause.py --quiet "orgina Symme res"  chords + warnings only
    python3 tools/clause.py -                           read clauses from stdin, one per line
    python3 tools/clause.py --selftest                  reproduce the known-good clauses
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import syllabify as S      # noqa: E402
import seam as SEAM        # noqa: E402
import grades as G         # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
LEXICON = os.path.normpath(os.path.join(HERE, "..", "reference", "example.md"))

WORD_RE = re.compile(r"^- ([a-z]+) \(")              # `- aba (seed)` + optional trailing prose
CLASS_RE = re.compile(r"^- ([a-z]+) \| ([a-z/]+) \| ([A-Z]+\*?) \| (.+)$")   # the class section

CASES = ("ACC", "GEN", "DAT", "LOC", "INS", "OBL")
VERB_FORMS = ("V1", "V2")
# a word is one of: bare root | root+case | root+Vn | root+MOD | root+MOD+case
SEQUENCES = [()] + [(m,) for m in CASES + VERB_FORMS] + \
            [("MOD",)] + [("MOD", m) for m in CASES]

DEFAULT_CLASS = "II*"          # RULED 2026-10-15: a root with no recorded class is under the noun default
FUNCTION_WORDS = ("ar", "mer", "mei")   # R5: they take no suffixes and are not verb-arguments

def load_lexicon(path=LEXICON):
    """-> (roots, classes). Both come from `reference/example.md`: the word lines give the roots,
    the class section gives (pos, class, verb sense) -- a root with no row there is `II*`."""
    roots, classes = set(), {}
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            ln = raw.rstrip("\n")
            m = CLASS_RE.match(ln.strip())
            if m:
                r, pos, cls, sense = m.groups()
                classes[r] = (pos, cls, sense.strip())
                roots.add(r)
                continue
            m = WORD_RE.match(ln.strip())
            if m:
                roots.add(m.group(1))
    return roots, classes


def surface(root, seq, head=None):
    """The spelling the locked rules produce: M3a (seam) + H9 (head colour) + H3/H4 (the grade vowel).

    -> (spelling, [(morpheme, suffix, chord, tier, note), ...]). The seam is applied to the FIRST
    morpheme only -- chained suffixes can never break phonotactics (M3b).
    """
    cls = G.trigger_class(head) if head else G.trigger_class(root)
    out, parts = root, []
    for i, m in enumerate(seq):
        sfx = G.suffix(m, cls)
        if m == "MOD" and root[-1] not in G.VOWELS:      # a consonant-final root drops the h (R6/H9)
            sfx = sfx[:1] + sfx[2:]
        body = sfx.replace("-", "")
        if i == 0 and body:
            out, tier, note = SEAM.seam(root, body)
        else:
            out += body
            tier, note = 0, "chained suffix: coda + onset is a legal medial CC (M3b)"
        parts.append((m, sfx, G.CHORD[m], tier, note))
    return out, parts


def verb_candidates(word, root):
    """Every LEGAL verb form of `root` that spells `word` — `M4a` finite x `M4c` aspect x `M5f` evid /
    `M5g` mood (the two are mutually exclusive, so the endings list carries both cases).

    This is the only way to decompose an *enhanced* verb form (`thymarissig`, `thymaralin`), because the
    plain `SEQUENCES` table knows nothing about the aspect coda or the outer syllables. The chord of each
    part is the grade's chord, so the LAST part is the word's chord (`M2c`).
    """
    out = []
    endings = [(e, None) for e in (None,) + tuple(G.EVIDENTIAL)] + [(None, m) for m in G.MOOD]
    for fname in ("V0", "V1", "V2"):
        for aname in G.ASPECT:
            for ename, mname in endings:
                surf, _note = G.verb(root, fname, aname, ename, mname)
                if surf != word:
                    continue
                dom = G.ASPECT[aname][1] == "dom"
                labels = [fname, aname] + ([ename] if ename else []) + ([mname] if mname else [])
                chords = [G.CHORD[fname], "V" if dom else "I"] \
                    + (["V" if dom else "IV"] if ename else []) \
                    + (["V"] if mname else [])
                out.append((root, tuple(labels), word,
                            [(lab, "", ch) for lab, ch in zip(labels, chords)], None))
    return out


def decompose(word, roots, heads=(None,)):
    """-> [(root, seq, spelling, parts, head), ...] for every reading whose spelling is exactly `word`.

    `heads` lets a MODIFIER word be re-read with a head's colour (H9); `None` = the root's own colour.
    A bare root comes back as an empty sequence -- it is BOTH the NOM noun and the `V0` verb (M5d), and
    only the clause's structure can say which (see `analyse_clause`).
    """
    out = []
    for root in sorted(roots, key=len, reverse=True):
        if not word.startswith(root):
            continue
        out.extend(verb_candidates(word, root))
        for seq in SEQUENCES:
            if not seq and word != root:
                continue
            for head in (heads if "MOD" in seq else (None,)):
                spell, parts = surface(root, seq, head)
                if spell == word:
                    out.append((root, seq, spell, parts, head))
    return out


def identify(word, roots, looser=False):
    """-> (kind, root, seq, parts, head) -- the best reading of one written word.

    kind: 'function' (R5) | 'bare' (a lexicon root with no suffix) | 'lexeme' (root + morphemes) |
          'unknown' (not in the lexicon) | 'illegal' (not phonotactically legal).
    """
    if word in FUNCTION_WORDS:                      # R5: ar / mer / mei (no suffixes)
        return ("function", word, (), [], None)
    if word in ("a", "e", "o", "i", "u", "ae", "y"):    # H8: a LONE VOWEL word = the article
        return ("function", word, (), [], None)         #     (an initial capital makes it VOC)
    if S.analyse(word)["illegal"]:
        return ("illegal", None, (), [], None)
    if word in roots:
        return ("bare", word, (), [], None)
    heads = tuple(sorted(roots)) if looser else (None,)
    cands = decompose(word, roots, heads)
    if not cands:
        return ("unknown", None, (), [], None)
    cands.sort(key=lambda c: (c[4] is not None, len(c[1])))
    root, seq, _spell, parts, head = cands[0]
    return ("lexeme", root, seq, parts, head)
def analyse_clause(words, roots, classes):
    """One clause (a list of written words) -> {lines, chords, warns, stressed, toks}.

    Every line is tagged OK / NOTE / WARN. A WARN is advisory (the class is advisory by
    construction); nothing here is a hard failure.
    """
    lines, warns, chords = [], [], []
    toks = []
    for w in words:
        key = w.lower()          # the docs write stress capitals (`orGi`): analyse the bare spelling,
        kind, root, seq, parts, head = identify(key, roots)     # keep the original for display
        if kind in ("unknown", "illegal"):
            kind, root, seq, parts, head = identify(key, roots, looser=True)   # H9: head-coloured MOD
        cls = classes[root][1] if root in classes else (DEFAULT_CLASS if kind in ("bare", "lexeme") else None)
        toks.append({"word": w, "key": key, "kind": kind, "root": root, "seq": seq,
                     "parts": parts, "head": head, "cls": cls})

    def say(tag, text):
        lines.append("%-4s %s" % (tag, text))
        if tag == "WARN":
            warns.append(text)

    # --- 1. every written word must be a word -------------------------------------------------
    for t in toks:
        if t["kind"] == "illegal":
            say("WARN", "`%s` is not phonotactically legal at all (tools/syllabify.py --check)" % t["word"])
        elif t["kind"] == "unknown":
            say("WARN", "`%s` is not in reference/example.md -- not a coined word yet (the only word source)"
                % t["word"])

    # --- 2. roles and chords (H2 + M2c) --------------------------------------------------------
    for t in toks:
        parts = t["parts"]
        if t["kind"] == "function":
            t["role"], t["chord"] = "function (R5)", None
        elif parts and any(p[0] == "MOD" for p in parts):
            t["role"] = "modifier" + ("" if parts[-1][0] == "MOD" else " + " + parts[-1][0])
            t["chord"] = parts[-1][2]                   # M2c: the OUTERMOST suffix sounds the chord
        elif parts and (parts[0][0] in ("V0", "V1", "V2") or parts[-1][0] in VERB_FORMS):
            # a plain finite ending (`V1`) OR a full verb form (`V1+progressive+witnessed`, M4c/M5f)
            t["role"] = "verb " + "+".join(p[0] for p in parts)
            t["chord"] = parts[-1][2]                   # the outermost category sounds the chord
        elif parts and parts[-1][0] in CASES:
            t["role"], t["chord"] = "argument " + parts[-1][0], parts[-1][2]
        else:
            # a bare root: NOM noun or V0 verb -- the chord is I either way (H2); the ROLE is
            # resolved in `_finish` (clause-final = the verb, S2's default)
            t["role"], t["chord"] = "bare (NOM noun OR V0 verb)", G.CHORD["NOM"]
        if t["chord"]:
            chords.append(t["chord"])
        if len(t["parts"]) > 1:
            inner = ", ".join(p[0] + " " + p[2] for p in t["parts"][:-1])
            say("NOTE", "`%s` carries 2 suffixes (%s); M2c: the OUTERMOST one (%s) is its chord"
                % (t["word"], inner, parts[-1][0]))
    return _finish(toks, chords, lines, warns, classes)




def _finish(toks, chords, lines, warns, classes):
    """Steps 3-6 of the report: the verb, the agentivity reading, the class, the stressed line."""
    def say(tag, text):
        lines.append("%-4s %s" % (tag, text))
        if tag == "WARN":
            warns.append(text)

    # --- 3. the verb (S2: verb-final is the default) -----------------------------------------
    verbs = [t for t in toks if t["parts"]
             and (t["parts"][0][0] in ("V0", "V1", "V2") or t["parts"][-1][0] in VERB_FORMS)]
    if len(verbs) > 1:
        say("WARN", "more than one verb form in the clause (%s)" % ", ".join(t["word"] for t in verbs))
    v0 = None
    if not verbs and toks and toks[-1]["chord"] == G.CHORD["NOM"] and not toks[-1]["parts"]:
        v0 = toks[-1]
        v0["role"] = "verb V0 (bare)"
        say("NOTE", "`%s` is bare: it is BOTH a NOM noun and a bare `V0` verb (M5d) -- read here as the "
            "verb because it is clause-final (S2's default)" % v0["word"])
    elif not verbs:
        say("NOTE", "no verb form in the clause (a bare word is still NOM-or-V0, M5d)")

    # --- 4. the agentivity reading (S4 / M5c / M5d + the V0 ruling of 2026-10-15) ------------
    nom = [t for t in toks if t["role"].startswith("bare (NOM")]
    acc = [t for t in toks if t["role"] == "argument ACC"]
    form = verbs[-1]["parts"][0][0] if verbs else ("V0" if v0 else None)
    reading = None
    if form in ("V1", "V2"):
        reading = form
        say("OK", "verb form `%s`: %s" % (form, "there IS an instigator" if form == "V1"
                                         else "there is NO instigator"))
    elif form == "V0":
        if nom:
            reading, why = "implied V1", "a NOM (AG) participant is present"
        elif acc:
            reading, why = "implied V2", "only an ACC (PT) participant is present"
        else:
            reading, why = None, "no participant at all"
        say("NOTE", "`V0` claims nothing, so the reading comes from the PARTICIPANT'S CASE -> %s (%s)"
            % (reading or "undefined", why))
    if reading == "V2" and nom:
        say("WARN", "a `V2` clause has no A (S4 derived rule a): the participant must be ACC, but `%s` "
            "is NOM" % nom[0]["word"])
    if form and verbs and toks and verbs[-1] is not toks[-1]:
        say("NOTE", "the verb is not clause-final: allowed (S2 free scrambling); verb-final is the default")

    # --- 5. the CLASS (advisory; RULED 2026-10-15) -------------------------------------------
    vtok = verbs[-1] if verbs else v0
    if vtok:
        cls = vtok["cls"]
        if cls == "D":
            say("NOTE", "`%s` is class D: both framings are natural (causative / anticausative pair)"
                % vtok["root"])
        elif cls == "II*":
            say("NOTE", "`%s` has no recorded class -> the NOUN DEFAULT: 'be / become N'" % vtok["root"])
        else:
            patientive = reading in ("V2", "implied V2")
            agentive = reading in ("V1", "implied V1")
            if cls == "I" and patientive:
                say("WARN", "`%s` is class I (agentive) but is used with a PATIENTIVE reading"
                    % vtok["root"])
            elif cls == "II" and agentive:
                say("WARN", "`%s` is class II (patientive) but is used with an AGENTIVE reading"
                    % vtok["root"])
            else:
                say("OK", "class %s and the %s reading agree" % (cls, reading or form))

    # --- 7. the `M5f` stop licence (`A1`/`P3`'s ONE exception) ---------------------------------
    for t in toks:
        if t["key"][-1] in ("b", "d", "g") and not any(p[0] in G.EVIDENTIAL for p in t["parts"]):
            say("WARN", "`%s` ends in a stop, and a word-final stop is legal ONLY as the evidential "
                "suffix (`M5f`, `A1`'s one exception) -- so this form must be a verb carrying an "
                "evidential (or it is a mis-harmonised spelling of one)" % t["word"])

    # --- 6. the stressed line (P4c: counted from the ROOT; N1: capital on the syllable's 1st letter)
    marked = []
    for t in toks:
        if t["kind"] == "function":     # R5 / H8 words have no root: no stress mark. (P4 covers ROOTS;
            marked.append(t["word"])    # function-word stress is still open, §0 item 30 -- and marking
            continue                    # `a` as `A` would wrongly read as VOC, the H8 open case §0 item 4)
        m = SEAM.mark(t["key"], t["root"] or t["key"])
        marked.append(m[2] if m else t["word"])
    return {"lines": lines, "chords": chords, "warns": warns, "toks": toks,
            "stressed": " ".join(marked)}


SELFTEST = [    # (clause, expected chords, must there be a WARN?)
    ("orgi thyma",                 "I-I",       False),
    ("orgi sefmehna thyma",        "I-V-I",     False),
    ("orgi thymara",               "I-I",       False),
    ("orgina res",                 "V-I",       False),
    ("orgi sefmehna os",           "I-V-I",     False),
    ("orgina Symme res",           "V-IV-I",    False),
    ("sefmehna Symme osno",        "V-IV-I",    True),    # os is class I: patientive use
    ("hosdahes sefmehna thymara",  "IV-V-I",    False),   # a head-coloured modifier (H9)
    ("orgi Resne",                 "I-I",       True),    # V2 clause with a NOM participant (S4 a)
    ("sefmehna thymara",           "V-I",       False),
]

N1_PINS = [      # (form, root, expected stressed spelling) -- N1 as AMENDED 2026-10-15
    ("sefmehna",   "sefmeh", "sefMehna"),
    ("hosdahesna", "hosda",  "hosDahesna"),
    ("argonna",    "argonna", "arGonna"),
    ("orgina",     "orgi",   "orGina"),
    ("resne",      "res",    "Resne"),
    ("walunu",     "walu",   "waLunu"),
    ("forahna",    "forah",  "foRahna"),
    ("forara",     "forah",  "foRara"),
]


def selftest():
    roots, classes = load_lexicon()
    bad = 0
    for clause, want, want_warn in SELFTEST:
        res = analyse_clause(clause.split(), roots, classes)
        got = "-".join(res["chords"])
        ok = got == want and bool(res["warns"]) == want_warn
        bad += 0 if ok else 1
        print("%s %-28s chords %-8s expected %-8s warn %s"
              % ("OK  " if ok else "FAIL", clause, got, want, "yes" if res["warns"] else "no"))
        if not ok:
            for ln in res["lines"]:
                print("       | " + ln)
    for form, root, want in N1_PINS:
        got = (SEAM.mark(form, root) or (None, None, None))[2]
        ok = got == want
        bad += 0 if ok else 1
        print("%s N1 %-12s (root %-8s) -> %-12s expected %s"
              % ("OK  " if ok else "FAIL", form, root, got, want))
    print("\nlexicon: %d roots, %d with a class row (%s)"
          % (len(roots), len(classes), " ".join(sorted(classes))))
    print("self-test:", "ALL PASS" if not bad else "%d FAILURE(S)" % bad)
    return 0 if not bad else 1


def report(clause, roots, classes, quiet=False):
    res = analyse_clause(clause.split(), roots, classes)
    print("clause: %s" % clause)
    print("  stressed (P4c): %s" % res["stressed"])
    if not quiet:
        for t in res["toks"]:
            parts = "+".join(p[0] for p in t["parts"]) or "bare"
            print("  %-13s %-9s %-16s %-9s %s"
                  % (t["word"], t["root"] or "-", parts,
                     ("class " + t["cls"]) if t["cls"] else "-", t["role"]))
    for ln in res["lines"]:
        print("  " + ln)
    print("  chords: %s   [%d WARN]" % (" - ".join(res["chords"]) if res["chords"] else "(none)",
                                        len(res["warns"])))
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check a written clause against the locked rules.")
    ap.add_argument("words", nargs="*", help="the clause (quoted, or one word per argument)")
    ap.add_argument("--quiet", action="store_true", help="chords + notes only, no word table")
    ap.add_argument("--selftest", action="store_true", help="reproduce the known-good clauses")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    roots, classes = load_lexicon()
    if not args.words or args.words == ["-"]:
        bad = 0
        for ln in sys.stdin:
            ln = ln.strip()
            if ln and not ln.startswith("#"):
                bad += 1 if report(ln, roots, classes, args.quiet)["warns"] else 0
                print()
        return 1 if bad else 0
    report(" ".join(args.words), roots, classes, args.quiet)
    return 0


if __name__ == "__main__":
    sys.exit(main())

