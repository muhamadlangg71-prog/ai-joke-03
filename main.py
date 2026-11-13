"""ai-joke-03 entry: writes one deterministic joke about AI coding agents.

The joke is a fixed string. No network, no randomness, no clock:
both runs write the exact same bytes.
"""

import os

JOKE = (
    "My AI agent promised it would never hallucinate. "
    "Then it invented a library, imported it, and the build passed."
)


def main() -> None:
    if not 1 <= len(JOKE) <= 280:
        raise ValueError("joke must be 1-280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
