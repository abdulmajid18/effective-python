import os.path
from pathlib import Path

path = os.path.abspath(
    os.sep.join(
        ["", "Users", "dusty", "subdir", "subsubdir", "file.ext"]
    )
)
print(path)

path = Path("/Users") / "dusty" / "subdir" / "subsubdir" / "file.ext"
print(path)

from pathlib import Path
from typing import Callable


def scan_python_1(path: Path):
    sloc = 0
    with path.open() as source:
        for line in source:
            line = line.strip()
            if line and not line.startswith("#"):
                sloc += 1
    return sloc


def count_sloc(path: Path, scanner: Callable[[Path], int]) -> int:
    if path.name.startswith("."):
        return 0
    elif path.is_file():
        if path.suffix != ".py":
            return 0
        with path.open() as source:
            return scanner(path)
    elif path.is_dir():
        count = sum(
            count_sloc(name, scanner) for name in path.iterdir())
        return count
    else:
        return 0
