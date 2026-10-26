# goit-pycore-hw-04

Homework for topic 6 of the course "Python Programming: Foundations and Best Practices 2.0": working with files and the module system.

| File | Task |
|---|---|
| `task_1.py` | `total_salary(path)` — total and average salary from `data/salaries.txt` |
| `task_2.py` | `get_cats_info(path)` — list of cats from `data/cats.txt` |
| `task_3.py` | directory tree with colored names (colorama) |
| `task_4.py` | console assistant bot with a phone book |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python task_1.py
python task_2.py
python task_3.py /path/to/directory
python task_4.py
```

Bot commands (case-insensitive): `hello`, `add <name> <phone>`, `change <name> <phone>`, `phone <name>`, `all`, `close` / `exit`; Ctrl+C or Ctrl+D also exits.
