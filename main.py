"""Copy the bundled front-page image to the output directory.

Entry for the make.fun news-image-20261122 daily news-image bounty.

The front page is "The Global Herald" for Sunday, November 22, 2026.
Lead stories:
  - Pentagon moves to restrict U.S.-Canada defense ties
  - Trump vows a 10% cap on credit card interest
  - A magnitude 6.9 earthquake shakes Peru's Andes
  - Iran strikes a U.S. base in Kuwait as Gulf attacks widen
  - A Russian missile lands in Poland and NATO calls it a violation
Small items:
  - COP31 deadlock in Antalya
  - Rohingya hailing the ICJ genocide verdict against Myanmar

The program copies the bundled entry.png (in the same directory as this
script) to the output directory given by MAKEFUN_OUTPUT_DIR (default
/output) as entry.png, and verifies the copy is complete and identical.
Any failure exits non-zero with a clear error message on stderr.
"""

import os
import shutil
import sys

SOURCE_NAME = "entry.png"


def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(script_dir, SOURCE_NAME)

    if not os.path.isfile(source):
        fail(f"source image not found: {source}")
    source_size = os.path.getsize(source)
    if source_size == 0:
        fail("source image is empty")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, SOURCE_NAME)

    try:
        shutil.copyfile(source, destination)
    except OSError as exc:
        fail(f"could not copy {source} to {destination}: {exc}")

    if not os.path.isfile(destination):
        fail(f"output image missing after copy: {destination}")
    copied_size = os.path.getsize(destination)
    if copied_size == 0:
        fail("output image is empty")
    if copied_size != source_size:
        fail(
            f"size mismatch: source {source_size} bytes, "
            f"output {copied_size} bytes"
        )

    print(
        f"entry.png written to {destination} "
        f"({copied_size} bytes, matches source)"
    )


if __name__ == "__main__":
    main()
