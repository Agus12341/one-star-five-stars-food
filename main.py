#!/usr/bin/env python3
"""Write the alien one-star review of Earth to entry.txt in the output folder."""

import os

# One sentence from an alien tourist: one star for Earth, five stars
# for its food. Picked from five drafts judged pairwise on the kit's
# criteria (a one-star alien review that still compliments the food
# first, then a convincing outsider's voice, both halves landing, one
# sentence with every word earning its place, and a fresh angle). The
# grievance is the applauding when a plane lands; the compliment is
# the cheese melted on everything, including other cheese. The gate
# checks entry.txt as UTF-8 text of 1 to 200 characters: this
# sentence is 181 code points, 182 with its trailing newline
# (verified by a local run, byte for byte, and it stays a single
# sentence: one full stop, at the end).
TEXT = "One star for the noise, the queues and a species that applauds when its own aircraft lands, but five stars for the cheese they melt on absolutely everything, including other cheese."


def write_entry(out_dir: str) -> None:
    """Write the review, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
