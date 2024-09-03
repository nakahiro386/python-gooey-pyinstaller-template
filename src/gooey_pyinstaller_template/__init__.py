import argparse
import codecs
import logging
import sys
from pathlib import Path

from gooey import Gooey

__bundle_dir = str(
    Path(getattr(sys, "_MEIPASS")) / "languages"  # noqa: B009
    if getattr(sys, "frozen", False)
    else Path.cwd() / "languages"
)


@Gooey(
    program_name="gooey-pyinstaller-template",
    language="japanese",
    language_dir=__bundle_dir,
)  # type: ignore[misc]
def main() -> int:
    # pyinstaller to exe,run the exe, and it cannot end after completion · Issue #810 · chriskiehl/Gooey · GitHub
    # https://github.com/chriskiehl/Gooey/issues/810
    if sys.stdout is not None and sys.stdout.encoding != "UTF-8":
        sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer, "strict")
    if sys.stderr is not None and sys.stderr.encoding != "UTF-8":
        sys.stderr = codecs.getwriter("utf-8")(sys.stderr.buffer, "strict")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--log",
        choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"],
        default="INFO",
    )
    args = parser.parse_args()

    log_format = "%(asctime)s:%(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(format=log_format, level=getattr(logging, args.log))

    __logger = logging.getLogger(__name__)
    __logger.info(args)

    print("Hello from gooey-pyinstaller-template!")
    return 0
