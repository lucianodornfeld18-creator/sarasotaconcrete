# -*- coding: utf-8 -*-
"""Style QA over dist/: forbidden phrases (prompt 9.2), network fingerprints (prompt 2.2), 'ensure' count,
em-dash count, emoji, sentence-length distribution, fact density (numbers/units/citations per 150 words)."""
import html
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
DIST = pathlib.Path(__file__).resolve().parent / "dist"

FORBIDDEN = ["In today's fast-paced world", "Whether you're", "whether you are", "Look no further", "It's important to note", "It is important to note",
             "It's worth noting", "In conclusion", "Ultimately", "At the end of the day", "When it comes to", "elevate", "seamless", "unlock", "delve",
             "robust", "leverage", "game-changer", "transform your outdoor space", "dream outdoor space", "backyard oasis", "backyard paradise",
             "coastal oasis", "Florida lifestyle", "we understand that", "our team of experts", "top-notch", "state-of-the-art", "cutting-edge",
             "meticulous", "comprehensive", "hassle-free", "peace of mind", "stand the test of time", "a testament to", "nestled", "vibrant",
             "boasts", "tapestry", "not only", "from start to finish", "one-stop shop", "we've got you covered", "enhance", "utilize", "in order to",
             "Let's dive in", "Here's the thing", "Why Choose Us", "Conclusion"]
FINGERPRINTS = ["38-Point", "42-Point", "-Point Install", "Our Four Promises", "Straight answers before you spend a dollar", "in plain English",
                "Built Local Since", "Poured right. Built to last.", "Every surface we pour", "24 cities. One crew.", "Real Sarasota addresses",
                "Be the first", "homeowners ask, weekly", "Concrete Specialists Serving", "Neighborhoods & ZIP Codes We Serve", "done the right way",
                "the questions buyers search", "Five expensive", "Where we work in", "Local concrete & paver crew"]
DENSITY_EXEMPT = {"/gallery/"}

FACT_RE = re.compile(r"\b\d[\d,\.]*\s*(%|percent|sq ft|square|in\.|inch|inches|ft|feet|miles?|°F|degrees|PSI|psi|yrs?|years?|days?|hours?|weeks?|months?|nm|lb|tons?|cm|kW)"
                     r"|\$\d|\b(19|20)\d\d\b|Zone [AVX]E?|F\.S\.|Ch\.|Article|§"
                     r"|\b(one|two|three|four|five|six|seven|eight|nine|ten|twelve|thirty)\s+(to\s+\w+\s+)?(weeks?|months?|days?|hours?|years?|inches|feet|percent|working days)\b"
                     r"|\b(Statute|Ordinance|Code|Census|EDR|NOAA|USDA|FEMA|FWC|DBPR|ACI|ICPI|ANSI|Accela|eTRAKiT|Click2Gov|FTG)\b", re.I)


def main_text(h):
    m = re.search(r"<main.*?</main>", h, re.S)
    t = m.group(0) if m else h
    t = re.sub(r"<form.*?</form>", " ", t, flags=re.S)
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def main():
    report, worst = {}, []
    for f in sorted(DIST.rglob("index.html")):
        route = ("/" + f.parent.relative_to(DIST).as_posix().strip(".") + "/").replace("//", "/")
        t = main_text(f.read_text(encoding="utf-8"))
        low = t.lower()
        probs = []
        for ph in FORBIDDEN:
            n = len(re.findall(r"\b" + re.escape(ph.lower()) + r"s?\b", low))
            if n:
                probs.append(f"forbidden '{ph}' x{n}")
        for fp in FINGERPRINTS:
            if fp.lower() in low:
                probs.append(f"fingerprint '{fp}'")
        ens = len(re.findall(r"\bensure", low))
        if ens > 1:
            probs.append(f"'ensure' x{ens}")
        em = t.count("—")
        if em > 3:
            probs.append(f"em-dash x{em}")
        if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", t):
            probs.append("emoji")
        sents = [s for s in re.split(r"(?<=[.!?])\s+", t) if len(s.split()) > 2]
        lens = [len(s.split()) for s in sents]
        if lens:
            long_ = sum(1 for x in lens if x >= 35) / len(lens)
            if long_ > 0.5:
                probs.append(f"sentence length: {long_:.0%} sentences over 35 words")
        words = len(re.findall(r"[A-Za-z][A-Za-z'\-]+", t))
        facts = len(FACT_RE.findall(t))
        density = facts / max(words, 1) * 150
        # /gallery/ is exempt: its body is 26 photo captions, which are descriptive by design.
        # Forcing numbers into image captions would make them worse, not more verifiable.
        if words > 300 and density < 1.0 and route not in DENSITY_EXEMPT:
            probs.append(f"fact density {density:.2f} per 150 words")
        report[route] = {"words": words, "facts_per_150": round(density, 2), "sentences": len(lens), "avg_sentence": round(sum(lens) / len(lens), 1) if lens else 0, "problems": probs}
        if probs:
            worst.append((route, probs))
    (DIST.parent / "qa-style-report.json").write_text(json.dumps(report, indent=1), encoding="utf-8")
    print(f"{len(report)} pages checked; {len(worst)} with problems")
    for r, ps in worst:
        print(r, "->", "; ".join(ps))


if __name__ == "__main__":
    main()
