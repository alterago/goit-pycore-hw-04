"""Task 1: total and average salary from a text file."""

from pathlib import Path

ENCODING = "utf-8"


def parse_salary(value: str) -> int | float:
    """Return the salary as int when it is whole, otherwise as float."""
    number = float(value)
    return int(number) if number.is_integer() else number


def total_salary(path: str | Path) -> tuple[int | float, int | float]:
    """Return the total and the average salary of the developers in the file.

    Each line of the file is 'Full Name,salary'. Lines that cannot be parsed
    are skipped with a warning. A missing or unreadable file, or a file without
    valid lines, gives (0, 0).
    """
    salaries = []
    try:
        with open(path, encoding=ENCODING) as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    _, salary = line.split(",")
                    salaries.append(parse_salary(salary))
                except ValueError:
                    print(f"Skipping malformed line {line_number}: {line!r}")
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0, 0
    except (OSError, UnicodeDecodeError) as error:
        print(f"Cannot read file {path}: {error}")
        return 0, 0

    if not salaries:
        return 0, 0

    total = sum(salaries)
    average = total / len(salaries)
    return total, int(average) if float(average).is_integer() else average


if __name__ == "__main__":
    salary_file = Path(__file__).parent / "data" / "salaries.txt"
    total, average = total_salary(salary_file)
    print(f"Total salary: {total}, Average salary: {average}")
