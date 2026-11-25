"""One-line roast of a fridge for the roast-your-fridge bounty.

Writes the proxy-tournament winning line (R1) to /output/entry.txt: the fridge
hums all night like it is working hard, and the twist is that the only thing
it has ever finished is the milk. Chosen from six candidates by a Groq proxy
bracket judged against the published judge brief.
"""
from pathlib import Path

ENTRY = "My fridge hums all night like it is busy, but the only thing it has ever finished is the milk."  # R1, bracket winner


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
