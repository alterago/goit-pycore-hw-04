"""Task 2: read information about cats from a text file."""

from pathlib import Path

ENCODING = "utf-8"
FIELDS = ("id", "name", "age")


def get_cats_info(path: str | Path) -> list[dict[str, str]]:
    """Return a list of dicts with the keys 'id', 'name' and 'age'.

    Each line of the file is 'id,name,age'. Lines that cannot be parsed are
    skipped with a warning. A missing or unreadable file gives an empty list.
    """
    cats = []
    try:
        with open(path, encoding=ENCODING) as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue
                values = line.split(",")
                if len(values) != len(FIELDS):
                    print(f"Skipping malformed line {line_number}: {line!r}")
                    continue
                cats.append(dict(zip(FIELDS, values)))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except (OSError, UnicodeDecodeError) as error:
        print(f"Cannot read file {path}: {error}")
        return []

    return cats


if __name__ == "__main__":
    cats_file = Path(__file__).parent / "data" / "cats.txt"
    cats_info = get_cats_info(cats_file)
    print(cats_info)
