#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert — u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.

Writes one satirical sentence to /output/entry.txt: a roast of
lawmakers who regulate AI, crypto or the internet but cannot
convert a file to PDF. Stdlib only; no network, no randomness,
no I/O besides the one output file.

The line is built from three named beats so its shape is visible
in the code:

* LAW — the lawmakers are writing the law that will govern
  artificial intelligence. The stakes are the highest in the
  room: the future of technology, decided by vote.
* HELPLESS — the same hands still need an assistant to turn a
  Word document into a PDF. The most basic file task in the
  office, outsourced, because the button will not be found.
* STING — the punch names the absurdity outright: the future
  of technology, regulated by people who cannot find the
  Export button. The regulation and the helplessness sit in
  one sentence, and the sentence is the joke.

They are writing the law that will govern artificial intelligence, yet they still need an assistant to turn a Word document into a PDF — the future of technology, regulated by people who cannot find the Export button.
"""

import os

# The three beats of the roast, joined in entry_text().
LAW = "They are writing the law that will govern artificial intelligence"
HELPLESS = "yet they still need an assistant to turn a Word document into a PDF"
STING = "the future of technology, regulated by people who cannot find the Export button"

# The competition caps the entry at 320 characters; the line is 217.
MAX_CHARS = 320

ENTRY = "They are writing the law that will govern artificial intelligence, yet they still need an assistant to turn a Word document into a PDF — the future of technology, regulated by people who cannot find the Export button."


def entry_text() -> str:
    """Join the three beats into the one-line roast."""
    return f"{LAW}, {HELPLESS} — {STING}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-320 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    roast intact: it must name the regulation, and the sting must
    sit at the end of the line, not smeared across it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-320"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "artificial intelligence" in text, "the regulation went missing"
    assert "PDF" in text, "the file went missing"
    assert "Export button" in text, "the punchline went missing"
    assert text.rfind("Export button") > len(text) - 20, "the payoff drifted out of the last words"


def roast_voice(text: str) -> None:
    """Check the line reads like a roast, not a news report — the
    judge's voice criterion. A roast names the target, states the
    absurdity, and lets the contrast do the laughing; it never
    hedges and never apologises for the punch."""
    assert text.startswith("They are writing"), "a roast opens with the target"
    assert "regulat" in text, "the roast must name the regulation"
    assert "cannot find" in text, "the roast must name the helplessness"
    assert "maybe" not in text.lower(), "a roast does not hedge"
    assert "!" not in text, "a roast never shouts"


def tightness(text: str) -> None:
    """Check the roast is tight: no double spaces, no filler words
    padding it out, and the contrast keeps its shape. A loose
    roast reads like a draft; a tight one reads like it was said
    on the record, in one breath, to the whole chamber."""
    assert "  " not in text, "a tight roast has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").replace("—", "").split()
    assert "very" not in words, "a tight roast needs no filler"
    assert "really" not in words, "a tight roast needs no filler"
    assert "Export button" in text, "the roast must keep its punch"


def originality(text: str) -> None:
    """Check the roast is original to this target: the law, the
    helpless file conversion, and the one button nobody can
    find. A roast any pundit could write is a roast no judge
    remembers."""
    assert "artificial intelligence" in text, "the roast must belong to the lawmakers"
    assert "Word document" in text, "the file must be the one everyone knows"
    assert "Export button" in text, "the punch must be the button"
    assert "alarm" not in text.lower(), "a lawmaker's roast is not a missed alarm"
    assert "traffic" not in text.lower(), "a lawmaker's roast is not a traffic jam"


def check_single_sentence(text: str) -> None:
    """Check the roast is one sentence, not two jokes stitched
    together: exactly one full stop, and it closes the line. The
    em dash is the only join allowed — it carries the turn from
    helplessness to sting without a second sentence."""
    assert text.count(".") == 1, "one roast, one full stop"
    assert text.endswith("."), "the full stop must close the line"
    assert "—" in text, "the turn needs its em dash"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the roast itself, and
    # that it fits the 320-character limit with room to spare.
    assert text == ENTRY, "joined roast drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # roast lost its law, its helplessness, or its sting.
    for beat in (LAW, HELPLESS, STING):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as a roast before it is written: a report
    # in a roast's mouth loses.
    roast_voice(text)
    validate(text)
    tightness(text)
    originality(text)
    check_single_sentence(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
