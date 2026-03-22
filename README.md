# Python Practice

A structured collection of Python fundamentals and advanced topics, organized as a learning roadmap.

## Folder Structure

| #  | Folder | Topics Covered |
|----|--------|---------------|
| 01 | `01_fundamentals/` | Variables, strings, data types, basic I/O, class basics |
| 02 | `02_oop/` | Encapsulation, inheritance |
| 03 | `03_functional/` | Lambda, map, filter, optional parameters |
| 04 | `04_collections/` | Counter, collections module |
| 05 | `05_decorators/` | Decorators theory, practice, exercises & solutions |
| 06 | `06_iterators/` | Iterator protocol, custom iterators |
| 07 | `07_generators/` | Generator functions, reading large files |
| 08 | `08_file_handling/` | File read/write/append, assignments |
| 09 | `09_exceptions/` | Exception handling, try/except/finally |
| 10 | `10_json/` | JSON parsing, serialization, dict practice |
| 11 | `11_api_testing/` | Requests library, API automation, reference scripts |
| 12 | `12_logging/` | basicConfig, custom loggers, file handlers |
| 13 | `13_threading_multiprocessing/` | Threading, multiprocessing (notebooks + scripts) |
| 14 | `14_dsa/` | Data structures — singly linked list |
| 90 | `90_sandbox/` | Miscellaneous / experimental scripts |

## Conventions

- **Folders** are numbered for learning order and use `snake_case`.
- **Files** inside each folder are numbered (`01_`, `02_`, …) for sequencing.
- **Data files** (`.json`, `.txt`, `.log`) live in a `data/` (or `logs/`) subfolder within each topic.
- **Solutions / references** are placed in a `solutions/` or `references/` subfolder.

## How to Use

1. Start from `01_fundamentals/` and work your way up.
2. Each folder is self-contained — run any `.py` file from **inside its folder**:
   ```
   cd 10_json
   python 01_json_basics.py
   ```
3. Notebooks (`.ipynb`) are in `13_threading_multiprocessing/notebooks/`.
