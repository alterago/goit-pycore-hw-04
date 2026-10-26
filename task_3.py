"""Task 3: show the structure of a directory with colored names.

Usage: python task_3.py /path/to/directory
"""

import sys
from pathlib import Path

from colorama import Fore, Style, init

DIRECTORY_COLOR = Fore.BLUE + Style.BRIGHT
FILE_COLOR = Fore.GREEN
ERROR_COLOR = Fore.RED

BRANCH = "┣ "
LAST_BRANCH = "┗ "
PIPE = "┃ "
SPACE = "  "


def sorted_entries(directory: Path) -> list[Path]:
    """Return the directory's entries: subdirectories first, then files, by name."""
    return sorted(directory.iterdir(), key=lambda entry: (not entry.is_dir(), entry.name.lower()))


def print_tree(directory: Path, prefix: str = "") -> None:
    """Print the contents of ``directory`` recursively as a tree."""
    try:
        entries = sorted_entries(directory)
    except PermissionError:
        print(f"{prefix}{LAST_BRANCH}{ERROR_COLOR}[permission denied]{Style.RESET_ALL}")
        return

    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = LAST_BRANCH if is_last else BRANCH
        if entry.is_dir():
            print(f"{prefix}{connector}{DIRECTORY_COLOR}📂 {entry.name}{Style.RESET_ALL}")
            print_tree(entry, prefix + (SPACE if is_last else PIPE))
        else:
            print(f"{prefix}{connector}{FILE_COLOR}📜 {entry.name}{Style.RESET_ALL}")


def main() -> None:
    init(autoreset=True)

    if len(sys.argv) != 2:
        print(f"{ERROR_COLOR}Usage: python {Path(sys.argv[0]).name} /path/to/directory")
        sys.exit(1)

    directory = Path(sys.argv[1])
    if not directory.exists():
        print(f"{ERROR_COLOR}Path does not exist: {directory}")
        sys.exit(1)
    if not directory.is_dir():
        print(f"{ERROR_COLOR}Path is not a directory: {directory}")
        sys.exit(1)

    print(f"{DIRECTORY_COLOR}📦 {directory.resolve().name}{Style.RESET_ALL}")
    print_tree(directory)


if __name__ == "__main__":
    main()
